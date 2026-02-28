# Fisierul care porneste tool-ul

import argparse
from core.case_manager import create_case
from artifacts.system_info import collect_system_info

def main():
    parser = argparse.ArgumentParser(description="Forensics Tool")

    parser.add_argument("--collect-system", action="store_true", help="Collect system info")
    parser.add_argument("--case", help="Case name")

    args = parser.parse_args()
    
    if args.collect_system and args.case:
        case_path = f"evidence/{args.case}"
        collect_system_info(case_path)


if __name__ == "__main__":
    main()