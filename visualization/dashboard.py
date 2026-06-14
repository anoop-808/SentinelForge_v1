import json
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load events
with open("../scripts/security_events.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Create output directory
Path("charts").mkdir(exist_ok=True)

# -------------------------
# Severity Distribution
# -------------------------
severity_counts = df["severity"].value_counts()

plt.figure(figsize=(8,5))
severity_counts.plot(kind="bar")
plt.title("Security Event Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/severity_distribution.png")
plt.close()

# -------------------------
# Event Categories
# -------------------------
event_types = []

for event in df["event"]:
    if "Login success" in event:
        event_types.append("Login Success")
    elif "Failed" in event or "authentication failure" in event:
        event_types.append("Failed Login")
    elif "Sudo Activity" in event:
        event_types.append("Sudo Activity")
    elif "Cron Activity" in event:
        event_types.append("Cron Activity")
    else:
        event_types.append("Other")

df["event_type"] = event_types

event_counts = df["event_type"].value_counts()

plt.figure(figsize=(8,5))
event_counts.plot(kind="bar")
plt.title("Security Events by Category")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/event_categories.png")
plt.close()

# -------------------------
# Pie Chart
# -------------------------
plt.figure(figsize=(8,8))
event_counts.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Security Event Breakdown")
plt.tight_layout()
plt.savefig("charts/event_breakdown_pie.png")
plt.close()

print("Dashboard charts generated successfully.")
