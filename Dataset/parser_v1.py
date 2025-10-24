import re
import csv
import pandas as pd

# Ordered feature list for output (no "raw")
columns = [
    "process_id",
    "application_number",
    "request_sequence",
    "src_ip",
    "num_vars",
    "vars_size_bytes",
    "timestamp",
    "method",
    "path",
    "response_size_bytes",
    "processing_time_ms",
    "http_version",
    "status",
    "num_headers",
    "headers_size_bytes",
    "core_switches",
    "core_number"
]

# Regex for your log line
pattern = re.compile(
    r"\[pid: (\d+)\|app: (\d+)\|req: ([^\]]+)\] ([\d\.]+) \(\) \{(\d+) vars in (\d+) bytes\} \[([^\]]+)\] (\w+) ([^\s]+) => generated (\d+) bytes in (\d+) msecs \(HTTP/([\d\.]+) (\d+)\) (\d+) headers in (\d+) bytes \((\d+) switches on core (\d+)\)"
)

input_file = "keystone_features.csv"
output_file = "keystone_features_parsed_struct.csv"

df = pd.read_csv(input_file)

with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(columns)
    for raw in df["raw"]:
        values = {col: "" for col in columns}
        match = pattern.search(raw)
        if match:
            (
                values["process_id"],
                values["application_number"],
                values["request_sequence"],
                values["src_ip"],
                values["num_vars"],
                values["vars_size_bytes"],
                values["timestamp"],
                values["method"],
                values["path"],
                values["response_size_bytes"],
                values["processing_time_ms"],
                values["http_version"],
                values["status"],
                values["num_headers"],
                values["headers_size_bytes"],
                values["core_switches"],
                values["core_number"]
            ) = match.groups()
        writer.writerow([values[col] for col in columns])

print(f"Done! Output saved as {output_file}")
