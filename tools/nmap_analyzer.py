import re


SERVICE_MAP = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
}

RECOMMENDATIONS = {
    "FTP": [
        "Check anonymous login",
        "nmap --script ftp-*",
        "Hydra password audit"
    ],

    "SSH": [
        "nmap -sV -p22",
        "Banner grabbing",
        "Check valid credentials",
        "Hydra password audit"
    ],

    "HTTP": [
        "whatweb",
        "gobuster",
        "feroxbuster",
        "nikto",
        "ffuf"
    ],

    "SMB": [
        "smbclient",
        "enum4linux",
        "smbmap",
        "crackmapexec"
    ]
}

def analyze(path):
    detected_services = []

    with open(path, "r") as f:
        lines = f.readlines()

        for line in lines:
            match = re.search(r"(\d+)/tcp\s+open", line)

            if not match:
                continue

            port = int(match.group(1))

            service = SERVICE_MAP.get(port)

            if service is not None:
                detected_services.append(
                    {
                        "port": port,
                        "service": service
                    }
                )

        return detected_services


def recommend(services):

    output = []

    for service in services:

        name = service["service"]

        output.append({
            "service": name,
            "port": service["port"],
            "recommendations": RECOMMENDATIONS.get(name, [])
        })

    return output