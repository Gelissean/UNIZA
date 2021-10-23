# f = open(file)
from tools.file_tools import read_ascii_from_file


def kassisk(file_name, key_length=3):
    matches = []
    text = read_ascii_from_file(file_name)
    text_length = len(text)
    for i in range(text_length - key_length):
        for j in range(i + 1, text_length - key_length):
            found = True
            for k in range(key_length):
                if text[i + k] != text[j + k]:
                    found = False
                    break
            if found:
                matches.append((j - i, text[i: i + key_length]))
    return matches


if __name__ == "__main__":
    retval = kassisk("../text1_enc.txt")
    print(retval)
