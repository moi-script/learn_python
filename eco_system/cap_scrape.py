import re
import json

from loc_scrape import scrapeLocalFile
# This is what the raw stdout from PowerShell's Get-FileHash usually looks like
raw_cli_output = scrapeLocalFile()

# 1. Define the Regex Pattern
# \s+ handles any unpredictable amount of whitespace
# ([A-F0-9]+) captures the uppercase hash into Group 1
# (.+) captures the rest of the line (the file path) into Group 2


def getInfoJson() :
    pattern = r"SHA256\s+([A-F0-9]+)\s+(.+)"
    
    # 2. Search the raw output for the pattern
    match = re.search(pattern, raw_cli_output)
    
    if match:
        # 3. Build a clean Python dictionary using the captured groups
        parsed_data = {
            "file_name": match.group(2).split('\\')[-1], # Grabs just the file name from the path
            "security_hash": match.group(1),
            "absolute_path": match.group(2).strip()
        }
        
        # 4. Convert to JSON
        # json.dumps() is Python's exact equivalent to JSON.stringify()
        # indent=4 makes it pretty-printed and easy to read
        json_result = json.dumps(parsed_data, indent=4)
        
        print("Successfully parsed into JSON:")
        print(json_result)
        return json_result
    else:
        print("Could not find a matching hash in the output.")
        
        