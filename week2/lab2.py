# Constants
KB = 1024
MB = 1048576
GB = 1073741824
# Inputs
num_entries = int(input("Please enter the number of entries per second: "))
entry_size = int(input("Please enter the average number of bytes per entry: "))

# Calculations
per_minute_bytes = num_entries * entry_size * 60
per_hour_bytes = per_minute_bytes * 60
per_day_bytes = per_hour_bytes * 24

# Convert to KB, MB, GB
per_minute_kb = per_minute_bytes / KB
per_hour_mb = per_hour_bytes / MB
per_day_gb = per_day_bytes / GB

# Output
print("Storage Estimates")
print(f"Per minute: {per_minute_kb} KB")
print(f"Per hour: {per_hour_mb} MB")
print(f"Per day: {per_day_gb} GB")