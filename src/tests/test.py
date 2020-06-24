from src.networks.file_reader import FileReader
from ..networks.random_stn import RandomSTN
class Test:
    def __init__(self, samples):
        self.networks = []
        if type(samples) == int:
            self.networks = RandomSTN().random_stns(samples, 10)
        else:
            self.samples = samples
            for sample in samples:
                reader = FileReader()
                self.networks.append(reader.read_file(sample))
        self.test()

    def test(self):
        pass
