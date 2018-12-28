"""
Plan:
IPA transcription: 
	https://rapidapi.com/katspaugh/api/ipa-transcription
	https://github.com/mphilli/English-to-IPA
"""

import argparse
import collections 
import re

class NOTE:

	def __init__(self, src):
		self.lines_map = {} #  index: [timeline, chinese, english]
		self.words_map = {} #  word: set(index1, index2)
		self.base_words_set = set()
		self.all_words_map = collections.defaultdict(int)
		self.output_name = None 
		self.directory = None 
		self.toefl_words_set = set()

		vocabulary_path = "/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/modern-family/vocabulary/"
		base_txt = vocabulary_path + "1368-word-list.txt"
		toefl_txt = vocabulary_path + "toefl.txt"
		self.words_txt = vocabulary_path + "words.txt"

		self.lines_map, self.words_map, self.output_name, self.directory = self.src2lines_word(src)
		self.base_words_set = self.txt2base_word(base_txt)
		self.toefl_words_set = self.txt2toefl_word(toefl_txt)
		self.all_words_map = self.txt2all_words_map(self.words_txt)

		self.table_title = """
| Number  | Timeline  | Chinese  | English  | 
| :-------- | :---------: | :---------: | :---------: | 
"""

###########
	def read_file(self, file):
		"""
		file: txt 
		r: [str]
		r: str 
		"""
		script_path = file
		directory = "/".join(script_path.split("/")[:-1])
		name = script_path.split("/")[-1].strip(".srt")
		# print(name)

		with open(script_path, encoding='utf-8') as f:
			read_data = f.read()

		block = read_data.split("\n\n") 
		return block, name, directory

		 
	def is_valid_group(self, group):
		"""
		group: [str]
		---
		toDo: flexible for future change 
		"""
		return len(group) == 4


	def clean(self, word):
		"""
		word: str
		r: str 
		"""
		return word.strip('",!.?-').lower() 


	def merge2sentence(self, content):
		"""
		content: [[str, str]]
		r: Chinese: str
		r: English: str 
		"""
		Chinese, English = "", ""
		for a, b in content:
			Chinese += a + " "
			English += b + " "
		return Chinese, English


	def is_end(self, english):
		"""
		english: str
		r: Boolean
		"""
		if english[-1] in (".", "!", "?"):
			return True 
		return False 


	def is_word(self, word):
		"""
		word: str 
		r: Boolean
		"""
		pattern = r'[a-zA-Z-\']+'
		if re.match(pattern, word) == None:
			return False 
		return True 


	def src2lines_word(self, src):
		"""
		!!!
		src: txt
		r: lines_map: {str:[str, str, str]}
		r: words_map: {str:set}
		r: name: str
		r: directory: str 
		"""
		lines_map, words_map = {}, collections.defaultdict(set)
		block, name, directory = self.read_file(src)
		# print(block[11]) # 
		"""
		Output: 
		23
		00:00:01,530 --> 00:00:03,740
		真想知道曼尼现在在做什么
		I wonder what Manny's doing right now.
		"""
		start = 0
		lines = block[start:] # get rid of what is not lines
		position, content = [], [] 
		for i, line in enumerate(lines):
			group = line.split("\n")
			if not self.is_valid_group(group):
				continue
			index, timeline, chinese, english = group
			if not position:
				position = [index, timeline]
			content.append([chinese, english])

			words = english.split(" ")
			for word in words:
				word = self.clean(word)
				if self.is_word(word):
					words_map[word].add(position[0])

			if self.is_end(english):
				Chinese, English = self.merge2sentence(content)
				lines_map[position[0]] = [position[1], Chinese, English]
				position = []
				content = []

		return lines_map, words_map, name, directory


###########
	def txt2base_word(self, file):
		"""
		file: 1368.txt
		r: base_words_set: set()
		"""
		base_words_set = set()
		with open(file, encoding='utf-8') as f:
			read_data = f.read()
		word_list  = read_data.strip("").split("\n")
		for word in word_list:
			if word != "":
				base_words_set.add(word)
		return base_words_set

	def txt2toefl_word(self, file):
		"""
		file: 1368.txt
		r: base_words_set: set()
		"""
		toefl_words_set = set()
		with open(file, encoding='utf-8') as f:
			read_data = f.read()
		word_list  = read_data.strip("").split("\n")
		for word in word_list:
			if word != "":
				toefl_words_set.add(word)
		return toefl_words_set

