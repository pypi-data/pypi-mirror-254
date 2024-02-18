import datetime as DT

MAJOR_VERSION = 0
'''Major version number'''

MINOR_VERSION = 6
'''Minor version number'''

REVISION_VERSION = 3
'''Revision version number'''

VERSION = (MAJOR_VERSION,MINOR_VERSION,REVISION_VERSION)
'''DAPI2 library DAPI2 version (3-tuple)'''

__version__ = '{0:d}.{1:d}.{2:d}'.format(*VERSION)
'''DAPI2 library DAPI2 version (str)'''

__ver__ = '{0:d}.{1:d}'.format(*VERSION)
'''DAPI2 library DAPI2 short version (str)'''

DATE = DT.date(2024, 1, 28)
'''Release date'''

__date__ = DATE.isoformat()
'''Release date string in ISO format'''

REQUIRED_PYTHON = (3,8)
'''The required Python verison'''