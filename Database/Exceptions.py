class _Exceptions(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# exceptions classes, you can print the exception using print(exception)
class DatabaseException(_Exceptions):
    class ConnectionInvalid(_Exceptions):
        pass

    class NOT_NULL_VIOLATION(_Exceptions):
        pass

    class FOREIGN_KEY_VIOLATION(_Exceptions):
        pass

    class UNIQUE_VIOLATION(_Exceptions):
        pass

    class CHECK_VIOLATION(_Exceptions):
        pass

    class database_ini_ERROR(_Exceptions):
        pass

    class UNKNOWN_ERROR(_Exceptions):
        pass