###########
	def txt2all_words_map(self, file):
		"""
		file: words.txt
		r: all_words_map: {str:int}
		"""
		all_words_map = collections.defaultdict(int)
		with open(file, encoding='utf-8') as f:
			read_data = f.read()
		word_list  = read_data.strip("").split("\n")
		for word in word_list:
			word = word.strip("") 
			if word == "":
				continue
			a, b = word.split(" ")
			all_words_map[a] = int(b)
		return all_words_map

# --------- init above -------------

	def create_table(self, word, sentence):
		"""
		word: str
		sentence: set(str)
		r: cur_table: str 
		"""
		count = 2
		is_toefl = ""
		if word in self.toefl_words_set:
			is_toefl = "#托福"
		cur_table = "## " + word + "  " + str(self.all_words_map[word]) + " " 
		cur_table += '<span align="right">' + is_toefl + "</span>" + "\n" # correct later
		cur_table += self.table_title
		for i, sen in enumerate(sentence):
			if i > count:
				break 
			timeline, chinese, english = self.lines_map[sen]
			english = english.replace(word, "<b>" + word + "</b>")
			cur_table += "|" + sen + "|" + timeline + "|" + chinese + "|" + english + "|" + "\n"
		return cur_table

	def render_summary(self, words):
		"""
		words: [str]
		r: summary: str 
		"""
		words.sort(reverse = True)
		summary = "The number of selected words is " + str(len(words)) + "\n\n"

		table_title = "|"
		for i in range(6):
			if i == 0:
				table_title += "row\\column"
			else:
				table_title += "|" + str(i) 
		table_title +=  "|" + "\n"

		for _ in range(6):
			table_title += "| :--------"
		table_title += "| " + "\n"

		table_content = ""
		row, last = divmod(len(words), 5)
		if last != 0: row += 1 

		for i in range(row):
			table_content += "|" + str(i+1)
			for i in range(5):
				table_content += "|" 
				if words:
					table_content += words.pop() 
			table_content += "|" + "\n"

		summary += table_title + table_content + "\n"
		return summary

	def to1368md(self):
		"""
		"""
		markdown = "# " + "Base Words from " + self.output_name + "\n"
		tables = ""
		selected = []

		for word in self.base_words_set:
			if word in self.words_map:
				cur_table = self.create_table(word, self.words_map[word])
				tables += cur_table + "\n"
				selected.append(word)

		summary = self.render_summary(selected)
		markdown += summary + tables 

		output_file_path = self.directory + "/" + "1368" + self.output_name + ".md"

		with open(output_file_path, mode="w", encoding="utf-8") as f:
			f.write(markdown)

	def to_new_words_md(self):
		"""
		"""
		baseline = 14 # 42 
		markdown = "# " + "New Words from " + self.output_name + "\n"
		new_words = []
		tables = ""

		for word, sentence in self.words_map.items():
			if word not in self.all_words_map or self.all_words_map[word] < baseline:
				cur_table = self.create_table(word, sentence)
				tables += cur_table + "\n"
				new_words.append(word)

			self.all_words_map[word] += len(sentence)

		summary = self.render_summary(new_words)
		markdown += summary + tables 

		output_file_path = self.directory + "/" + "new-words-" + self.output_name + ".md"

		with open(output_file_path, mode="w", encoding="utf-8") as f:
			f.write(markdown)


	def to_quizlet(self):
		"""
		"""
		markdown = "# " + "Quizlet " + self.output_name + "\n"
		for key, val in self.lines_map.items():
			_, chinese, english = val 
			markdown += "|" + key + "|" + chinese + "||" + english + "\n"

		output_file_path = self.directory + "/" + "quizlet" + "-" + self.output_name + ".md"

		with open(output_file_path, mode="w", encoding="utf-8") as f:
			f.write(markdown)


	def update_words_txt(self):
		"""
		"""
		content = ""
		self.all_words_map = dict(sorted(self.all_words_map.items()))
		for key, val in self.all_words_map.items():
			content += key + " " + str(val) + "\n"

		output_file_path = self.words_txt

		with open(output_file_path, mode="w", encoding="utf-8") as f:
			f.write(content)		


if __name__ == "__main__":
	file = "/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/modern-family/Fantastic.Beasts.The.Crimes.of.Grindelwald.srt"
	note = NOTE(file)
	# note.to1368md()
	# note.to_quizlet( )
	note.to_new_words_md()
	# note.update_words_txt()

    # parser = argparse.ArgumentParser()
    # parser.add_argument("-f", "--file", nargs = 1, help="src to markdown")
    # args = parser.parse_args()
    # if args.file:
    # 	src2md(args.file[0])

