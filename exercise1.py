#!/usr/bin/python
import json
import operator
import yaml

exercise1 = open('exercise1_input','r',encoding='utf-8')
json_string = exercise1.read()

datastore = json.loads(json_string)
ages_dict = datastore ["ppl_ages"]
buckets_list = datastore ['buckets']

max_age = max(ages_dict.items(), key=operator.itemgetter(1))[1]
max_age += 1
buckets_list+=[0,max_age]
buckets_list.sort()
buckets_counter = len(buckets_list)

keystring = "{0} - {1}"
result = {}

for i in range(1,buckets_counter):
    val = [""]
    dictkey = keystring.format(buckets_list[i-1],buckets_list[i])
    for name in ages_dict:
        if buckets_list[i-1] < ages_dict[name]<buckets_list[i]:
            val.append(':'+name)
    result[dictkey] = val

with open('result', 'w') as yaml_file:
    yaml.dump(result, yaml_file, default_flow_style=False,encoding='utf-8')





