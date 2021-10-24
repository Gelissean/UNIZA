def convert(original, deciphered):
    max_i = len(original)
    max_j = len(deciphered)
    retval = []
    j = 0
    for i in range(max_i):
        if (original[i] >= 'A') & (original[i] <= 'Z') & (j < max_j):
            retval.append(deciphered[j])
            j += 1
        else:
            retval.append(original[i])
    return ''.join(retval)
