# =============================================================
# Author: http://sefikail.cz
# License: http://creativecommons.org/licenses/by/3.0/
# Source code: https://github.com/sefikail/scriptus
# Version: Version: 15.07.2016
# =============================================================

import platform


def is_64bit():
	if platform.machine().endswith('64'):
		return True
	return False
