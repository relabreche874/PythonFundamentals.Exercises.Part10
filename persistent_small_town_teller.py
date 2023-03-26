import pickle
class PersistentUtils:
    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data