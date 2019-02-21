#!/usr/bin/python
import json
import operator
#import yaml
ex1 = open('Ex1_input','r',encoding='utf-8')
json_string = ex1.read()

datastore = json.loads(json_string)
#print(datastore)
ages_dict = datastore ["ppl_ages"]
buckets_list = datastore ['buckets']
#print(ages_dict['Dan'])
#print(buckets_list)


max_age = max(ages_dict.items(), key=operator.itemgetter(1))[1]
max_age += 1
#print(max_age)
buckets_list+=[0,max_age]

buckets_list.sort()
buckets_counter = len(buckets_list)
#print(buckets_list,buckets_counter)

fo = open('tempfile','w')
for i in range(1,buckets_counter):
#    line1 = buckets_list[i-1]+'-'+ buckets_list[i]
    print(buckets_list[i-1],'-',buckets_list[i],':')
#    fo.write(line1)
    for key in ages_dict:
        if buckets_list[i-1] < ages_dict[key]<buckets_list[i]:
#            line2 = '- :'+key+ages_dict[key]
            print('- :',key,ages_dict[key])

fo.close()

