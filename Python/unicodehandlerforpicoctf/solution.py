from unihandecode import Unihandecoder

flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
data1 = Unihandecoder(lang='zh')
strng = ''
for d in flag:
    strng += data1.decode(d)
flag = strng 

# print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i])) for i in range(0, len(flag), 2)]))

for d in flag:
    total = ord(d)
    print(chr(total))

