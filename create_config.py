import json


def create_config(file_name: str):
    with open(file_name, "r") as file:
        esper_output = []
        for line in file.readlines():
            esper_name = line.split(":")[0]
            name, alternative = esper_name.split("-")
            values = line.split(":")[1].split(" ")[0]
            if len(values.split(",")) != 8:
                print(name)
                return

            story, cube, kronos, apep, fafnir, tower, war_def, war_atk = [int(value) for value in values.split(",")]
            esper_class = line.split(":")[1].split(" ")[1].replace("\n", "")
            esper_output.append({
                "name": name,
                "alternative": alternative,
                "story": story,
                "cube": cube,
                "kronos": kronos,
                "apep": apep,
                "fafnir": fafnir,
                "tower": tower,
                "war_def": war_def,
                "war_atk": war_atk,
                "class": esper_class
            })

        with open("config.json", "w+") as file:
            file.write(json.dumps({"espers": esper_output}))


if __name__ == "__main__":
    create_config("info.txt")
