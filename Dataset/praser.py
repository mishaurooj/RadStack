import re
import csv
import pandas as pd
from datetime import datetime

# Helper to derive endpoint_class from path
def endpoint_class(path):
    if path.startswith('/v3/auth/tokens'):
        return 'auth'
    elif '/users' in path:
        return 'user_mgmt'
    elif '/projects' in path:
        return 'project_mgmt'
    elif '/roles' in path:
        return 'role_mgmt'
    else:
        return 'other'

# Helper to get weekday from timestamp string
def get_wday(dtstr):
    try:
        dt = datetime.strptime(dtstr, "%a %b %d %H:%M:%S %Y")
        return dt.weekday()
    except:
        return ""

# Helper to get hour from timestamp string
def get_hour(dtstr):
    try:
        dt = datetime.strptime(dtstr, "%a %b %d %H:%M:%S %Y")
        return dt.hour
    except:
        return ""

# Helper for success
def get_success(status):
    try:
        code = int(status)
        return 1 if 200 <= code < 300 else 0
    except:
        return 0

# Regex for parsing the log line
pattern = re.compile(
    r"\[pid: (\d+)\|app: (\d+)\|req: ([^\]]+)\] ([\d\.]+) \(\) \{(\d+) vars in (\d+) bytes\} \[([^\]]+)\] (\w+) ([^\s]+) => generated (\d+) bytes in (\d+) msecs \(HTTP/([\d\.]+) (\d+)\) (\d+) headers in (\d+) bytes \((\d+) switches on core (\d+)\)"
)

# Feature order for output
columns = [
    "timestamp",
    "user_id",
    "project_id",
    "src_ip",
    "method",
    "path",
    "endpoint_class",
    "status",
    "success",
    "hour",
    "wday",
    "freq15_user",
    "source",
    "raw"
]

input_file = "keystone_features.csv"
output_file = "keystone_features_parsed.csv"

df = pd.read_csv(input_file)

with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(columns)
    for raw in df["raw"]:
        # Default values
        values = {
            "timestamp": "",
            "user_id": "",
            "project_id": "",
            "src_ip": "",
            "method": "",
            "path": "",
            "endpoint_class": "",
            "status": "",
            "success": "",
            "hour": "",
            "wday": "",
            "freq15_user": "",
            "source": "text",
            "raw": raw
        }
        match = pattern.search(raw)
        if match:
            # Parse timestamp
            values["timestamp"] = match.group(7)
            # src_ip
            values["src_ip"] = match.group(4)
            # method
            values["method"] = match.group(8)
            # path
            values["path"] = match.group(9)
            # endpoint_class
            values["endpoint_class"] = endpoint_class(values["path"])
            # status
            values["status"] = match.group(13)
            # success
            values["success"] = get_success(values["status"])
            # hour
            values["hour"] = get_hour(values["timestamp"])
            # wday
            values["wday"] = get_wday(values["timestamp"])
        # freq15_user: leave as ""
        # user_id, project_id: leave as ""
        row = [values[col] for col in columns]
        writer.writerow(row)

print("Done! Output saved as", output_file)
