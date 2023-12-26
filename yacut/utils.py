import random
import string

from .constants import RANDOM_LENGTH
from .models import URLMap


def get_unique_short_id():
    unique_str = get_random_str()
    i = 0
    while i < 10 or URLMap.query.filter_by(short=unique_str).scalar():
        unique_str = get_random_str()
        i += 1
    return unique_str


def get_random_str():
    input_range = string.ascii_letters + string.digits
    random_str = ''.join(random.sample(input_range, RANDOM_LENGTH))
    return random_str
