from models import Esper, Stats


def normalize(score: int) -> str:
    return "{:.2f}".format((score / 5.0) * 10 / 15)


def calc_stats(espers: Stats) -> str:
    return f"""
*Story*: {normalize(espers.story)} - _Peggiore_: {espers.get_worse('story').name}
*Cube*: {normalize(espers.cube)} - _Peggiore_: {espers.get_worse('cube').name}
*Kronos*: {normalize(espers.kronos)} - _Peggiore_: {espers.get_worse('kronos').name}
*Apep*: {normalize(espers.apep)} - _Peggiore_: {espers.get_worse('apep').name}
*Fafnir*: {normalize(espers.fafnir)} - _Peggiore_: {espers.get_worse('fafnir').name}
*War Attack*: {normalize(espers.war_atk)} - _Peggiore_: {espers.get_worse('war_atk').name}
*War Defense*: {normalize(espers.war_def)} - _Peggiore_: {espers.get_worse('war_def').name}

*Distribuzione Classi*
{' - '.join([f'{key}: {value}' for key, value in espers.get_classes().items()])}
    """
