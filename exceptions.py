class Error(Exception):
    """ Handles custom error handling"""
    pass


class InvalidDict(Error):
    """Handles invvalid dictionary"""
    pass

class FailedToGetData(Error):
    """Handles Failed conversions of data"""
    pass