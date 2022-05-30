from models import Esper, Stats


def normalize(score: int) -> str:
    return "{:.2f}".format((score / 5.0) * 10 / 15)


def calc_stats(espers: Stats) -> str:
    return f"""
*Story*: {normalize(espers.story)}
*Cube*: {normalize(espers.cube)}
*Kronos*: {normalize(espers.kronos)}
*Apep*: {normalize(espers.apep)}
*Fafnir*: {normalize(espers.fafnir)}
*War Attack*: {normalize(espers.war_atk)}
*War Defense*: {normalize(espers.war_def)}
    """
