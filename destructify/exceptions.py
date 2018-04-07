class DestructifyError(Exception):
    pass


class DefinitionError(DestructifyError):
    pass


class ImpossibleToCalculateLengthError(DefinitionError):
    pass


class ParseError(DestructifyError):
    pass


class StreamExhaustedError(ParseError):
    pass


class UnknownDependentFieldError(ParseError):
    pass

