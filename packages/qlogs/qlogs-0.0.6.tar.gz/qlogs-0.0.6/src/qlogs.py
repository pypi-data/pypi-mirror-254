import os, re, argparse, json

def search(query, directory):  

    if not directory.endswith('/'):
        directory += '/'
        
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file_name in files:
        file_path = os.path.join(directory, file_name)
        matching_lines = []

        try:
        # Open the file and read lines
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    # Check if the search term is present in the line
                    if re.search(query, line):
                        # Append matching line along with file name and line number
                        matching_lines.append(f"{line.strip()}")
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
        
        print(f"Found in {file_name}: {len(matching_lines)}")


def lookup(cve, directory):
    with open(os.path.join(__location__, f'data/{cve.lower()}.json')) as file:
        data = json.load(file)
        queries = data["queries"]
        statusCode = 200
        
        if not directory.endswith('/'):
            directory += '/'
        
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        for file_name in files:
            file_path = os.path.join(directory, file_name)
            matching_lines = []

            try:
                # Open the file and read lines
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                        # Check if the search term is present in the line
                        for query in queries:
                            if re.search(query, line) and re.search(f' {statusCode} ', line):
                                # Append matching line
                                matching_lines.append(f"{line.strip()}")
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
        
            print(f"Found in {file_name}: {len(matching_lines)}")


def main():
    parser = argparse.ArgumentParser(prog="qlogs", description="Pass in a CVE value as a query parameter and qlogs will search your log files for evidence of compromise.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-q", "--query", help="Query String")
    parser.add_argument("-c", "--cve", help="CVE Record")
    parser.add_argument("-d", "--directory", help="Directory String")
    args = parser.parse_args()

    if (args.query):
        search(args.query, args.directory)
    elif (args.cve):
        lookup(args.cve, args.directory)
    else:
        print('Please provide either a query string or CVE record number, along with the directory to perform the scan.')


if __name__ == "__main__":
    main()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
