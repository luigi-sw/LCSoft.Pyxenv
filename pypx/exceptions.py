'''Custom exceptions for pypx.'''

class PypxError(Exception):
    '''Base exception for pypx errors.'''
    pass

class PythonNotFoundError(PypxError):
    '''Raised when Python version is not found.'''
    pass

class DownloadError(PypxError):
    '''Raised when download fails.'''
    pass

class InstallationError(PypxError):
    '''Raised when installation fails.'''
    pass

class VenvError(PypxError):
    '''Raised when virtual environment operation fails.'''
    pass
