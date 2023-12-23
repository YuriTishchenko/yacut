import re

from .constants import EMPTY_PATTERN, PATTERN_CUSTOM_ID, URL_REGEX


def empty_id(id):
    return re.match(EMPTY_PATTERN, id)

def is_url(link):
    return re.match(URL_REGEX, link)

def check_id(id):
    return re.match(PATTERN_CUSTOM_ID, id)
 