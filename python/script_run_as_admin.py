# =============================================================
# Author: http://sefikail.cz
# License: http://creativecommons.org/licenses/by/3.0/
# Source code: https://github.com/sefikail/scriptus
# Version: Version: 15.07.2016
# =============================================================

import ctypes
import os


def script_run_as_admin():
	try:
		admin = os.getuid() == 0
	except AttributeError:
		admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	if not admin:
		return False
	return True


if not script_run_as_admin():
	raise Exception('Script must be run as root.')
