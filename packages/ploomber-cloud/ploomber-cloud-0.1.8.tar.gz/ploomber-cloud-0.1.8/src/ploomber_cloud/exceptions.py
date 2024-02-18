from click import ClickException


class BasePloomberCloudException(ClickException):
    """Base exception for all Ploomber Cloud exceptions"""

    def __init__(self, message):
        super().__init__(message)
        # this attribute will allow the @modify_exceptions decorator to add the
        # community link
        self.modify_exception = True


class InvalidPloomberConfigException(BasePloomberCloudException):
    """Exception for invalid ploomber-config.json"""

    pass
