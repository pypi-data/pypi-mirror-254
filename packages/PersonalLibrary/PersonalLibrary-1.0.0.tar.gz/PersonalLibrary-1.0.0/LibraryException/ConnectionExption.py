from Exception.LibraryException import LibraryException
from Text.Text import Text


class ConnectionException(LibraryException):
    def __init__(self, errorMessage: str = None):
        if errorMessage is None:
            errorMessage = Text().translate("error.connection")
        super().__init__(errorMessage)
        self.error_code = self.error_code()
        self.errorMessage = errorMessage
