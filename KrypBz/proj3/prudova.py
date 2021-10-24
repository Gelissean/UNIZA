from KrypBz.proj3.square_generator import square_generator
from KrypBz.tools.char_ops import coincidence_index_comparison, move_char
from KrypBz.tools.cipher_tools import convert
from KrypBz.tools.file_tools import get_file_paths, read_file, convert_to_ascii, write_to_file
from KrypBz.tools.coincidence_indeces import coincidence_indeces


def translate(ciphered, a, b, m, x0, buffer_size=100):
    generator = square_generator(a, b, m, x0)
    retval = ""
    buffer = ""
    i = 0
    for c in ciphered:
        buffer += move_char(c, -generator.get_actual(), 26)
        generator.generate_next()
        i += 1
        if i >= buffer_size:
            retval += buffer
            buffer = ""
            i = 0
    retval += buffer
    return retval


def brute_force(subor, a, b, m, epsilon, keys):
    original = read_file(subor)
    ciphered = convert_to_ascii(original)
    #TODO po poslednu / #folder_path = subor.get_path
    for i in range(88888,m):
        attempt = translate(ciphered, a, b, m, i)
        for index in keys:
            if coincidence_index_comparison(attempt, 26, coincidence_indeces.get(index)) <= epsilon:
                #write_to_file(convert(original, attempt), folder_path + '/' + index + '_' + str(i))
                write_to_file(convert(original, attempt), "./cv4/" + index + '_' + str(i))


def prudova(cesta, a, b, m, epsilon, keys):
    subory = get_file_paths(cesta)
    subory = ["./cv4/sprava_enc.txt"]
    for subor in subory:
        print("Analysing file: \t" + str(subor))
        brute_force(subor, a, b, m, epsilon, keys)
    print("Done")


if __name__ == '__main__':
    keys = ["sk", "en"]
    prudova("./cv4/", 8121, 28411, 134456, 0.005, keys)
