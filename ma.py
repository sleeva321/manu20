str=raw_input()
x = ""
for i in str:
	if i not in x:
		x = x + i
print x
