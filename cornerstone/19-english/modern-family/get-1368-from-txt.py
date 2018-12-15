import re

file = "1368.txt"

with open(file, encoding='utf-8') as f:
	read_data = f.read()

# print(read_data)
# print(type(read_data)) # str 

words = re.findall("[a-zA-Z.]+", read_data)
# print(words)
# print(len(words))

word_list = ""
for word in words:
	word_list += word + "\n"
# print(word_list)


output_file_path = "1368-word-list.txt"

with open(output_file_path, mode="w", encoding="utf-8") as f2:
	f2.write(word_list)