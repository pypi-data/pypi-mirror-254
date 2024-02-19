class FaluError(Exception):
    def __init__(self, message=None, status_code=None, error_code=None, problem=None):
        super(FaluError, self).__init__(message)

        self.status_code = status_code
        self.error_code = error_code
        self.problem = problem
        self._message = message

    def __str__(self):
        return self._message

    def __repr__(self):
        return "{class_name} => (Message:{message}, status: {status})".format(
            class_name=self.__class__.__name__,
            message=self._message,
            status=self.status_code
        )


class ApiError(FaluError):
    pass


class AuthenticationError(FaluError):
    pass


class ApiConnectionError(FaluError):
    pass
