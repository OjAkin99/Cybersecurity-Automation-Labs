# A dictionary to track how many times each IP address fails to log in
failed_attempts = {}

# Open and read the security log file line by line
with open("security_log.txt", "r") as file:
    for line in file:
        # Check if the log line indicates a FAILED login attempt
        if "FAILED" in line:
            # Extract the IP address from the end of the string line
            parts = line.split("IP: ")
            if len(parts) > 1:
                # FIX: Added [1] to pull the second part of the split list
                ip_address = parts[1].strip()
                
                # Add 1 to the failure count for this specific IP address
                failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1

# Review the data and sound the alert for suspicious behavior
print("--- [ SOC ALERT GENERATOR ] ---")
for ip, count in failed_attempts.items():
    if count > 3:
        print(f"🚨 ALERT: Potential Brute-Force Attack Detected!")
        print(f"👉 Malicious IP: {ip} generated {count} failed login attempts.")
