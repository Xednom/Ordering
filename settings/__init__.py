from settings.base import *

from settings.production import *

try:
   from settings.local import *
except:
   pass
