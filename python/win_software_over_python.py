# =============================================================
# Author: http://aleskrejci.cz
# Version: 15.07.2016
# =============================================================

import errno
import json
import platform
import winreg


def is_64bit():
	if platform.machine().endswith('64'):
		return True
	return False


arch_keys = {winreg.KEY_WOW64_32KEY: '32bit'}
if is_64bit():
	arch_keys = {winreg.KEY_WOW64_32KEY: '32bit', winreg.KEY_WOW64_64KEY: '64bit'}

software_in_registers = []
for arch_key, arch_value in arch_keys.items():
	reg_key_path = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | arch_key)
	for i in range(0, winreg.QueryInfoKey(reg_key_path)[0]):
		reg_sub_key = winreg.OpenKey(reg_key_path, winreg.EnumKey(reg_key_path, i))
		soft_dict = {}
		for reg_name in ['DisplayName', 'DisplayVersion', 'Publisher', 'UninstallString', 'InstallDate']:
			soft_dict.setdefault(reg_name, '')
			try:
				reg_data, reg_type = winreg.QueryValueEx(reg_sub_key, reg_name)
				soft_dict[reg_name] = reg_data
			except OSError as e:
				if e.errno == errno.ENOENT:  # Key doesn't exist
					pass
		soft_dict['Architecture'] = arch_value
		reg_sub_key.Close()
		software_in_registers.append(soft_dict)

try:
	if software_in_registers:
		print(json.dumps(software_in_registers, sort_keys=True))

except Exception as e:
	print(e)
