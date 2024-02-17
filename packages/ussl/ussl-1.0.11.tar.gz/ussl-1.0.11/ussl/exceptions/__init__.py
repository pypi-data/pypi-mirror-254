from typing import List, Union


class SOARException(Exception):
    _return_code: int = 1
    _TEMPLATE = 'Error: {args}.'

    @property
    def return_code(self):
        return self._return_code

    def __init__(self, message: Union[List[str], str, dict]):
        self.message = message
        if isinstance(self.message, List):
            self.message = self._TEMPLATE.format(args=', '.join(self.message))
        elif isinstance(self.message, str):
            self.message = self._TEMPLATE.format(args=self.message)
        else:
            self.message = self._TEMPLATE.format(args=str(self.message))
        super().__init__(self.message)


class DataError(SOARException):
    _return_code: int = 10
    _TEMPLATE = 'Data error: {args}.'


class NoInputError(DataError):
    _return_code: int = 11
    _TEMPLATE = 'Missing input data: {args}.'


class NoSecretsError(DataError):
    _return_code: int = 12
    _TEMPLATE = 'Missing secrets: {args}.'


class BadInputError(DataError):
    _return_code: int = 13
    _TEMPLATE = 'Input data validation error: {args}.'


class BadSecretsError(DataError):
    _return_code: int = 14
    _TEMPLATE = 'Secrets validation error: {args}.'


class ProtocolError(SOARException):
    _return_code: int = 20
    _TEMPLATE = 'Protocol error: {args}.'


class ConnectionFailed(ProtocolError):
    _return_code: int = 21
    _TEMPLATE = 'Connection failed: {args}.'


class CredentialsError(ProtocolError):
    _return_code: int = 22
    _TEMPLATE = 'Invalid credentials: {args}.'


class PermissionsError(ProtocolError):
    _return_code: int = 23
    _TEMPLATE = 'Missing permissions: {args}.'


class ExecutionError(ProtocolError):
    _return_code: int = 24
    _TEMPLATE = 'Command execution error: {args}.'
