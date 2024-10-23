class PyexcusesError(Exception):
    "Base class for all pyexcuses exceptions"


class LanguageNotFoundError(PyexcusesError):
    pass


class CategoryNotFoundError(PyexcusesError):
    pass
