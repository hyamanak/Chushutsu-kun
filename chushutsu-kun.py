import re, sys, os

            
def check_duplication_in_file(existing_file, word):
    return word not in existing_file

def check_duplication_in_list(word):
    return word not in matched_list

with open(sys.argv[1], 'r') as doc_file, open(sys.argv[2], 'a+') as docw_file:
    matched_list = []

    for line in doc_file.readlines():
        for word in re.findall(r"([A-Z][\w-]*(?:\s+[A-Z][\w-]*)+)", line):
           if check_duplication_in_list(word) and check_duplication_in_file(docw_file, word):
                matched_list.append(word)
    
    for word_to_add in matched_list:
        print(word_to_add, file=docw_file)



