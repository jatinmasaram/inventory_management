class ProductNotFoundException(Exception):
    pass


class CustomerNotFoundException(Exception):
    pass


class OrderNotFoundException(Exception):
    pass


class DuplicateSKUException(Exception):
    pass


class DuplicateEmailException(Exception):
    pass


class InsufficientStockException(Exception):
    pass

class UnauthorizedException(
    Exception
):
    pass