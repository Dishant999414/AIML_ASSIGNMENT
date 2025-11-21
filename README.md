task 3 = Mini Project Proposal: Using AI Agents to Improve SIEM Threat Detection and Automate SOC Response

Security Operation Centers (SOC) deal with huge amounts of logs and alerts every day. Most alerts are repetitive, noisy, or not 
actually dangerous. Because of this, security teams waste time on false positives and miss real threats. My project idea is to use 
an AI Agent that works with a SIEM system to make detection smarter and automate the basic responses. The goal is to reduce manual 
work and help analysts focus on real attacks.

1. How the AI Agent Helps SIEM Detection ;

The AI agent will continuously learn from log patterns, past incidents, analyst feedback, and the environment. It will apply the 
standard 20 SIEM rules such as:

Login failures
Successful logins from new locations
Privilege escalation
New admin account creation
Multiple password resets
File integrity changes
Suspicious process execution
Network scanning behaviour
Large outbound data transfers
Malware signature detection
Disabled antivirus
USB device insertion
Firewall rule change
Unauthorized port activity
VPN login anomalies
Brute-force attempts
RDP connection attempts
Database query spikes
Configuration changes
Multiple alerts from same host

2. How the AI Agent Automates SOC Responses ;

Once the agent is confident that a threat is real, it can start automated actions. For example:

If there are too many login failures → temporarily lock the user account.
If a server shows file integrity changes → isolate that server from the network.
If large outbound data is detected → block the connection and alert the SOC.
If malware behavior is detected → trigger antivirus scan and quarantine.

These actions save SOC analysts from doing basic steps manually. Analysts can still override, approve, or adjust these automated 
actions, so the control stays with the human team.

3. Benefits for a SOC Team ;

Fewer false alerts: The agent reduces noise by analyzing context before escalating.
Faster response: Immediate action prevents attacks from spreading.
Better detection: Using patterns + SIEM rules increases accuracy.
Less workload: Analysts can focus on investigation and reporting instead of routine tasks.

4. Final Outcome ;

This mini-project will provide a working demo where a SIEM generates alerts based on its 20 rules, and an AI Agent classifies 
the alert as High, Medium, or Low risk. The agent will then show the recommended automated action. This is a practical, realistic
 project that adds value to any SOC environment and proves how AI can support modern cyber security.
