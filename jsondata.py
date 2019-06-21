import json


#json.load and json.dump for file
with open('states.json') as file:
    data = json.load(file)
    print(type(data))
    print(data)
    print(type(data['states']))
    print(data['states'])

    count = 0
    for state in data['states']:
        # print(state)
        del state['area_codes']
        count += 1
    print('States Count:', count)

    with open('new_states.json', 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)


print('Hiiiii, Yogesh')


# jsondata = '''{
#   "accounting": [
#     {
#       "firstName": "John",
#       "lastName": "Doe",
#       "age": 23,
#       "gender-male": true
#     },
#     {
#       "firstName": "Mary",
#       "lastName": "Smith",
#       "age": 32,
#       "gender-male": false
#     }
#   ]
# }'''
#
#json.loads and json.dumps for string
# data = json.loads(jsondata)
# print(type(data))
# print(data)
# print(type(data['accounting']))
#
# for dt in data['accounting']:
#     print(dt)
#     print(dt['firstName'])
#
# newdt = json.dumps(data, indent=2, sort_keys=True)
# print(type(newdt))
# print(newdt)
