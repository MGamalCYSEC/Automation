import os
import argparse

# Define the ANSI escape code for red text
RED = '\033[91m'
RESET = '\033[0m'

def highlight_keyword(line, keyword):
    """Highlight the keyword in the line with red color."""
    return line.replace(keyword, f"{RED}{keyword}{RESET}")

def search_keywords_in_directory(input_directory, keywords_file):
    try:
        # Read the keywords from the file
        with open(keywords_file, 'r') as kf:
            keywords = [line.strip() for line in kf.readlines()]
        
        print(f"Loaded keywords: {keywords}")
        print(f"Searching in directory: {input_directory}")
        
        # Walk through the directory and all subdirectories
        for root, dirs, files in os.walk(input_directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', errors='ignore') as f:
                        for line_number, line in enumerate(f, start=1):
                            for keyword in keywords:
                                if keyword in line:
                                    highlighted_line = highlight_keyword(line.strip(), keyword)
                                    print(f"[{file_path}] Line {line_number}: {highlighted_line}")
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Search for keywords in files within a directory.")
    parser.add_argument("directory", type=str, help="The directory to search.")
    parser.add_argument("keywords_file", type=str, help="The file containing keywords, one per line.")

    args = parser.parse_args()
    search_keywords_in_directory(args.directory, args.keywords_file)

if __name__ == "__main__":
    main()
