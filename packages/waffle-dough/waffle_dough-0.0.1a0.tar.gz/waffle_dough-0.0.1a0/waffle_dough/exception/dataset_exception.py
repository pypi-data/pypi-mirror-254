from .base_exception import BaseException


class DatasetException(BaseException):
    """Exception raised for errors in the dataset."""


class DatasetTaskError(DatasetException):
    """Exception raised for errors in the dataset task."""


class DatasetNotFoundError(DatasetException):
    """Exception raised for errors trying to load a dataset that does not exists."""


class DatasetAlreadyExistsError(DatasetException):
    """Exception raised for errors trying to create a dataset that already exists."""


class DatasetCRUDError(DatasetException):
    """Exception raised for errors trying to export a dataset."""


class DatasetImportError(DatasetException):
    """Exception raised for errors trying to import a dataset."""


class DatasetAdapterError(DatasetException):
    """Exception raised for errors in the dataset adapter."""


class DatasetAdapterTaskError(DatasetAdapterError):
    """Exception raised for errors in the dataset adapter task."""


class DatasetAdapterImportError(DatasetAdapterError):
    """Exception raised for errors in the dataset adapter task."""


class DatasetAdapterExportError(DatasetAdapterError):
    """Exception raised for errors in the dataset adapter task."""


class DatasetAdapterAlreadyExistsError(DatasetAdapterError):
    """Exception raised for errors in the dataset adapter task."""


class DatasetAdapterNotFoundError(DatasetAdapterError):
    """Exception raised for errors in the dataset adapter task."""


class DatasetEmptyError(DatasetAdapterError):
    """Exception raised for errors in the dataset adapter task."""


class DatasetSplitError(DatasetAdapterError):
    """Exception raised for errors in the dataset adapter task."""
