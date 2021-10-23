def to_index(char):
    return ord(char) - ord('A')


def to_char(num, alphabet_size):
    return chr(num % alphabet_size + ord('A'))


def coincidence_index_comparison(text, alphabet_size, probabilities):
    indeces = []
    for i in range(alphabet_size):
        indeces.append(0)
    for c in text:
        indeces[to_index(c)] += 1
    result = 0
    for j in range(alphabet_size):
        i = indeces[j] / len(text)
        result += pow(i - probabilities[j], 2)
    return result


def move_char(char, shift, alphabet_size):
    return to_char(to_index(char) + shift % alphabet_size, alphabet_size)
