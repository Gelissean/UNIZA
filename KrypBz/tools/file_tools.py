def get_file_paths(path):  # TODO
    pass


def read_file(path):
    file = open(path)
    text = ""
    for riadok in file:
        text += riadok
    return text


def read_ascii_from_file(path):
    file = open(path)
    text = ""
    for riadok in file:
        text2 = ""
        for c in riadok:
            if (ord(c) >= ord('A')) & (ord(c) <= ord('Z')):
                text2 += c
        text += text2
    return text


def convert_to_ascii(text, buffer_size=100):
    retval = ""
    buffer = ""
    i = 0
    for c in text:
        if (ord(c) >= ord('A')) & (ord(c) <= ord('Z')):
            buffer += c
        i += 1
        if i >= buffer_size:
            i = 0
            retval += buffer
            buffer = ""
    retval += buffer
    return retval


def write_to_file(text, path):
    file = open(path, 'w')
    file.write(text)
    file.close()
