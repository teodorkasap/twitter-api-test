import re


def read_file_to_list(file):
    lineList = [line.rstrip('\n') for line in open(file)]
    return lineList

def get_creds(file_path):
    creds_list = read_file_to_list(file_path)
    creds = {}
    for var in creds_list:
        key = re.search('(^[^:]*)', var)
        value = re.search(':(.*)', var)
        if key:
            key_name = str(key.group(1))
        if value:
            key_value = str(value.group(1))
        creds.update({key_name:key_value})
    print(creds)
    return creds