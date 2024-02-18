from typing import Any, Dict, Union

from fastapi import status

from connect.client import ClientError


'''
Error utilities for EaaS extensions.

By default eass runner injects the `connect.eaas.core.utils.client_error_exception_handler`
function to the FastAPI app initialization as exception handler.
This function catch all errors raised in the context of the WebApplication that are
an instance of the `connecet.client.ClientError` class and coerce them into JSON format
(`fastapi.responses.JSONResponse`) if the error instance has the attribute `error_code` setted.

`connect_extension_utils.api.errors` is a wrapper around this behaviour that facilitates the use of
prefixed error responses.
'''


class Error:
    STATUS_CODE = status.HTTP_400_BAD_REQUEST

    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __call__(self, **kwds: Dict[str, Any]) -> ClientError:
        format_kwargs = kwds.get('format_kwargs', {})

        message = self.message.format(**format_kwargs)
        errors = kwds.get('errors')

        if not errors:
            errors = [message or 'Unexpected error.']
        if not isinstance(errors, list):
            errors = [errors]

        return ClientError(
            message=message,
            status_code=self.STATUS_CODE,
            error_code=self.error_code,
            errors=errors,
        )


class ExtensionErrorMeta(type):
    PREFIX = 'EXT'
    ERRORS = {}

    def __getattr__(cls, __name: str) -> Union[Error, AttributeError]:
        valid_dict = {cls.PREFIX: cls.ERRORS}
        try:
            prefix, code = __name.split('_')
            error = valid_dict[prefix][int(code)]
        except (KeyError, ValueError):
            raise AttributeError(f"type object '{cls.__name__}' has no attribute '{__name}'")
        return Error(message=error, error_code=__name)


class ExtensionErrorBase(metaclass=ExtensionErrorMeta):
    '''
    Base Error class to group a set of validation (`fastapi.status.HTTP_400_BAD_REQUEST`)
    errors base on a prefix. By default the `PREFIX` value is `EXT`, but it can be overwritten.
    Also a list of `errors` can be provided.

    Usage:

    ```
    # Define a custom error class
    class MyError(ExtensionErrorBase)
        PREFIX = "EXT"
        ERRORS = {
            1: "Some error",
            2: "Some {template} error.",
            3: "Not found",

        }

    # raise the error
    raise MyError.EXT_001()
    raise MyError.EXT_002(format_kwargs={"template": "foo"})
    ```
    '''


class Http404(ClientError):
    def __init__(self, obj_id, **kwargs):
        message = "Object `{obj_id}` not found.".format(obj_id=obj_id)
        status_code = status.HTTP_404_NOT_FOUND
        error_code = 'NFND_000'
        errors = [message]
        super().__init__(message, status_code, error_code, errors, **kwargs)
