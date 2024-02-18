class AuthorizationError(Exception):
    def __init__(self, detail: str) -> None:
        self.detail = detail


class UnauthorizedError(AuthorizationError):
    def __init__(self, detail: str = 'Unauthorized. Please authenticate and/or obtain the necessary permissions.') -> None:
        super().__init__(detail)
