__author__ = 'jeet'

import sys
import getopt
import os


def merge_files(location):
    if os.path.isdir(location):
        print "============================================"
        print "Merge Below Files In The Directory"
        print "============================================"
        for cur_file in os.listdir(location):
            if cur_file.endswith(".txt"):
                print cur_file
                merge_content(os.path.join(location, cur_file))
        print "============================================"
    else:
        print("Command must be in --> python MergeFile.py -p 'path' <-- format")
        sys.exit(2)


def merge_content(file_to_merge):
    output_file = open("Result.txt", 'a')
    current_file = open(file_to_merge, 'r')
    output_file.write(current_file.read())


if __name__ == '__main__':
    directory_path = ""

    if len(sys.argv) != 3:
        print("Command must be in --> python MergeFile.py -p 'path' <-- format")
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:", ["path="])
    except getopt.GetoptError:
        print("Command must be in --> python MergeFile.py -p 'path' <-- format")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-p", "--path"):
            directory_path = arg
        else:
            print("Command must be in --> python MergeFile.py -p 'path' <-- format")
            sys.exit()

    merge_files(directory_path)
