from KrypBz.tools.coincidence_indices import coincidence_indices


def to_index(char):
    return ord(char) - ord('A')


def to_char(num, alphabet_size):
    return chr(num % alphabet_size + ord('A'))


def coincidence_index_comparison(text, alphabet_size):
    indices = []
    for i in range(alphabet_size):
        indices.append(0)
    for c in text:
        indices[to_index(c)] += 1
    result = 0
    coinc_indices = coincidence_indices.get_all()
    retval = {}
    for key in coinc_indices:
        for j in range(alphabet_size):
            i = indices[j] / len(text)
            result += pow(i - coinc_indices[key][j], 2)
        retval[key] = result
    return retval


def coincidence_index(text, alphabet_size):
    indices = []
    for i in range(alphabet_size):
        indices.append(0)
    for c in text:
        indices[to_index(c)] += 1
    result = 0
    coinc_indices = coincidence_indices.get_all()
    retval = {}
    for j in range(alphabet_size):
        i = indices[j] / len(text)
        result += pow(i, 2)
    return result


def move_char(char, shift, alphabet_size):
    return to_char(to_index(char) + shift % alphabet_size, alphabet_size)
