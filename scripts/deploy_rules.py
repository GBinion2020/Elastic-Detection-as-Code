import os
import requests
import json
import glob

KIBANA_URL = os.getenv("KIBANA_URL")
KIBANA_API_KEY = os.getenv("KIBANA_API_KEY")

if not KIBANA_URL or not KIBANA_API_KEY:
    print("Error: KIBANA_URL or KIBANA_API_KEY not set.")
    sys.exit(1)

headers = {
    "Authorization": f"ApiKey {KIBANA_API_KEY}",
    "kbn-xsrf": "true",
    "Content-Type": "application/json"
}

DETECTION_PATH = "detections/**/*.yml"                              #find all detection rules in detection folder

for rule_file in glob.glob(DETECTION_PATH, recursive=True):         #finds all detection rules
    with open(rule_file, "r") as f:                                 #open each rule
        rule = yaml.safe_load(f)                                    #load each rule
        response = requests.post(                                   #deploy each rule  
            f"{KIBANA_URL}/api/detection_engine/rules",             #Kibana API endpoint
            headers=headers,
            json=rule,
            verify=False
        )
        
        if response.status_code not in (200,201):                   #if deployment fails, print error
            print(f"Failed to deploy rule {rule_file}: {response.status_code}")
            sys.exit(1)
        else:                                                       #if deployment is successful, print success
            print(f"Successfully deployed rule {rule_file}")
