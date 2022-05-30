import ocr
from configuration import Config
from models import Stats
from espers import calc_stats

if __name__ == "__main__":
    config = Config("config.json")
    stats = Stats([config.get_esper("Q"), config.get_esper("HengYue"), config.get_esper("Lewis")])
    print(stats.get_worse("war_def"))
    print(stats.classes)
    print(stats.get_classes())

    print(calc_stats(stats))