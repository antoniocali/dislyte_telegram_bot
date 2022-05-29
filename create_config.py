import json


def create_config(file_name: str):
    with open(file_name, "r") as file:
        esper_output = []
        for line in file.readlines():
            esper_name = line.split(":")[0]
            name, alternative = esper_name.split("-")
            values = line.split(":")[1].split(" ")[0]
            if len(values.split(",")) != 8:
                print("error", line)
            story, cube, kronos, apep, fafnir, tower, war_atk, war_def = values.split(",")
            esper_class = line.split(":")[1].split(" ")[1]
            print(name, alternative, story, cube, kronos, apep, fafnir, tower, war_atk, war_def, esper_class)


if __name__ == "__main__":
    create_config("info.txt")
