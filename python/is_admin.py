# =============================================================
# Author: http://aleskrejci.cz
# Version: 15.07.2016
# =============================================================

import os
import ctypes


def script_admin():
	try:
		is_admin = os.getuid() == 0
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	if not is_admin:
		raise Exception('Script must be run as root.')
