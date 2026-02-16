****Educational and authorized security testing use only.

🚀 Features

High-speed AsyncIO concurrent scanning
TCP port detection
Basic banner grabbing
Service name mapping
Screenshot-friendly terminal output
CSV + JSON report export
Flask web dashboard UI
Input validation & safe defaults
Unit tests for core logic
Clean modular architecture

🧠 Tech Stack
Python 3.10+
asyncio sockets
Flask
unittest
CSV / JSON reporting


📁 Project Structure

async-port-scanner/
│
│──  async_scanner.py      # Core async scanner engine
│──  dashboard.py          # Flask web dashboard
│──  test_scanner.py       # Unit tests
│──  requirements.txt
│
└──templates/
    └── index.html        # Dashboard UI



    
Project strcuture proper Overview 👉 <img width="385" height="314" alt="image" src="https://github.com/user-attachments/assets/c1b1d385-f662-493c-92bb-b8c339b2b6f7" />


⚙️ Installation
git clone https://github.com/rajshevde-01/Async-Ultra-Fast-Port-Scanner-Web-Dashboard.git

cd async-port-scanner
pip install -r requirements.txt

▶️ CLI Usage
Scan localhost (default)
python async_scanner.py


Scan a target with custom range
python async_scanner.py scanme.nmap.org -s 1 -e 2000


Quiet mode (no progress prints)
python async_scanner.py example.com -e 5000 --quiet

📊 Output

Terminal table:

OPEN PORT TABLE
----------------------------------------------------------------------
PORT    SERVICE        BANNER
22      SSH            OpenSSH_8.2p1 Ubuntu
80      HTTP           Apache/2.4.41
443     HTTPS          nginx



Reports generated:

async_results.json
async_results.csv


🌐 Web Dashboard

Run:
python dashboard.py


Open in browser:
http://127.0.0.1:5000


Dashboard supports:
Target input
Port range selection
Sorted results table
Error handling
Dark security-themed UI


🧪 Unit Tests

Run tests:
python test_scanner.py


Coverage includes:
Service map validation
Host resolution
Argument parser behavior
Small-range async scan execution


🔒 Safety & Ethics
This tool is intended for:
Learning network security
Lab environments
Authorized penetration testing
Defensive security research

**Do not scan networks or systems without explicit permission.


📈 Skills Demonstrated
Async network programming
Concurrent socket operations
Network reconnaissance fundamentals
Security tool engineering
Input validation & error handling
Test-driven components
Flask UI integration
Structured reporting


🛣️ Roadmap (Future Enhancements)
UDP scanning module
OS fingerprint heuristics
MITRE ATT&CK service mapping
Rate control profiles
Docker containerization
CI test pipeline
Historical scan database
Authentication on dashboard


👤 Author

Raj Shevde
Cybersecurity Enthusiast — Blue Team | SOC | Threat Detection

## GitHub: https://github.com/raj-shevde

## LinkedIn: https://linkedin.com/in/rajshevde









    

