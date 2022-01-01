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
	line_list = []
	line_load = []
	for line in chat_list:
		line_list = line.split()
		if len(line_list) > 1:
			if name == line_list[1]: 
				if name == 'Chow':
					if len(line_list) < 3:
						continue
					chat.append(line_list[2]) 
				else:
					if len(line_list) < 4:
						continue
					chat.append(line_list[3]) 
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

	result.append(['名字', chat_list[len(chat_list) - 1]])
	result.append(['字數', msg_count])
	result.append(['語音', voice_count])
	result.append(['貼圖', sticker_count])
	return result

# 列印分析結果
def printer(result_list=[], session=0):
	print('')
	if session == 1:
		for line in result_list:
			print(line[0],': ', line[1], sep = '')
	elif session == 2:
		msg = ''
		for line in result_list:
			if ('[照片]' in line) or ('[語音訊息]' in line) or ('[貼圖]' in line) or ('[檔案]' in line):
				continue

			print(line)

# 選單狀態 return(int)
def input_menu():
	choice = 0
	print('1.聊天內容分析')
	print('2.顯示指定對象聊天內容')
	print('0.離開程式')
	while True:
		choice = input('請選擇：')
		if (choice == '0') or (choice == '1') or (choice == '2'):
			return choice


def main():
	filename = 'LINE.txt'
	while True:
		choice = int(input_menu())
		if choice == 1:
			name = input('name:')
			chat_list = read_file('LINE.txt')
			name = real_name(chat_list, name)
			indi_chat_list = indi_chat(chat_list, name)
			result = counter(indi_chat_list)
			printer(result, choice)
			print('\n')

		elif choice == 2:
			name = input('name:')
			chat_list = read_file('LINE.txt')
			name = real_name(chat_list, name)
			indi_chat_list = indi_chat(chat_list, name)
			printer(indi_chat_list, choice)
			print('\n')
		elif choice == 0:
			print('程式結束！')
			break

main()