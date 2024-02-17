# -*- coding: utf-8 -*-

class ErrorType:
    ServerSideError = 'ServerSideError'
    ClientSideError = 'ClientSideError'


class Error(Exception):
    error_type = ErrorType.ClientSideError
    message = None

    def __init__(self, message: str = None, cause: str = None, detail: dict = None, error_type: str = None):
        self.message = message or self.message
        self.cause = cause
        self.detail = detail
        self.status = self.__class__.__name__
        self.error_type = error_type or self.error_type

    def __str__(self):
        return self.message


class ClientKnownError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class ValidationError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class NotFoundError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class InvalidTokenError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class ForbiddenError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class NotAvailableError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


# server error below


class ServerKnownError(Error):
    error_type = ErrorType.ServerSideError
    message = "服务侧发生了早已预料的错误"

    def __init__(self, cause: str, **kwargs):
        super().__init__(cause=cause, **kwargs)


class ServerUnknownError(Error):
    error_type = ErrorType.ServerSideError
    message = "服务侧发生了始料未及的错误"

    def __init__(self, cause: str, **kwargs):
        super().__init__(cause=cause, **kwargs)
