import argparse
import sys
from csvimporter import CSVImporter
from exceptions import InvalidDict
from enums import  FileType, OutPutEnum

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", metavar='path', type=str, help="Path to get the csv file")
    parser.add_argument("--filetype", action='store', type=str, help="File type uploaded(csv, excel)", default=FileType.CSV.name.lower(),
                        choices=FileType.list())
    parser.add_argument("--output", action='store', type=str, help="Output of the formatted data", default=OutPutEnum.JSON.name.lower(),
                        choices=OutPutEnum.list())
    args = parser.parse_args()

    try:
        if FileType[args.filetype.upper()] is FileType.CSV:
            importer = CSVImporter(filepath=args.path, type = args.filetype, output_format=args.output)
        elif FileType[args.filetype.upper()] is FileType.EXCEL:
            print("This feature is not implemented and is in the pipeline, Please try using csv for now for demo")
            sys.exit()
        data = importer.get_rows(args.path)
        print(next(data))
        print("imported")
    except FileExistsError:
        print("File does not exist")
    except InvalidDict as e:
        print("Invalid Data in your file please correct and  upload again")
    except Exception as e:
        print("Sorry something went wrong please try again later:", e)

if __name__ == "__main__":
    main()
