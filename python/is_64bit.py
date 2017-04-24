# =============================================================
# Author: http://aleskrejci.cz
# Version: 15.07.2016
# =============================================================

import platform


def is_64bit():
	if platform.machine().endswith('64'):
		return True
	return False
