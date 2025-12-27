# APT29 (Cozy Bear / NOBELIUM)

## Notable Attacks

**SolarWinds Supply Chain Compromise (2020), Dark Halo Operations**
- **Targets:** US Government, Fortune 500, SaaS providers
- **Impact:** Long-term espionage via trusted software updates

## Emulation & Detection Strategy

We utilize **Atomic Red Team** to emulate the TTPs associated with the APT29 SolarWinds Supply Chain compromise (2020). While not an exact 1-to-1 replication, this simulation leverages the MITRE ATT&CK framework to model specific adversary behaviors.

Each TTP listed below corresponds to a specific detection rule available in this directory. These detections are managed and deployed using Detection-as-Code (DaC) practices via GitHub Actions.

## ATT&CK Techniques Used

| Phase | Technique |
| :--- | :--- |
| Initial Access | T1195 – Supply Chain Compromise |
| Initial Access | T1566.002 – Phishing Links |
| Execution | T1059.001 – PowerShell |
| Defense Evasion | T1027 – Obfuscated Files or Information |
| Credential Access | T1555.003 – Browser Credentials |
| Discovery | T1082 – System Information Discovery (Hostname) <br> T1016 – System Network Configuration Discovery (Windows) |
| Lateral Movement | T1570 – Lateral Tool Transfer |
| Persistence | T1098 – Account Manipulation |
| Defense Evasion | T1027 – Obfuscation via PowerShell |
| Command and Control | T1071.001 – Web Protocols |
| Exfiltration | T1041 – Exfiltration over C2 channel |
