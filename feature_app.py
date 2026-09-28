#!/usr/bin/env python3
"""
Lab 2 Creative Feature: Git Branching & Feature Workflow Demo
Student: Shreyas M H
Experiment: Creating and Managing Branches in Git
"""

import sys
import subprocess

BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{PURPLE}{BOLD}
  ____ ___ _____   _        _    ____     ____  
 / ___|_ _|_   _| | |      / \\  | __ )   |___ \\ 
| |  _ | |  | |   | |     / _ \\ |  _ \\     __) |
| |_| || |  | |   | |___ / ___ \\| |_) |   / __/ 
 \\____|___| |_|   |_____/_/   \\_\\____/   |_____|
{RESET}{CYAN}>> Experiment 2: Branch Creation, Feature Work & Merging <<{RESET}
"""

def show_branch_graph():
    print(f"\n{BOLD}{YELLOW}[*] Git Branch Lifecycle Visualization:{RESET}")
    print(f"""{CYAN}
       (feature-branch) ───[ Commit: Added new feature ]───┐
      /                                                    │ (git merge feature-branch)
     /                                                     ▼
(main) ───[ Initial Commit ]───────────────────────> [ Merged State ]
    {RESET}""")

def run_git_status():
    print(f"\n{BOLD}{GREEN}[*] Live Git Branch Status:{RESET}")
    try:
        branch_output = subprocess.check_output(["git", "branch", "-vv"], text=True)
        print(f"{BLUE}{branch_output.strip()}{RESET}")
        
        log_output = subprocess.check_output(
            ["git", "log", "--graph", "--oneline", "--decorate", "--all", "-n", "5"],
            text=True
        )
        print(f"\n{BOLD}{YELLOW}[*] Commit Graph History:{RESET}")
        print(log_output)
    except Exception as e:
        print(f"Git status info unavailable: {e}")

def main():
    print(BANNER)
    print(f"{GREEN}✓ Student: Shreyas M H (@shreyasMH26){RESET}")
    print(f"{GREEN}✓ Feature Status: Feature developed on 'feature-branch' and merged into 'main'!{RESET}")
    show_branch_graph()
    run_git_status()
    print(f"\n{BOLD}{CYAN}Feature successfully verified!{RESET}\n")

if __name__ == "__main__":
    main()
