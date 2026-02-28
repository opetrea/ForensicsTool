import os
import json
import socket
from datetime import datetime

TOOL_VERSION = "1.0"

def create_case(case_name: str, mode: str) -> str:
    # Creez structura unui caz nou

    base_path = os.path.join("evidence", case_name)

    raw_path = os.path.join(base_path, "raw")
    parsed_path = os.path.join(base_path, "parsed")
    reports_path = os.path.join(base_path, "reports")

    # Creez directoarele
    os.makedirs(raw_path, exist_ok=True)
    os.makedirs(parsed_path, exist_ok=True)
    os.makedirs(reports_path, exist_ok=True)

    metadata = {
        "case_name" : case_name,
        "created at" : datetime.utcnow().isoformat(),
        "mode" : mode,
        "hostname" : socket.gethostname(),
        "tool_version" : TOOL_VERSION
    }

    # Salvez metadata
    metadata_path = os.path.join(base_path, "metadata.json")

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    return base_path