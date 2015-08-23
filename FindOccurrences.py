__author__ = 'jeet'

import sys
import getopt
import os
import re
import matplotlib.pyplot as plt


def search_directory(root_directory, find_word):
    result = {}
    if os.path.isdir(root_directory):
        for cur_dir, sub_dir, files in os.walk(root_directory):
            no_of_file = 0
            for cur_file in files:
                if not cur_file.startswith('.'):
                    relative_path = os.path.join(cur_dir, cur_file)
                    if is_word_present(relative_path, find_word):
                        no_of_file += 1

            result[cur_dir] = no_of_file

        print(result)
        generate_plot(result, find_word)
    else:
        print("Path does not exist.")
        sys.exit()


def is_word_present(file_path, keyword_to_find):
    cur_file_content = open(file_path, 'r')
    is_find = re.search(keyword_to_find, cur_file_content.read())
    cur_file_content.close()
    if is_find:
        return True
    else:
        return False


def generate_plot(result_file, passed_keyword):
    directory_name = result_file.keys()
    file_count = result_file.values()
    x = [x for x in range(len(result_file.keys()))]
    fig = plt.figure(figsize=(12, 8))
    plt.xticks(x, directory_name, rotation=45)
    plt.bar(x, file_count)
    plt.xlabel("Directory")
    plt.ylabel("Count of files")
    plt.title("Find number of files containing keyword: " + passed_keyword)
    plt.show()
    fig.savefig("Output.png")
    plt.close()

if __name__ == '__main__':
    root_dir = ""
    keyword = ""

    if len(sys.argv) != 5:
        print("Input must be in below format: FindOccurrences.py -r <root_dir> -k <keyword>")
        sys.exit(2)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "r:k:", ["root_dir=", "keyword="])
    except getopt.GetoptError:
        print("Input must be in below format: FindOccurrences.py -r <root_dir> -k <keyword>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-r", "--root_dir"):
            root_dir = arg
        elif opt in ("-k", "--keyword"):
            keyword = arg
        else:
            print("Input must be in below format: FindOccurrences.py -r <root_dir> -k <keyword>")
            sys.exit()

    search_directory(root_dir, keyword)
