# Automation
This repository will feature a straightforward design and include a selection of automation tools to streamline and enhance daily penetration testing activities. Its structure and contents will include the following:
## Search Keywords in Files
This Python script recursively searches through all files in a given directory (including subdirectories) for specific keywords provided in a text file. It highlights any found keywords on the Linux terminal for easy visibility.

#### **Usage:**
1. Save a list of keywords in a file, one per line (e.g., `keywords.txt`).
2. Run the script with the following command:
   ```bash
   python search_keywords.py <directory> <keywords_file>
   ```
   Example:
   ```bash
   python search_keywords.py /var/www/html /path/to/keywords.txt
   ```
   
