# Constructingn data hierarchies and convert them to string representations is called, "serializing"
# Reconstructing the data from the string representation is called, "deseiralizing"

import json
from json.decoder import JSONDecodeError

f = open('workfile', 'r+')

try:
    z = json.load(f)    # Decode the object again
    for line in z:
        print(line, end='')
except JSONDecodeError:
    pass

obj = [1, 'simple', 'list']
x = json.dumps(obj)     # view object in its JSON string representation     
print('object:', x)
print('serialized:', json.dump(obj, f))     # serializes the object to a text file

print('=== File Content ===')
f.seek(0)   # set the file object position to the beginning of the file
for line in f:
    print(line, end='')


print()
f.close()
print('Filed closed successfully?:', f.closed)