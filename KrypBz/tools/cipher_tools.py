def convert(original, deciphered, buffer_size=100):
    max_i = len(original)
    max_j = len(deciphered)
    retval = ""
    buffer = ""
    j = 0
    for i in range(max_i):
        if (original[i] >= 'A') & (original[i] <= 'Z') & (j < max_j):
            buffer += deciphered[j]
            j += 1
        else:
            buffer += original[i]
        if i % buffer_size == 0:
            retval += buffer
            buffer = ""
    retval += buffer
    return retval
