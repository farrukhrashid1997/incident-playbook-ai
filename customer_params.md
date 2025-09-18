
### The parameters examples we can ask from the customer 
{
    "attack_type":  "Ransomware" or "Malware" | "Phishing" | "DDoS Attack" | "Insider Threat" | "Data Breach" 
    "environment_type": "OT (Operational Technology)" | "IT (Information Technology)" | "Hybrid (IT/OT)" | "Cloud Environment",
    "industry": "Manufacturing" | "Energy & Utilities" | "Healthcare" | "Financial Services" | "Transportation" | "Government",
    "severity_level": "Critical" | "High" | "Medium" | "Low",
    "affected_systems": [
    "systems can be mentioned, with how much ever details"],
    "compliance_requirements": [
        "is the customer following any compliance requirements internally which we should keep in mind while generating the incident response playbooks?"
  ],
  "additional_context": "Any extra information to make the response better?"
}


### Example of a customer param
{
  "attack_type": "ransomware",
  "industry": "manufacturing",
  "severity_level": "high",
  "environment_type": "OT (Operational Technology)", 
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


