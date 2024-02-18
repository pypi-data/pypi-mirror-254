



import pexpect
SCRIPT = "python3 script.py"

output = []

p = pexpect.spawn (SCRIPT)
while not p.eof ():
	line = p.readline ()	
	output.append (line)
	print (line)
	
print (output)

