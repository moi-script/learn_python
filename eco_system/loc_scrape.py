# Imagine you are building a system agent or a local file scraper 
# that needs to find all text files in a specific folder and then run a Windows 
# PowerShell command on them (for example, getting the SHA256 security hash of each file).


import subprocess
from pathlib import Path




def scrapeLocalFile() :
    
    # create or search  
    target_dir = Path('./my_scraped_files')


    # if exist or not then ok create a file in that folder 
    target_dir.mkdir(exist_ok=True)
    (target_dir / "sample_data.txt").write_text("Hello from the local file system!")

    print("Scanning directory...")

    # iterate in the folder and find all files with .txt
    for file_path in target_dir.glob('*.txt'):
     print(f"\nFound: {file_path.name}")

     absolute_path = file_path.resolve() # needs the absolute path for powershell path command
     # command set up for subprocess
     command = ["powershell", "-Command", f"Get-FileHash -Algorithm SHA256 '{absolute_path}'"]


     result = subprocess.run(command, capture_output=True, text=True)

     # print(result.stdout) # this output the result text type of hashed value
     if result.returncode == 0:
         return result.stdout
         
     else:
        print("An error occurred:")
        print(result.stderr)
        
# scrapeLocalFile()