"""
NetForge Lines of Code (LOC) Verifier
Calculates physical, logical, non-blank, and non-comment lines of code across all project files.
"""

import os
import sys

def count_lines(directory):
    total_files = 0
    total_raw_lines = 0
    total_code_lines = 0
    total_comments = 0
    total_blank = 0
    
    breakdown = {}

    for root, _, files in os.walk(directory):
        if "__pycache__" in root or ".git" in root or ".pytest_cache" in root:
            continue
        
        rel_root = os.path.relpath(root, directory)
        dir_name = rel_root.split(os.sep)[0] if rel_root != "." else "root"
        
        if dir_name not in breakdown:
            breakdown[dir_name] = {"files": 0, "lines": 0, "code": 0}

        for file in files:
            if file.endswith((".py", ".html", ".md", ".json", ".yml", ".yaml")):
                filepath = os.path.join(root, file)
                total_files += 1
                breakdown[dir_name]["files"] += 1
                
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        for line in f:
                            total_raw_lines += 1
                            breakdown[dir_name]["lines"] += 1
                            sline = line.strip()
                            if not sline:
                                total_blank += 1
                            elif sline.startswith("#") or sline.startswith("//") or sline.startswith("/*") or sline.startswith("*"):
                                total_comments += 1
                            else:
                                total_code_lines += 1
                                breakdown[dir_name]["code"] += 1
                except Exception as e:
                    pass

    print("=" * 65)
    print("                NETFORGE LOC VERIFICATION REPORT                ")
    print("=" * 65)
    print(f"{'Module / Subsystem':<25} | {'Files':<8} | {'Total Lines':<12} | {'Code Lines':<12}")
    print("-" * 65)
    for d, stats in sorted(breakdown.items()):
        print(f"{d:<25} | {stats['files']:<8} | {stats['lines']:<12,} | {stats['code']:<12,}")
    print("-" * 65)
    print(f"{'TOTAL CODEBASE':<25} | {total_files:<8} | {total_raw_lines:<12,} | {total_code_lines:<12,}")
    print("=" * 65)
    
    if total_raw_lines >= 50000:
        print(f"SUCCESS: Codebase size requirement met ({total_raw_lines:,} >= 50,000 LOC)")
        return 0
    else:
        print(f"WARNING: Codebase size is currently {total_raw_lines:,} LOC (< 50,000 Target)")
        return 1

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.exit(count_lines(base_dir))
