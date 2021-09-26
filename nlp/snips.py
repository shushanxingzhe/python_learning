import io
import json
from snips_nlu import SnipsNLUEngine


with io.open("./sample_dataset.json") as f:
    sample_dataset = json.load(f)

nlu_engine = SnipsNLUEngine()
nlu_engine.fit(sample_dataset)

parsing = nlu_engine.parse("What will be the weather in San Francisco next week?")
print(json.dumps(parsing, indent=2))
