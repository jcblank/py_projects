names = {}
#Defines the dictionary
names['JCB'] = 'João Carlos'
names['CAR'] = 'Carlos'
names['BLA'] = 'Blankenheim'
sentence = 'JCB' + ' is a men. ' + 'CAR' + ' is a woman. ' 
translate = names.get('JCB') + ' is a men ' + names.get('CAR') + ' is a woman.'
#takes just the value of the index
definition = names.get('JCBA')
#deletes the entry in the dictionary
#del names['CAR']
''' 
if definition:
    print(definition)
else:
    print("Name doesn't exist!")
'''
print(sentence)
print(translate)
