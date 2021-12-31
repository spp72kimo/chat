import os

# 讀取檔案 return(list)
def read_file(filename):
	all_chat = []

	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			all_chat.append(line)
		return all_chat

# 介面轉換 return(list)
def conveter(chat_list=[]):
	all_chat = []
	name = ''
	for line in chat_list:
		if ('Allen' in line) or ('Tom' in line):
			name = line.strip()
			continue
		chat = line.strip()
		all_chat.append(name + '：' + chat + '\n')
	return all_chat

# 寫入檔案
def write_file(filename,chat_list=[]):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in chat_list:
			f.write(line)

def main():
	in_filename = 'input.txt'
	out_filename = 'ooo.txt'
	
	# 也可以這樣寫
	#write_file(out_filename, conveter(read_file(in_filename)))

	list_origin = read_file(in_filename)
	list_convert = conveter(list_origin)
	write_file(out_filename, list_convert)

main()