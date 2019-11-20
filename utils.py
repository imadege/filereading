from urllib.parse import urlparse
import re
from contextlib import suppress


def is_within_range(value, min, max):
    """
    :param value to be validated agnaist:
    :param min lower limit:
    :param max upperlimt:
    :return boolean true if the value is within min and max:
    """
    with suppress(ValueError):
        value = int(value)
        if value >= min and value <= max:
            return True
        else:
            return False


def max_length(value, length):
    """
    :param value to be checked :
    :param length maximum length allowed:
    :return boolean true if value is with range:
    """
    if len(value) <= length:
        return True
    else:
        return False


def is_url(value):
    if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', value):
        return True
    else:
        return False
