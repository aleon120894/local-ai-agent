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
