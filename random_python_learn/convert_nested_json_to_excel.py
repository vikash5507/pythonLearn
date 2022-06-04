import json
import pandas as pd

NESTED_JSON_FILE_PATH = "/Users/vikash/PycharmProjects/pythonLearn/sense_related/ATS_based_entity_relation/All_Agencies/all_count_report_standard_ats_wise.json"

with open(NESTED_JSON_FILE_PATH, 'r') as f:
    data = json.load(f)


data_parsed = []
for k, v in data.items():
    for k1, v1 in v.items():
        for k2, v2 in v1.items():
            temp = {
                'From_Standard_Entity': k,
                'To_Standard_Entity': k1,
                'relation_name': k2,
            }
            for k3, v3 in v2.items():
                temp[k3] = v3
            data_parsed.append(temp)
print(data_parsed)

df = pd.DataFrame(data_parsed).set_index(
    'From_Standard_Entity')  # set_index() optional
df.to_excel('/Users/vikash/Desktop/ats_wise_relation_name.xlsx')
