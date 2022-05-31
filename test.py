import ocr
from configuration import Config
from models import Stats
from espers import calc_stats
import markdown
from utils import ESPER_MAPPING as MAPPING

if __name__ == "__main__":
    config = Config("config.json")
    espers = config.espers

    for esper in espers:
        print(markdown.markdown(f"""
# {esper.name} - {esper.alternative}

*Ruolo*: {esper.esper_class.name}

*Descrizione*: 

_Tier List_:

- *Story*: {MAPPING[esper.story]}
- *Cube*: {MAPPING[esper.cube]}
- *Kronos*: {MAPPING[esper.kronos]}
- *Apep*: {MAPPING[esper.apep]}
- *Fafnir*: {MAPPING[esper.fafnir]}
- *War Attack*: {MAPPING[esper.war_atk]}
- *War Defense*: {MAPPING[esper.war_def]}


"""))