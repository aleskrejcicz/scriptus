# =============================================================
# Author: http://sefikail.cz
# License: http://creativecommons.org/licenses/by/3.0/
# Source code: https://github.com/sefikail/scriptus
# Version: Version: 15.07.2016
# =============================================================

import re
import subprocess


# wmic product get Name, Version /format:list
arg_param = ['Name', 'Version']


def extract_data(arg_list, sep='='):
	dict_data = {}
	for arg in arg_list:
		split_array = arg.split(sep)
		if len(split_array) >= 2:
			dict_data[split_array[0]] = sep.join(split_array[1:])
	return dict_data


cmd = 'wmic product get ' + ','.join(arg_param) + ' /format:list'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
output = proc.stdout.read().decode(u'utf8')  # Dekodovani z bytove formy

param_array = []
for line in re.split('\n\s*\n', output.strip()):
	arg_list = re.split('[~\r\n]+', line.strip())
	param_array.append(extract_data(arg_list))

print(param_array)

# Spostu toho nevypise!