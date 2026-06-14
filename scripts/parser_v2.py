import subprocess
logs = subprocess.check_output(
	["journalctl","-n","100","--no-pager"],
	text = True
)

for line in logs.splitlines():
	if "sudo" in line or "CRON" in line:
		print(line)
