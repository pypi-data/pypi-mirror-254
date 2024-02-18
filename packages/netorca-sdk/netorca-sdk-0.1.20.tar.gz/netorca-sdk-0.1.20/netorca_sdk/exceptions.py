class NetorcaException(Exception):
    pass


class NetOrcaWrongYAMLFormat(NetorcaException):
    pass


class NetorcaBaseException(Exception):
    def __init__(self, message):
        self.message = message
        print(f"Netorca Exception: {message}")


class NetorcaValueError(NetorcaBaseException):
    pass


class NetorcaNotFoundError(NetorcaBaseException):
    pass


class NetorcaPermissionError(NetorcaBaseException):
    pass


class NetorcaTimeoutError(NetorcaBaseException):
    pass


class NetorcaAPIError(NetorcaBaseException):
    pass


class NetorcaAuthenticationError(NetorcaAPIError):
    pass


class NetorcaServerUnavailableError(NetorcaAPIError):
    pass


class NetorcaGatewayError(NetorcaAPIError):
    pass


class NetorcaInvalidContextError(NetorcaAPIError):
    pass
