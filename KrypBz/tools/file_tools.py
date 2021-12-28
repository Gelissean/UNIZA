import os


def get_file_paths(path):
    file_list = []
    for root, subs, files in os.walk(path):
        for file in files:
            cesta = os.path.join(root, file)
            if os.path.isfile(cesta) & (file[-4:] == ".txt"):
                file_list.append(cesta)
        # Modify directories in place to remove directories starting with '.'
        for dir in subs[:]:
            if dir.startswith('.'):
                subs.remove(dir)
    return file_list


def read_file(path):
    file = open(path)
    text = []
    for riadok in file:
        text.append(riadok)
    return ''.join(text)

def read_file_lines(path):
    file = open(path)
    text = []
    for riadok in file:
        text.append(riadok)
    return text

def read_ascii_from_file(path):
    file = open(path)
    text = []
    for riadok in file:
        for c in riadok:
            if (ord(c) >= ord('A')) & (ord(c) <= ord('Z')):
                text.append(c)
    return ''.join(text)


def convert_to_ascii(text):
    retval = []
    for c in text:
        if (ord(c) >= ord('A')) & (ord(c) <= ord('Z')):
            retval.append(c)
    return ''.join(retval)


def write_to_file(text, path):
    file = open(path, 'w')
    file.write(text)
    file.close()


def make_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)
