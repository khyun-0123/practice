text_list = input()
find = input()
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result_list = []

for i in range(len(text_list)):
    if text_list[i] in num_list:
        continue
    else:
        result_list.append(text_list[i])

result_list = ''.join(result_list)

if find in result_list:
    print(1)
else:
    print(0)