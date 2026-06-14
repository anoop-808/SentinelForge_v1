import json
events = []
f = open("../output.txt")
for line in f:
	if "[ALERT]" in line:
		severity = "HIGH"
	else:
		severity = "INFO"
	event = {
	      "event": line.strip(),
	      "severity": severity
	}
	events.append(event)
f.close()

out = open("security_events.json","w")
json.dump(events,out,indent=4)
out.close()
print ("JSON export completed")
