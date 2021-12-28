# f = open(file)

def kassisk(file_name, key_length=3):
    matches = []
    file = open(file_name)
    text = ""
    for riadok in file:
        text2 = ""
        for c in riadok:
            if (ord(c) >= ord('A')) & (ord(c) <= ord('Z')):
                text2 += c
        text += text2
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
    retval = kassisk("../cyphered/text2_enc.txt")
    print(retval)
