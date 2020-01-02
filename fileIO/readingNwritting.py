"""
    'r': when file is read-only
    'w': for writing only
    'a': opens the file for appending; any data written to the file is added to the end automatically
    'r+': opens the file for both reading and writing

    f.tell(): returns an integer giving the file object's current position in the file represented
              as number of bytes from the beginning of the file when in binary mode 
              and opaque number when in text mode
    f.seek(offset, whence): changes the file object's position
"""


f = open('workfile', 'r+')
# with open('workfile') as f:
#     read_data = f.read()
#     # print(read_data)
#     read_data_by_line = f.readline()
#     # print(read_data_by_line)

f.write('This is a test\n')     # returns the number of characters written

# This is memory efficient, fast, and leads to simple code
for line in f:
    print(line, end=' ')

f.close()
print('Is file closed safely?:', f.closed)

