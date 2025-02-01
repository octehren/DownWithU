import random

# These are all copyright-free!
VALID_VIDEO_URLS = frozenset([
    'https://www.youtube.com/watch?v=DKsj5mCR7qs', # Chollima on the Wing
    'https://www.youtube.com/watch?v=mJmjljQP3oY', # I Love Beijing Tiananmen
    'https://www.youtube.com/watch?v=rnbX7VUvxGU', # Linux Startup Sound
])

INVALID_VIDEO_URLS = frozenset([
    'this is invalid!', # not an URL
    'https://youtube.com/watch?v=thisisaninvalidvideolol', # Broken URL
    'https://google.com', # Not a supported URL
])

def get_random_valid_video_url() -> str:
    return random.choice(list(VALID_VIDEO_URLS))

def get_random_invalid_video_url() -> str:
    return random.choice(list(INVALID_VIDEO_URLS))