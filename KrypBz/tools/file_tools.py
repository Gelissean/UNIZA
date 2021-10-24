def get_file_paths(path):  # TODO
    pass


def read_file(path):
    file = open(path)
    text = []
    for riadok in file:
        text.append(riadok)
    return ''.join(text)


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
