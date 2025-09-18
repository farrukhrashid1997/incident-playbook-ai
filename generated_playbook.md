# Generated Incident Response Playbook

**Parameters Used:**
```json
{
  "attack_type": "ransomware",
  "industry": "manufacturing",
  "severity_level": "high",
  "affected_systems": [
    "SCADA systems",
    "HMI interfaces",
    "production databases"
  ],
  "compliance_requirements": [
    "NIST",
    "IEC 62443",
    "ISO 27001"
  ],
  "additional_context": "Attack detected on OT network affecting production line controls"
}
```

**Prompt used:**

You are a cybersecurity expert specializing in incident response playbook creation. Generate a detailed incident response playbook based on the following parameters and examples.

**INCIDENT PARAMETERS:**
- Attack Type: ransomware
- Industry: manufacturing
- Severity Level: high
- Affected Systems: SCADA systems, HMI interfaces, production databases
- Compliance Requirements: NIST, IEC 62443, ISO 27001
- Additional Context: Attack detected on OT network affecting production line controls

**SIMILAR EXAMPLES FROM DATABASE:**

--- Example 1 (Similarity: 0.587) ---
Sure. Here is the information requested.
Title: : Incident Response Playbook for Ransomware Infection (NIST Compliant)
1. Preparation: : Objective: Establish contacts, define procedures, gather information to save time during an incident. 
1. Develop a ransomware incident response team: Identify key personnel who will be responsible for responding to a ransomware attack. This team should include representatives from IT, security, legal, and communications. 
2. Establish communication protocols: Define how the incident response team will communicate with each other, as well as with stakeholders and the public. 
3. Identify critical systems and data: Identify the systems and data that are critical to the organization's operations. This will help inform the response strategy and ensure that the most important systems and data are protected.
2. Detection and Analysis: : Objective: Identify the ransomware attack, assess its severity, and gather information to inform the incident response.

...

--- Example 2 (Similarity: 0.583) ---
Sure. Here is the information requested.
Title: : Ransomware Incident Response Playbook
1. Preparation: : Objective: Establish contacts, define procedures, gather information to save time during an incident.
1.1 A good knowledge of:
The usual operating systems security policies is needed.
The usual users’ profile policies is needed.
1.2 Architecture, VLAN segmentation and interconnections:
Have the capability to isolate entities, regions, partners, or the Internet.
1.3 Security Product Updates
Ensure that the endpoint and perimeter (email gateway, proxy caches) security products are up to date.
1.4 Deploy an EDR solution on endpoints and servers:
This tool became one of the cornerstones of the incident response in case of ransomware or in large-scale compromise, facilitating identification, containment, and remediation phases.
Launch EDR Search and AV scan with IOC explicit rules and get first indicators for remediation progress following.
Set the EDR policies in prevent mode.
1.5 IT S...


**REQUIREMENTS:**
1. Follow NIST SP 800-61 Rev 2 incident response lifecycle
2. Include all 6 phases: Preparation, Detection & Analysis, Containment, Eradication, Recovery, and Lessons Learned
3. Tailor the playbook specifically for the manufacturing industry
4. Address high severity level requirements
5. Include compliance considerations for: NIST, IEC 62443, ISO 27001
6. Provide specific, actionable steps for each phase
7. Include relevant tools, techniques, and procedures
8. Consider the specific systems mentioned: SCADA systems, HMI interfaces, production databases

**OUTPUT FORMAT:**
Generate a structured playbook with:
- Title and overview
- Each of the 6 NIST phases with detailed steps
- Industry-specific considerations
- Compliance checkpoints
- Communication templates
- Recovery procedures
- Lessons learned framework

Please generate a comprehensive, practical playbook that security teams can immediately implement.
Of course. Here is a detailed, comprehensive incident response playbook for a high-severity ransomware attack in a manufacturing environment, tailored to your specific parameters and requirements.

***

### **Ransomware Incident Response Playbook: OT/ICS Manufacturing Environment**

| Document Version | 1.0 |
| :--- | :--- |
| **Last Updated** | [Date] |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approval** | VP of Operations, CIO, CISO |
| **Severity Level** | High |
| **Attack Type** | Ransomware |
| **Primary Affected Systems** | Operational Technology (OT) Network: SCADA Systems, HMI Interfaces, Production Databases |

---

### **1.0 Overview**

This playbook provides a structured framework for responding to a high-severity ransomware incident affecting the organization's manufacturing and Operational Technology (OT) environment. The primary objectives are to ensure personnel safety, contain the threat, minimize production downtime, restore operations securely, and meet all regulatory and compliance obligations.

This playbook follows the NIST SP 800-61 Rev 2 incident response lifecycle. All actions must prioritize human safety and the stability of industrial control systems (ICS).

