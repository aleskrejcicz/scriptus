# =============================================================
# Author: http://aleskrejci.cz
# Version: 15.07.2016
# =============================================================

import subprocess


def call_cmd(cmd):
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()
	# print('cmd', cmd)
	# print('stdout', stdout)
	# print('stderr', stderr)
	# print('===================')
	if p.returncode != 0:
		raise Exception('[ERROR] Msg ...', stdout, stderr)
	return stdout
