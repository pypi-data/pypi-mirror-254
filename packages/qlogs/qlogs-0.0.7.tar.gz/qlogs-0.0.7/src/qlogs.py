import os, re, argparse, json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def search(query, directory, encoding):  
    if not directory.endswith('/'):
        directory += '/'
        
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        for file_name in files:
            file_path = os.path.join(directory, file_name)
            matching_lines = []

            try:
            # Open the file and read lines
                with open(file_path, 'r', encoding=encoding if encoding else 'utf-8') as file:
                    for line in file:
                        # Check if the search term is present in the line
                        if re.search(query, line):
                            # Append matching line along with file name and line number
                            matching_lines.append(f"{line.strip()}")
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
        
            print(f"Found in {file_name}: {len(matching_lines)}")
    except Exception as e:
        print(f'There was an issue loading the files from the provided directory, please try again.')


def lookup(cve, directory, encoding):
    try:
        with open(os.path.join(__location__, f'data/{cve.lower()}.json')) as file:
            data = json.load(file)
            queries = data["queries"]
            statusCode = data["statusCode"][0]
        
            if not directory.endswith('/'):
                directory += '/'

            try:
                files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

                for file_name in files:
                    file_path = os.path.join(directory, file_name)
                    matching_lines = []

                    try:
                        # Open the file and read lines
                        with open(file_path, 'r', encoding=encoding if encoding else 'utf-8') as file:
                            for line in file:
                                # Check if the cve paths are present in the line
                                for query in queries:
                                    # if re.search(query, line) and re.search(f' {statusCode} ', line):
                                    if line.__contains__(query) and line.__contains__(f' {statusCode} '):
                                        # Append matching line
                                        matching_lines.append(f"{line.strip()}")
                    except Exception as e:
                        print(f"Error reading {file_name}: {e}")
        
                    print(f"Found in {file_name}: {len(matching_lines)}")
            except Exception as e:
                print(f'There was an issue loading the files from the provided directory, please try again.')
    except Exception as e:
        print(f'Unfortunately, this CVE is not yet supported.')


def main():
    parser = argparse.ArgumentParser(prog="qlogs", description="Pass in a CVE value as a query parameter and qlogs will search your log files for evidence of compromise.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-q", "--query", help="Query string")
    parser.add_argument("-c", "--cve", help="CVE record")
    parser.add_argument("-d", "--directory", help="Directory string")
    parser.add_argument("-e", "--encoding", help="Defaults to utf-8")
    args = parser.parse_args()

    if (args.query):
        search(args.query, args.directory, args.encoding)
    elif (args.cve):
        lookup(args.cve, args.directory, args.encoding)
    else:
        print('Please provide either a query string or CVE record number, along with the directory to perform the scan.')


if __name__ == "__main__":
    main()
