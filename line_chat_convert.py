import os

# 讀取檔案 return(list)
def read_file(filename):
	all_chat = []

	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			all_chat.append(line)
		return all_chat

# 寫入檔案
def write_file(filename, chat_list=[]):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in chat_list:
			f.write(line)

#確認名字 return(str)
def real_name(chat_list=[], key_name=''):
	chat_line = []
	for line in chat_list:
		chat_line = line.split()
		if len(chat_line) >= 3:
			if key_name in chat_line[1]:
			 	return (chat_line[1])

# 整理個人對話資料 return(list)
def indi_chat(chat_list=[], name=None):
	if name == None:
		print('沒有設定名字')
		return
	chat = []
	line_load = []
	for line in chat_list:
		if name in line:
			line_load = line.split()
			chat.append(line_load[3:])
		chat.append(name)
	return chat

# 次數分析 return(list)
def counter(chat_list=[]):
	result = []
	msg_count = 0
	pic_count = 0
	voice_count = 0
	sticker_count = 0

	for line in chat_list:
		if '[照片]' in line:
				pic_count += 1
		elif '[語音訊息]' in line:
				voice_count += 1
		elif '[貼圖]' in line:
				sticker_count += 1
		else:	
			msg_count += len(line)

	result.append(['name', chat_list[len(chat_list) - 1]])
	result.append(['msg', msg_count])
	result.append(['voice', voice_count])
	result.append(['sticker', sticker_count])
	return result

# 列印分析結果
def printer(result_list=[]):
	print('')
	for line in result_list:
		print(line[0],': ', line[1], sep = '')



def main():
	filename = 'LINE.txt'
	name = input('name:')
	chat_list = read_file('LINE.txt')
	name = real_name(chat_list, name)
	indi_chat_list = indi_chat(chat_list, name)
	result = counter(indi_chat_list)
	printer(result)

main()