def check(a,b):
	if (a=='(' and b==')') or (a=='{' and b=='}') or (a=='[' and b==']'):
		return 0
	else:
		return 1
input="({[]}))"
x=list(input)
stack=[]
for brac in x:
	if not stack or check(stack[-1],brac):
		stack.append(brac)
	else:
		stack.pop()
  
if not stack:
    print("Balanced")

