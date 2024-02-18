from wata.file.utils import utils

class FileProcess:
    @staticmethod
    def load_yaml(path):
        return utils.load_yaml(path)

    @staticmethod
    def write_yaml(data, save_path):
        utils.write_yaml(data, save_path)

    @staticmethod
    def load_json(path):
        return utils.load_json(path)

    @staticmethod
    def write_json(data, save_path):
        utils.write_json(data, save_path)

    @staticmethod
    def load_pkl(path):
        return utils.load_pkl(path)

    @staticmethod
    def write_pkl(data, save_path):
        utils.write_pkl(data, save_path)

    @staticmethod
    def load_txt(path):
        return utils.load_txt(path)

    @staticmethod
    def write_txt(data, save_path):
        utils.write_pkl(data, save_path)
