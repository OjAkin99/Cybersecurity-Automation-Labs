import socket

# STEP 1: Setup target profile
target_host = "localhost"
ports_to_scan = [21, 22, 80, 443]

try:
    target_ip = socket.gethostbyname(target_host)
    print("--- [ MONITOR: SCANNING AND GENERATING HTML REPORT ] ---")
    
    # 1. Initialize a new local file called report.html in write mode ("w")
    with open("report.html", "w") as html_file:
        
        # 2. Write the standard HTML layout structure and baseline style designs
        html_file.write("<!DOCTYPE html>\n<html>\n<head>\n")
        html_file.write("<title>Cybersecurity Port Scan Dashboard</title>\n")
        
        # Add basic CSS styling right inside the code to make it look clean
        html_file.write("<style>\n")
        html_file.write("body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; color: #333; }\n")
        html_file.write("h1 { color: #1a365d; border-bottom: 2px solid #1a365d; padding-bottom: 10px; }\n")
        html_file.write("table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }\n")
        html_file.write("th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }\n")
        html_file.write("th { background-color: #1a365d; color: white; }\n")
        html_file.write(".open { color: white; background-color: #e53e3e; padding: 4px 8px; border-radius: 4px; font-weight: bold; }\n")
        html_file.write(".closed { color: white; background-color: #38a169; padding: 4px 8px; border-radius: 4px; }\n")
        html_file.write("</style>\n</head>\n<body>\n")
        
        # 3. Write the Dashboard Headers into the file structure
        html_file.write(f"<h1>🚀 Cybersecurity Automated Port Scan Dashboard</h1>\n")
        html_file.write(f"<p><strong>Target Host Checked:</strong> {target_host} ({target_ip})</p>\n")
        html_file.write("<table>\n<tr><th>Port Number</th><th>Service Profile</th><th>Security Status</th></tr>\n")
        
        # Mapping common ports to names so the dashboard reads clearly
        port_services = {21: "FTP (File Transfer)", 22: "SSH (Secure Shell)", 80: "HTTP (Web Traffic)", 443: "HTTPS (Secure Web)"}

        # STEP 3: Begin looping through our target numbers (From Step 3)
        for port in ports_to_scan:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            result = s.connect_ex((target_ip, port))
            service_name = port_services.get(port, "Unknown Service")
            
            # 4. Dynamically write HTML table data tracks based on connection results
            if result == 0:
                # If port is open, write a red alert badge line into the table matrix
                html_file.write(f"<tr><td>{port}</td><td>{service_name}</td><td><span class='open'>🚨 OPEN (Vulnerable)</span></td></tr>\n")
            else:
                # If port is closed, write a clean green secure badge line into the table matrix
                html_file.write(f"<tr><td>{port}</td><td>{service_name}</td><td><span class='closed'>✅ SECURE (Closed)</span></td></tr>\n")
                
            s.close()
            
        # 5. Seal off our HTML file tags neatly
        html_file.write("</table>\n</body>\n</html>\n")
        
    print("✅ SUCCESS: Security audit complete! 'report.html' file has been updated.")

except Exception as e:
    print(f"🚨 ERROR: Dashboard file creation failed. Details: {e}")
