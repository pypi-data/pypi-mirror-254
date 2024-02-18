import os
import random
from contextlib import contextmanager

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.exc import DontWrapMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from connect.eaas.core.inject.common import get_config


_MAX_RETRIES = 1000
_ENGINE = None


def _get_numeric_string(size):
    sys_random = random.SystemRandom()
    return str(sys_random.randint(1 * 10 ** (size - 1), 1 * 10**size - 1))


def _generate_verbose_id(prefix):
    return (
        f"{prefix}-{_get_numeric_string(3)}" f"-{_get_numeric_string(3)}-{_get_numeric_string(3)}"
    )


class VerboseSessionError(Exception, DontWrapMixin):
    """
    Exception class to handle errors through custom methods of `VerboseBaseSession`.
    """


class VerboseBaseSession(Session):
    """
    Custom `sqlalchemy.orm.Session` class to generate and add verbose_id to a model.
    """

    def _set_verbose(self, instance):
        instance_class = instance.__class__
        for _ in range(1, _MAX_RETRIES + 1):
            verbose_id = _generate_verbose_id(instance_class.PREFIX)
            if not (
                self.query(
                    self.query(instance_class).filter(instance_class.id == verbose_id).exists(),
                ).scalar()
            ):
                instance.id = verbose_id
                return instance

        raise VerboseSessionError(
            f"Could not generate {instance_class.__name__} verbose ID"
            f" after {_MAX_RETRIES} attempts.",
        )

    def _set_verbose_all(self, instances):
        checked_instances = []
        if instances:
            count = len(instances)
            instance_class = instances[0].__class__
            all_same_class_check = all(isinstance(ins, instance_class) for ins in instances)
            assert all_same_class_check, "All instances must be of the same class."
            instance_class = instances[0].__class__
            for _ in range(1, _MAX_RETRIES + 1):
                ids = [_generate_verbose_id(instance_class.PREFIX) for _ in range(count)]
                if not (
                    self.query(
                        self.query(instance_class).filter(instance_class.id.in_(ids)).exists(),
                    ).scalar()
                ):
                    break
                ids = []
            if not ids:
                raise VerboseSessionError(
                    f"Could not generate a group of {count} {instance_class.__name__} verbose ID"
                    f" after {_MAX_RETRIES} attempts.",
                )

            for instance, verbose_id in zip(instances, ids):
                instance.id = verbose_id
                checked_instances.append(instance)
        return checked_instances

    def add_with_verbose(self, instance):
        instance = self._set_verbose(instance)
        return self.add(instance)

    def add_all_with_verbose(self, instances):
        instances = self._set_verbose_all(instances)
        return self.add_all(instances)

    def add_next_with_verbose(self, instance, related_id_field):
        instance_class = instance.__class__
        new_suffix = 0
        related_id_value = getattr(instance, related_id_field)
        if self.query(
            self.query(instance_class)
            .filter(instance_class.__dict__[related_id_field] == related_id_value)
            .exists(),
        ).scalar():
            last_obj = (
                self.query(instance_class)
                .order_by(
                    instance_class.id.desc(),
                )
                .first()
            )
            _instance_id, suffix = last_obj.id.rsplit("-", 1)
            new_suffix = int(suffix) + 1
        else:
            id_body = related_id_value.split("-", 1)[-1]
            _instance_id = f"{instance_class.PREFIX}-{id_body}"

        instance.id = "{0}-{1}".format(_instance_id, "{0:03d}".format(new_suffix))
        return self.add(instance)

    def add_all_with_next_verbose(self, instances, related_id_field):
        first_item = instances[0]
        instance_class = first_item.__class__
        new_suffix = 0
        related_id_value = getattr(first_item, related_id_field)

        if self.query(
            self.query(instance_class)
            .filter(instance_class.__dict__[related_id_field] == related_id_value)
            .exists(),
        ).scalar():
            last_obj = (
                self.query(instance_class)
                .order_by(
                    instance_class.id.desc(),
                )
                .first()
            )
            _instance_id, suffix = last_obj.id.rsplit("-", 1)
            new_suffix = int(suffix) + 1
        else:
            id_body = related_id_value.split("-", 1)[-1]
            _instance_id = f"{instance_class.PREFIX}-{id_body}"

        for instance in instances:
            instance.id = "{0}-{1}".format(_instance_id, "{0:03d}".format(new_suffix))
            new_suffix += 1

        return self.add_all(instances)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, class_=VerboseBaseSession)
Model = declarative_base()


def get_engine(config: dict = Depends(get_config)):
    global _ENGINE
    if not _ENGINE:
        _ENGINE = create_engine(
            config.get("DATABASE_URL", os.getenv("DATABASE_URL")),
            pool_pre_ping=True,
            pool_recycle=300,
        )

    return _ENGINE


def get_db(engine: Engine = Depends(get_engine)):
    db: VerboseBaseSession = SessionLocal(bind=engine)
    try:
        yield db
    finally:
        db.close()


def create_db(config: dict = Depends(get_config)):
    engine = get_engine(config)
    Model.metadata.create_all(bind=engine)
    return engine


@contextmanager
def get_db_ctx_manager(config):
    engine: Engine = get_engine(config)
    db: VerboseBaseSession = SessionLocal(bind=engine)
    try:
        yield db
    finally:
        db.close()
