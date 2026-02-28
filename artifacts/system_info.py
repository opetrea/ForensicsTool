import os
import json
import subprocess
from datetime import datetime

def run_command(command: str) -> str:
    # Rulez o comanda in shell si returnez output-ul

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def collect_system_info(case_path: str) -> None:
    # Colectez infromatii live despre sistem; salvez output-ul raw, generez artifac JSON in parsed;

    raw_path = os.path.join(case_path, "raw")
    parsed_path = os.path.join(case_path, "parsed")

    timestamp = datetime.utcnow().isoformat()

    # Colectare live
    hostname = run_command("hostname")
    uname = run_command("uname -a")
    uptime = run_command("uptime")
    current_user = run_command("whoami")
    os_release = run_command("cat /etc/os-release")
    users = run_command("cut -d: -f1 /etc/passwd")

    # Salvez raw
    raw_file_path = os.path.join(raw_path, "system_info.txt")
    with open(raw_file_path, "w") as f:
        f.write("==== HOSTNAME ====\n")
        f.write(hostname + "\n\n")

        f.write("==== UNAME ====\n")
        f.write(uname + "\n\n")

        f.write("==== UPTIME ====\n")
        f.write(uptime + "\n\n")

        f.write("==== CURRENT USER ====\n")
        f.write(current_user + "\n\n")

        f.write("==== OS RELEASE ====\n")
        f.write(os_release + "\n\n")

        f.write("==== USERS ====\n")
        f.write(users + "\n")

    # Generez JSON
    artifact = {
        "timestamp": timestamp,
        "artifact_type": "system_info",
        "source": "live_commands",
        "data": {
            "hostname": hostname,
            "kernel": uname,
            "uptime": uptime,
            "current_user": current_user,
            "os_release": os_release,
            "users": users.split("\n")
        }
    }

    parsed_file_path = os.path.join(parsed_path, "system_info.json")

    with open(parsed_file_path, "w") as f:
        json.dump(artifact, f, indent=4)

    print(f"[+] System info collected and saved to {parsed_file_path}")