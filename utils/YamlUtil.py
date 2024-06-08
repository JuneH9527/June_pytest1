import os
import yaml


class YamlReader:
    def __init__(self, yamlfile):
        self._data = None
        self._data_all = None
        if os.path.exists(yamlfile):
            self.yamlfile = yamlfile
        else:
            raise FileNotFoundError('文件不存在！')

    def read(self):
        if not self._data:
            with open(self.yamlfile, 'rb') as f:
                self._data = yaml.safe_load(f)
        return self._data

    def read_all(self):
        with open(self.yamlfile, 'rb') as f:
            self._data_all = dict(yaml.safe_load_all(f))
        return self._data_all
