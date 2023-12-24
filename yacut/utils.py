import random
import string

from .constants import RANDOM_LENGTH
from .models import URLMap


def get_unique_short_id():
    unique_str = get_random_str()
    while URLMap.query.filter_by(short=unique_str).first() is not None:
        unique_str = get_random_str()
    return unique_str


def get_random_str():
    input_range = string.ascii_letters + string.digits
    random_str = ''.join(random.sample(input_range, RANDOM_LENGTH))
    return random_str
