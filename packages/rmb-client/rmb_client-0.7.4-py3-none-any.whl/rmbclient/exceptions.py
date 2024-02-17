
class ResourceExists(Exception):
    pass


class ResourceNotFound(Exception):
    pass


class Unauthorized(Exception):
    pass


class ServerInternalError(Exception):
    pass


class ServerConnectionError(Exception):
    pass