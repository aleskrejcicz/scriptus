# =============================================================
# Author: http://sefikail.cz
# License: http://creativecommons.org/licenses/by/3.0/
# Source code: https://github.com/sefikail/scriptus
# Version: Version: 15.07.2016
# =============================================================

import errno
import sys
import json
import platform


if platform.python_version()[0] == "2":
	reload(sys)
	sys.setdefaultencoding("utf-8")

try:
	import _winreg as winreg  # Try importing on Python 2
except ImportError:
	import winreg  # Fallback to Python 3 (if this raises an Exception, it'll escalate)


def is_64bit():
	if platform.machine().endswith('64'):
		return True
	return False


def script_admin():
	import ctypes, os
	try:
		is_admin = os.getuid() == 0
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	if not is_admin:
		raise Exception('Script must be run as root.')


# ================================================


arch_keys = {winreg.KEY_WOW64_32KEY: '32bit'}
if is_64bit():
	arch_keys = {winreg.KEY_WOW64_32KEY: '32bit', winreg.KEY_WOW64_64KEY: '64bit'}

softwarelist_in_registers = []
for arch_key, arch_value in arch_keys.items():
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | arch_key)
	for i in range(0, winreg.QueryInfoKey(key)[0]):
		skey_name = winreg.EnumKey(key, i)
		skey = winreg.OpenKey(key, skey_name)

		soft_sub = {}
		for value in ['DisplayName', 'DisplayVersion', 'Publisher', 'UninstallString', 'InstallDate']:
			soft_sub.setdefault(value, '')
			try:
				reg_data, reg_type = winreg.QueryValueEx(skey, value)
				soft_sub[value] = reg_data
			except OSError as e:
				if e.errno == errno.ENOENT:  # Key doesn't exist
					pass
		skey.Close()
		soft_sub['Architecture'] = arch_value
		softwarelist_in_registers.append(soft_sub)

try:
	if softwarelist_in_registers:
		print(json.dumps(softwarelist_in_registers, sort_keys=True))

except Exception as e:
	print(e)
