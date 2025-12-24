import glob                                                 #finds all detections rules
import sys                                                  #load detections definitions
import yaml                                                 #enforce deteciton standards
import json
from jsonschema import validate, ValidationError            #fail CI if something is wrong

DETECTION_CODE = "Detections/**/*.yml"
SCHEMA_PATH = "Schemas/Schema1.json"

with open(SCHEMA_PATH,"r") as schema_file:
    schema = json.load(schema_file)

errors_found = False

for rule_file in glob.glob(DETECTION_CODE, recursive=True): #find all detection rules
    with open(rule_file,"r") as f:                          #open each rule
        rule = yaml.safe_load(f)                            #load each rule
    try: 
        validate(instance=rule,schema=schema)               #validate each rule found in Detections folder
    except ValidationError as e:                            #if validation fails, print error
        print(f"Validation error in {rule_file}: {e}")
        print(f"{e.message}")
        errors_found = True

if errors_found:                                            #if any errors were found, exit with error
    sys.exit(1)
else:
    print("All rules are valid.")                           #if no errors were found, exit with success


