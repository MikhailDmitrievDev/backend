class ErrorSymbolsException(Exception):

    def __init__(self, message: str = "Error symbol exception."):
        self.message = message
