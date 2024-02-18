import factory

from .database import Session


class OnlyIdSubFactory(factory.SubFactory):
    def evaluate(self, instance, step, extra):
        if step.builder.factory_meta._is_transactional and step.sequence > 0:
            session = step.builder.factory_meta.sqlalchemy_session
            transactional_instance = session.query(
                step.builder.factory_meta.model,
            ).first()
            if transactional_instance:  # pragma: no branch
                related_field = step.builder.factory_meta._related_id_field
                return getattr(transactional_instance, related_field)
        result = super().evaluate(instance, step, extra)
        return result.id


class TransactionalVerboseSQLAlchemyOptions(factory.alchemy.SQLAlchemyOptions):
    def _build_default_options(self):
        return super()._build_default_options() + [
            factory.base.OptionDefault('_related_id_field', None),
            factory.base.OptionDefault('_is_transactional', False),
        ]


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base Factory with support of verbose_id and transaction verbose_id."""

    _options_class = TransactionalVerboseSQLAlchemyOptions

    class Meta:
        """Factory configuration."""

        sqlalchemy_session = Session
        sqlalchemy_session_persistence = 'commit'

    @classmethod
    def _save(cls, model_class, session, args, kwargs):
        obj = model_class(*args, **kwargs)
        if cls._meta._is_transactional:
            kwargs['id'] = cls.add_next_with_verbose(
                model_class,
                session,
                obj,
                cls._meta._related_id_field,
            )
        return super()._save(model_class, session, args, kwargs)

    @classmethod
    def add_next_with_verbose(cls, model_class, session, obj, related_id_field):
        new_suffix = 0
        related_id_value = getattr(obj, related_id_field)
        if session.query(
            session.query(model_class)
            .filter(model_class.__dict__[related_id_field] == related_id_value)
            .exists(),
        ).scalar():
            last_obj = (
                session.query(model_class)
                .order_by(
                    model_class.id.desc(),
                )
                .first()
            )
            _instance_id, suffix = last_obj.id.rsplit("-", 1)
            new_suffix = int(suffix) + 1
        else:
            id_body = related_id_value.split("-", 1)[-1]
            _instance_id = f"{model_class.PREFIX}-{id_body}"

        new_id = "{0}-{1}".format(_instance_id, "{0:03d}".format(new_suffix))
        return new_id
