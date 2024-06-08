import yaml
from utils.YamlUtil import YamlReader

# with open('data.yml', 'r', encoding='utf-8') as f:
#     r = yaml.safe_load_all(f)
#     for doc in r:
#         if 'ppv3_2' in doc:
#             print(doc['ppv3_2']['client_id'])
#             break

# res = YamlReader()
res = YamlReader("./config/config.yml").read()
print(res)

