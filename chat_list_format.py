#將聊天紀錄格式化存於清單

lines = []
line_list = []
i = 0
limit = 0
chat_form = []

with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())


print('原始數據：')
for l in lines:
	msg = ''
	line_list = l.split()
	print(line_list)
	time = line_list[0][:5]
	name = line_list[0][5:]
	for i in range(1,len(line_list)):
		msg += line_list[i]

	chat_form.append([time, name, msg])

print('')
print('格式化後數據：')
for line_form in chat_form:
	print(line_form)