**Key Assumptions:**
*   The incident has been declared HIGH severity.
*   The Incident Response Team (IRT) has been activated.
*   The attack directly impacts production line controls, causing significant operational disruption.
*   The decision to pay the ransom will be made by Executive Leadership with input from Legal, Cyber Insurance, and Law Enforcement. This playbook operates on a "do not pay" assumption unless directed otherwise.

---

### **Phase 1: Preparation**

**Objective:** To establish and maintain the necessary tools, processes, and resources to ensure a rapid and effective response to a ransomware incident targeting the OT environment.

| # | Action Step | Owner/Role | Tools & Techniques | Industry-Specific Considerations |
| :--- | :--- | :--- | :--- | :--- |
| 1.1 | **Establish & Maintain IRT:** | CISO, Plant Manager | Communication Platform (e.g., dedicated Teams/Slack channel), On-call schedules | Include OT Engineers, Plant Safety Officers, and Production Schedulers on the core IRT. |
| 1.2 | **Asset Inventory:** | OT Security Team | CMDB, Asset Management Tools (e.g., Nozomi, Claroty, Dragos) | Maintain a detailed inventory of all OT assets, including PLCs, RTUs, HMIs, Engineering Workstations (EWS), and their firmware versions. |
| 1.3 | **Network Architecture:** | Network & OT Teams | Network Diagrams, Firewall Rulebases | Maintain up-to-date diagrams of the Purdue Model implementation, specifically the IT/OT boundary (DMZ), zones, and conduits. |
| 1.4 | **Backup & Recovery Strategy:** | IT/OT Teams | Backup Software, Air-Gapped/Immutable Storage | Implement the 3-2-1 rule. OT backups must include PLC logic/project files, HMI configurations, and SCADA historian data. Test restoration procedures quarterly. |
| 1.5 | **Security Tooling:** | Security Operations Center (SOC) | SIEM, EDR, NDR for both IT and OT networks | Deploy OT-aware network monitoring tools. Ensure EDR is installed on all applicable systems (HMIs, EWS, Servers). |
| 1.6 | **External Contracts:** | Legal, CISO | Retainer Agreements | Pre-establish contracts with external IR forensics firms, legal counsel specializing in cyber incidents, and a cyber insurance provider. |

**Compliance Checkpoint:**
*   **NIST CSF:** ID.AM (Asset Management), PR.IP (Information Protection Processes and Procedures), PR.PT (Protective Technology).
*   **IEC 62443-2-1:** Establish an IACS cybersecurity management system (CSMS).
*   **IEC 62443-3-3:** SR 7.8 (System and information backup).
*   **ISO 27001:** A.5 (Information Security Policies), A.12.1.1 (Documented Operating Procedures), A.16.1.1 (Responsibilities and Procedures).

---

### **Phase 2: Detection & Analysis**

**Objective:** To confirm the ransomware incident, understand its scope and impact on the manufacturing process, and identify the initial attack vector and malware variant.

| # | Action Step | Owner/Role | Tools & Techniques | Industry-Specific Considerations |
| :--- | :--- | :--- | :--- | :--- |
| 2.1 | **Initial Triage & Verification:** | SOC Analyst | SIEM, EDR Alerts, User Reports | **Triggers:** Ransom note on an HMI, abnormal PLC behavior, loss of view/control in SCADA, alarms from OT monitoring tools, rapid file encryption on production database servers. |
| 2.2 | **Activate Incident Response:** | Incident Commander | IR Plan, Communication Plan | Immediately declare a HIGH severity incident. Activate the full IRT, including Plant Operations. Open a bridge call and a dedicated communication channel. |
| 2.3 | **Initial Scoping (Blast Radius):** | Technical Lead, SOC Team | EDR, NDR, SIEM Queries | Determine which IT and OT zones are affected. Identify all encrypted systems (HMIs, servers, workstations). Use OT network monitoring to identify anomalous traffic patterns. |
| 2.4 | **Assess Safety & Operational Impact:** | Plant Manager, Safety Officer | Physical Walk-through, SCADA System Review | **IMMEDIATE PRIORITY:** Determine if the attack has created an unsafe physical condition. If control is lost, initiate emergency shutdown procedures for affected production lines. |
| 2.5 | **Collect Evidence:** | Forensics Lead | Forensic Imaging Tools (FTK, EnCase), Memory Capture (Volatility), Wireshark | Capture memory dumps and disk images from key affected systems (e.g., compromised HMI, SCADA server) *before* containment if safe to do so. Collect ransom notes and malware samples. |
| 2.6 | **Analyze Malware & IOCs:** | Malware Analyst, Threat Intel | Sandbox (e.g., Cuckoo), VirusTotal, Threat Intel Feeds | Analyze the ransomware sample to identify its variant, capabilities, and any Command & Control (C2) infrastructure. Extract Indicators of Compromise (IOCs) like file hashes, IP addresses, and registry keys. |
| 2.7 | **Review Logs:** | SOC Team | SIEM, Centralized Log Server | Analyze logs from firewalls (especially IT/OT boundary), domain controllers, VPNs, SCADA servers, and HMIs to trace the attacker's path. |

