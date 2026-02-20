import yaml
import os

class Config:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            with open("config.example.yml") as f:
                with open(path, "w") as out:
                    out.write(f.read())
        self.load()

    def load(self):
        with open(self.path) as f:
            self.data = yaml.safe_load(f)

    def save(self):
        with open(self.path, "w") as f:
            yaml.dump(self.data, f)
