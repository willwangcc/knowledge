"""
src -> markdown 
"""

import argparse

def clean(word):
	return word.strip(",!.?-").lower() 

def txt2hashmap(file):
	"""
	file: str
	r: word_map {word: []} d
	"""
	word_map = {}
	with open(file, encoding='utf-8') as f:
		read_data = f.read()
	word_list  = read_data.strip("").split("\n")
	for word in word_list:
		if word != "":
			word_map[word] = []
	return word_map 	

def src2md(file):
	script_path = file
	directory = "/".join(script_path.split("/")[:-1])
	name = script_path.split("/")[-1].strip(".srt")
	# print(name)

	with open(script_path, encoding='utf-8') as f:
		read_data = f.read()

	block = read_data.split("\n\n") 

	# print(block[11]) # 
	"""
	Output: 
	23
	00:00:01,530 --> 00:00:03,740
	真想知道曼尼现在在做什么
	I wonder what Manny's doing right now.
	"""
	word_map = txt2hashmap("/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/modern-family/1368-word-list.txt")


	markdown = "# " + name + "\n"

	title = """
| Number  | Timeline  | Chinese  | English  | 
| :-------- | :---------: | :---------: | :---------: | 
"""

	occur_word = set()
	lines_map = {}
	lines = block[11:]
	for line in lines:
		group = line.split("\n")
		if len(group) != 4: continue 
		index, timeline, chinese, english = line.split("\n")
		words = english.split(" ")
		for word in words:
			word = clean(word)
			if word in word_map:
				occur_word.add(word)
				word_map[word].append(index) 
		lines_map[index] = line 
	# print(lines_map)

	markdown += "\n" + "## 出现的单词 " + "\n\n" + str(occur_word) + "\n\n"

	word_count = 0 
	for key, val in word_map.items():
		if len(val) >= 1:
			word_count += 1
			cur_table = "## "  + key + "\n"
			cur_table += title
			# print(val)
			for i in val:
				line = lines_map[i]
				index, timeline, chinese, english = line.split("\n")
				english = english.replace(key, "<b>" + key + "</b>")
				cur_table += "|" + index + "|" + timeline + "|" + chinese + "|" + english + "|" + "\n"
			markdown += cur_table
			markdown += "\n"

	markdown += "\n"
	markdown += "1368中一共出现了" + str(word_count) + "个单词" + "\n\n"


	authors = block[2:7]
	for i in authors:
		author = i.split("}")[-1]
		markdown += "* " + author + "\n"

	output_file_path = directory + "/" + "1368" + name + ".md"

	with open(output_file_path, mode="w", encoding="utf-8") as f2:
		f2.write(markdown)
	return markdown


file = "/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/modern-family/Modern.Family.S09E06.srt"
print(src2md(file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", nargs = 1, help="src to markdown")
    args = parser.parse_args()
    if args.file:
    	src2md(args.file[0])

