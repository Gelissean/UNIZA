class Dataset:
    def __init__(self, path_data, path_labels):
        self.rows = None
        self.columns = None
        self.size = None
        self.ins = None
        self.outs = None
        self.read_ins(path_data)
        self.read_outs(path_labels)

    def read_ins(self, path_data):
        with open(path_data, "rb") as f:
            bytes_read = f.read()
        test = int.from_bytes(bytes_read[0:4], byteorder="big", signed=False)
        self.size = int.from_bytes(bytes_read[4:8], byteorder="big", signed=False)
        self.rows = int.from_bytes(bytes_read[8:12], byteorder="big", signed=False)
        self.columns = int.from_bytes(bytes_read[12:16], byteorder="big", signed=False)
        ins = []
        step_size = self.rows * self.columns
        offset = 16
        steps = (len(bytes_read)-offset)//step_size
        assert (len(bytes_read)-offset) % step_size == 0
        for i in range(steps):
            ins.append([b/255 for b in bytes_read[offset + i * step_size : offset + (i + 1) * step_size]])
        self.ins = ins

    def read_outs(self, path_labels):
        with open(path_labels, "rb") as f:
            bytes_read = f.read()
        test = int.from_bytes(bytes_read[0:4], byteorder="big", signed=False)
        size = int.from_bytes(bytes_read[4:8], byteorder="big", signed=False)
        outs = []
        for b in bytes_read[8:]:
            outs.append([b])
        self.outs = outs