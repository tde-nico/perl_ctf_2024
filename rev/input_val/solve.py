from z3 import *


LEN = 34
flag = [BitVec(f'chr_{i}', 32) for i in range(LEN)]

s2 = "oF/M5BK_U<rqxCf8zWCPC(RK,/B'v3uARD"
s2 = [ord(s2[i]) for i in range(LEN)]
array2 = [ 1102, 1067, 1032, 1562, 1612, 1257, 1562, 1067, 1012, 902, 882, 1397, 1472, 1312, 1442, 1582, 1067, 1263, 1363, 1413, 1379, 1311, 1187, 1285, 1217, 1313, 1297, 1431, 1137, 1273, 1161, 1339, 1267, 1427 ]


s = Solver()

array = [None] * LEN

for i in range(LEN):
	array[i] = s2[i] ^ flag[i]

for j in range(LEN):
	array[j] -= s2[33 - j]

array3 = [None] * LEN

for k in range(17):
	array3[k] = array[1 + k * 2] * 5
	array3[k + 17] = array[k * 2] * 2

for l in range(LEN):
	array3[l] += 1337

for n2 in range(LEN):
	s.add(array3[n2] == array2[n2])

if s.check() == sat:
	m = s.model()
	print(''.join([chr(m[flag[i]].as_long()) for i in range(LEN)]))

# pearl{w0w_r3v3r51ng_15_50_Ea5y_!!}
