
N = int(input())

temp = list(map(str, input().split("/")))
temp.pop(0)
stack = []

for new_item in temp:
    if new_item == ".":
        pass
    elif new_item == "..":
        if stack:
            stack.pop()
    else:
        stack.append(new_item)

if stack:
    print("/" + '/'.join(stack))
else:
    print("/")