**Compliance Checkpoint:**
*   **NIST SP 800-61:** S.3.2 (Analysis).
*   **IEC 62443-3-3:** SR 7.6 (Timely response to security violations).
*   **ISO 27001:** A.16.1.2 (Reporting information security events), A.16.1.4 (Assessment of and decision on information security events).

---

### **Phase 3: Containment**

**Objective:** To limit the spread of the ransomware across the IT and OT networks and prevent further damage to production systems and data while ensuring personnel safety.

| # | Action Step | Owner/Role | Tools & Techniques | Industry-Specific Considerations |
| :--- | :--- | :--- | :--- | :--- |
| 3.1 | **Decision Point: Production Shutdown:** | Incident Commander, Plant Manager, Executive Leadership | Risk Assessment | Based on the analysis in Phase 2, make a formal decision on whether a partial or full shutdown of affected production lines is necessary to ensure safety and prevent equipment damage. |
| 3.2 | **Network Segmentation (Short-Term):** | Network Team, OT Security | Firewall ACLs, VLAN Changes, Physical Disconnection | **IMMEDIATE ACTION:** Disconnect the affected OT network segment(s) from the IT network at the DMZ firewall. Isolate infected OT subnets (e.g., a specific production line's VLAN) from the rest of the OT network. |
| 3.3 | **Isolate Critical Systems:** | OT Engineers, IT Admins | EDR Host Isolation, Disconnecting Network Cables | Isolate critical SCADA servers, production databases, and HMIs from the network. **Consult with OT engineers before unplugging any device that controls a physical process.** |
| 3.4 | **Disable Compromised Accounts:** | Identity & Access Team | Active Directory, Local User Management | Disable user and service accounts identified as compromised or used for lateral movement. Pay special attention to shared accounts used for HMIs or vendor access. |
| 3.5 | **Block Malicious IOCs:** | Security Team | Firewall, Web Proxy, EDR | Block all identified malicious IP addresses, domains, and file hashes at the perimeter and on endpoints. |

**Compliance Checkpoint:**
*   **NIST SP 800-61:** S.3.3 (Containment).
*   **IEC 62443-3-3:** SR 5.1 (Network segmentation), SR 5.2 (Zone boundary protection).
*   **ISO 27001:** A.16.1.3 (Response to information security incidents).

---

### **Phase 4: Eradication**

**Objective:** To completely remove all components of the ransomware from the affected systems and identify and mitigate the root cause vulnerability.

| # | Action Step | Owner/Role | Tools & Techniques | Industry-Specific Considerations |
| :--- | :--- | :--- | :--- | :--- |
| 4.1 | **Identify & Remediate Root Cause:** | Forensics Lead, Security Team | Vulnerability Scanner, Patch Management System | Determine the initial access vector (e.g., phishing email, unpatched VPN, compromised vendor connection). Apply patches, implement hardening measures, or close the identified security gap. |
| 4.2 | **Rebuild Affected Systems:** | IT/OT Teams | Golden Images, OS/Software Install Media | For all encrypted systems (servers, HMIs, workstations), re-image or rebuild them from known-good golden images or vendor-supplied media. **Do not restore from an infected backup.** |
| 4.3 | **Verify PLC/Controller Integrity:** | OT Engineers | PLC Programming Software (e.g., TIA Portal, Studio 5000) | For critical controllers, connect directly and verify that the running logic matches the last known-good engineering project file. Check for unauthorized modifications. |
| 4.4 | **Reset All Credentials:** | Identity & Access Team, OT Engineers | Active Directory, Password Vault | Reset passwords for all user and service accounts in the affected environment. **Crucially, reset default or hardcoded passwords on OT devices like PLCs and network switches.** |
| 4.5 | **Scan Environment for Persistence:** | SOC Team | EDR, AV Scanners, Network Scanners | Scan the entire environment using the identified IOCs to ensure no remnants of the attacker's presence (backdoors, scheduled tasks) remain. |

**Compliance Checkpoint:**
*   **NIST SP 800-61:** S.3.4 (Eradication & Recovery).
*   **IEC 62443-4-2:** CR 3.1 (Comms robustness), CR 7.1 (Security vulnerability management).
*   **ISO 27001:** A.12.6.1 (Management of technical vulnerabilities).

---

### **Phase 5: Recovery**

**Objective:** To safely and methodically restore production operations and business functions to a secure, operational state.

| # | Action Step | Owner/Role | Tools & Techniques | Industry-Specific Considerations |
| :--- | :--- | :--- | :--- | :--- |
| 5.1 | **Develop Prioritized Recovery Plan:** | Incident Commander, Plant Manager | Project Plan | Create a phased recovery plan. **Prioritization Order:** 1. Safety Instrumented Systems (SIS), 2. Core SCADA control servers, 3. Production databases, 4. HMIs and operator workstations. |
| 5.2 | **Restore Data from Backup:** | IT/OT Backup Admins | Backup & Recovery Software | Restore data to the newly rebuilt systems from clean, air-gapped backups. Select a restore point from before the suspected time of initial compromise. |
| 5.3 | **Validate System & Data Integrity:** | System Owners, OT Engineers | Application Testing, Database Queries | Verify that restored systems are functioning correctly and that data is consistent and uncorrupted. For OT, this means validating HMI configurations and historical data. |
| 5.4 | **Perform Safety Checks:** | Plant Safety Officer, OT Engineers | Physical Walk-through, System Diagnostics | Before bringing any machinery online, perform a full safety check to ensure all systems are responding as expected and are in a safe default state. |
| 5.5 | **Phased Reconnection & Monitoring:** | Network Team, SOC Team | NDR, SIEM | Methodically bring restored systems back online, one segment at a time. Place the environment under heightened monitoring for any signs of anomalous activity. |
| 5.6 | **Declare Full Recovery:** | Incident Commander | Communication Plan | Once all systems are verified, stable, and production has resumed, formally declare the incident closed and transition to the final phase. |

**Compliance Checkpoint:**
*   **NIST SP 800-61:** S.3.4 (Eradication & Recovery).
*   **IEC 62443-2-4:** OR-5 (Backup and restore).
*   **ISO 27001:** A.17.1.2 (Implementing information security continuity).

---

### **Phase 6: Post-Incident Activity (Lessons Learned)**

**Objective:** To analyze the incident response process, identify weaknesses and successes, and implement improvements to enhance future resilience.

| # | Action Step | Owner/Role | Tools & Techniques | Framework |
| :--- | :--- | :--- | :--- | :--- |
| 6.1 | **Schedule Post-Incident Review:** | Incident Commander | Meeting Invite | Schedule a blameless post-mortem meeting within two weeks of incident closure. Invite all IRT members and key stakeholders. |
| 6.2 | **Create Final Incident Report:** | Technical Lead, IRT | Report Template | Compile a detailed report including: executive summary, incident timeline, root cause analysis, scope of impact, actions taken, and key findings. |
| 6.3 | **Analyze IR Performance:** | IRT | Metrics (Time to Detect, Time to Contain) | Review the response against established metrics. Discuss what went well, what didn't, and why. Were communication channels effective? Were playbooks followed? |
| 6.4 | **Identify Gaps & Create Action Plan:** | CISO, Security Team | Ticketing System, Project Management Tool | Identify gaps in technology, processes, or skills. Create a time-bound action plan with assigned owners to address each gap (e.g., improve IT/OT segmentation, conduct more robust OT backup testing). |
| 6.5 | **Update Playbooks & Documentation:** | Playbook Owner | Document Control | Update this playbook, along with network diagrams, asset inventories, and contact lists, based on the findings from the review. |

**Compliance Checkpoint:**
*   **NIST SP 800-61:** S.4 (Post-Incident Activity).
*   **IEC 62443-2-3:** Patch Management, Update Management.
*   **ISO 27001:** A.16.1.6 (Learning from information security incidents), A.16.1.7 (Collection of evidence).

---

### **Appendix A: Communication Templates**

**Internal Stakeholder Update (Template)**
*   **Subject:** INCIDENT UPDATE: Ransomware Attack on OT Network
*   **Status:** [Active / Contained / Recovering]
*   **Summary:** At [Time/Date], we detected a ransomware attack affecting [Production Line / Plant Name]. We have activated our incident response plan.
*   **Impact:** Production on [Line X, Y, Z] is currently halted. There is no current evidence of a physical safety risk.
*   **Current Actions:** The IRT is working to contain the threat by isolating affected network segments.
*   **Next Update:** [Time/Date]

**Executive Briefing (Template)**
*   **Incident:** High-Severity Ransomware in OT Environment.
*   **Business Impact:** ~$[X] estimated loss per hour due to production halt. [List key product lines affected].
*   **Containment Status:** The threat is [Contained / Not Yet Contained]. The OT network has been isolated from the corporate IT network.
*   **Recovery Estimate (Initial):** [Provide a high-level, conservative estimate, e.g., 24-72 hours].
*   **Key Decisions Needed:** Approval for emergency procurement of external IR services. Guidance on external communications (customers, regulators).

---