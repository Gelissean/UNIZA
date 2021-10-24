import os

from KrypBz.proj3.square_generator import square_generator
from KrypBz.tools.char_ops import coincidence_index_comparison, move_char, coincidence_index
from KrypBz.tools.cipher_tools import convert
from KrypBz.tools.file_tools import get_file_paths, read_file, convert_to_ascii, write_to_file, make_directory
from KrypBz.tools.coincidence_indices import coincidence_indices


def translate(ciphered, a, b, m, x0, buffer_size=100):
    generator = square_generator(a, b, m, x0)
    retval = []
    for c in ciphered:
        retval.append(move_char(c, -int(26 * generator.get_actual()), 26))
        generator.generate_next()
    return ''.join(retval)


def brute_force(subor, cesta_ciel, a, b, m, epsilon):
    original = read_file(subor)
    ciphered = convert_to_ascii(original)
    original_indices = coincidence_indices.get_all_power()
    head, tail = os.path.split(subor)
    cesta = cesta_ciel + '/' + tail
    make_directory(cesta)
    for i in range(m):
        attempt = translate(ciphered, a, b, m, i)
        coinc_index = coincidence_index(attempt, 26)
        for key in original_indices:
            if abs(coinc_index - original_indices[key]) <= epsilon:
                write_to_file(convert(original, attempt), cesta + '/' + key + '_' + str(i) + '.txt')


def prudova(cesta_zdroj, cesta_ciel, a, b, m, epsilon):
    subory = get_file_paths(cesta_zdroj)
    for subor in subory:
        print("Analysing file: \t" + str(subor))
        brute_force(subor, cesta_ciel, a, b, m, epsilon)
    print("Done")


if __name__ == '__main__':
    # prudova("./cv4", "./cv4", 8121, 28411, 134456, 0.01)  # stream cipher
    prudova("./sifrovane", "./desifrovane", 84589, 45989, 217728, 0.01)  # stream cipher
