import os
import yaml


local_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.dirname(local_path)


class Config:
    def __init__(self):
        self.file_path = os.path.join(root_path, 'running', 'conf.yml')

    def get(self, module, key):
        with open(self.file_path, "r", encoding="utf-8") as f:
            yaml_data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return yaml_data[module][key]

    def get_common(self, key):
        return self.get('common', key)

    def get_api(self, key):
        return self.get('api', key)

    def get_app(self, key):
        return self.get('app', key)

    def get_web(self, key):
        return self.get('web', key)

    def set(self, module, key, value):
        with open(self.file_path, "r", encoding="utf-8") as f:
            yaml_data = yaml.load(f.read(), Loader=yaml.FullLoader)
        yaml_data[module][key] = value
        with open(self.file_path, 'w', encoding="utf-8") as f:
            yaml.dump(yaml_data, f)

    def set_dict(self, module, data):
        with open(self.file_path, "r", encoding="utf-8") as f:
            yaml_data = yaml.load(f.read(), Loader=yaml.FullLoader)
        yaml_data[module] = data
        with open(self.file_path, 'w', encoding="utf-8") as f:
            yaml.dump(yaml_data, f)

    def set_common(self, key, value):
        self.set('common', key, value)

    def set_common_dict(self, data):
        self.set_dict('common', data)

    def set_app(self, key, value):
        self.set('app', key, value)

    def set_app_dict(self, data):
        self.set_dict('app', data)

    def set_web(self, key, value):
        self.set('web', key, value)

    def set_web_dict(self, data):
        self.set_dict('web', data)


config = Config()

if __name__ == '__main__':
    pass










