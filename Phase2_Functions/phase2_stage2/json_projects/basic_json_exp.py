#May 22 Basic JSON Example 19:12 

import json

data = {
    "name" : "Tamaghna",
    "age" : 28
}

#Save JSON
with open("Phase2_Functions/phase2_stage2/json_projects/data.json", "w") as file:
    json.dump(data,file,indent=4)

#Load JSON
with open("Phase2_Functions/phase2_stage2/json_projects/data.json", "r") as file:
    loaded_data=json.load(file)

print(loaded_data)