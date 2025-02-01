from django.core.exceptions import ImproperlyConfigured

import logging
logger = logging.getLogger('django')

try:
    from .environment import *
except ImproperlyConfigured as icf:
    print(f"improperly configured: {icf}")
    exit(-1)
except Exception:
    print("Environment variables problem. Please contact wih developer.")
    exit(-1)

from .common import *
from .database import *
