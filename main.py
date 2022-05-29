from os import path
from configuration import Config


if __name__ == '__main__':
    abs_path = path.abspath("config.json")
    config = Config(abs_path)
    print(set([config.get_esper("q"), config.get_esper("eros")]))
