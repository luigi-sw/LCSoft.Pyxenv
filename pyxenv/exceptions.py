'''Custom exceptions for pyxenv.'''

class pyxenvError(Exception):
    '''Base exception for pyxenv errors.'''
    pass

class PythonNotFoundError(pyxenvError):
    '''Raised when Python version is not found.'''
    pass

class DownloadError(pyxenvError):
    '''Raised when download fails.'''
    pass

class InstallationError(pyxenvError):
    '''Raised when installation fails.'''
    pass

class VenvError(pyxenvError):
    '''Raised when virtual environment operation fails.'''
    pass
