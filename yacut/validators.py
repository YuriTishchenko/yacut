import re

from .constants import EMPTY_PATTERN, PATTERN_CUSTOM_ID, URL_REGEX


def empty_id(id):
    return True if re.match(EMPTY_PATTERN, id) else False

def is_url(link):
    return True if re.match(URL_REGEX, link) else False

def check_id(id):
    return True if re.match(PATTERN_CUSTOM_ID, id) else False
 