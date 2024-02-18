import jwt

from connect_extension_utils.api.errors import Http404


def get_user_data_from_auth_token(token):
    '''
    Helper function to fill the Events fields of ceartian object, base on
    the token that be access through `request.headers['connect-auth']` f.e.:
    ```
    created.by.id
    created.by.name
    ```
        :param str token:
        :return: Python dict containing id and name of user making the request
        :rtype: dict[str, str]
    '''
    payload = jwt.decode(token, options={"verify_signature": False})
    return {
        'id': payload['u']['oid'],
        'name': payload['u']['name'],
    }


def get_object_or_404(db, model, filters, object_id):
    '''
    Wrapper to use `Http404`response error class within a WebApplication
    view handler function.

        :param sqlalchemy.ormSession db:
        :param connect_extension_utils.db.models.Model model:
        :param tuple[bool] filters:
        :param str object_id:
        :return: A db model instance or a HTTP 404 error.
        :rtype: Union[Type[connect_extension_utils.db.models.Model], Http404]
    '''
    obj = db.query(model).filter(*filters).one_or_none()
    if not obj:
        raise Http404(obj_id=object_id)
    return obj
