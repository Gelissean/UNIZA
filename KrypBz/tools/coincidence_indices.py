class coincidence_indices:
    @staticmethod
    def get(key):
        indeces = coincidence_indices.get_all()
        if key in indeces:
            return indeces[key]
        else:
            raise NotImplementedError

    @staticmethod
    def get_all():
        indices = {
            "sk": [0.1142, 0.0135, 0.0305, 0.0501, 0.0801, 0.0130, 0.0020, 0.0200, 0.0816, 0.0180, 0.0466, 0.0300,
                   0.0406, 0.0741, 0.0931, 0.0205, 0.0000, 0.0491, 0.0531, 0.0496, 0.0441, 0.0361, 0.0000, 0.0005,
                   0.0195, 0.0200],
            "en": [0.0780, 0.0149, 0.0474, 0.0383, 0.1137, 0.0208, 0.0172, 0.0479, 0.0833, 0.0015, 0.0058, 0.0292,
                   0.0275, 0.0655, 0.0716, 0.0354, 0.0006, 0.0684, 0.0690, 0.1000, 0.0228, 0.0096, 0.0102, 0.0009,
                   0.0199, 0.0006]}
        return indices


    @staticmethod
    def get_all_power():
        indices = coincidence_indices.get_all()
        result = {}
        for key in indices:
            temp = 0
            for i in indices[key]:
                temp += pow(i, 2)
            result[key] = temp
        return result
