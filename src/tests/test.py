from src.networks.file_reader import FileReader

class Test:
    def __init__(self, samples):
        self.networks = []
        self.samples = samples
        for sample in samples:
            reader = FileReader()
            self.networks.append(reader.read_file(sample))
        self.test()
        
    def test(self):
        pass
