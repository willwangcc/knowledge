"""
Plan:
IPA transcription: 
	https://rapidapi.com/katspaugh/api/ipa-transcription
	https://github.com/mphilli/English-to-IPA
"""

import argparse
import collections 
import re
import subprocess 

import eng_to_ipa as ipa
import vocabulary_generator
"""
upload_imgur 
ffmpeg 
"""

class NOTE:

	def __init__(self, src):
		self.src = src 

		# vocabulary library 
		self.vocabulary = vocabulary_generator.VOCABULARY()
		self.gre = self.vocabulary.get_gre()
		self.toefl = self.vocabulary.get_toefl()
		self.ielts = self.vocabulary.get_ielts()
		self.base = self.vocabulary.get_base_words()
		self.cet4 = self.vocabulary.get_cet4()
		self.cet6 = self.vocabulary.get_cet6()
		self.all_words_map = self.vocabulary.get_all_words_map()
		self.sentence_map = self.vocabulary.get_sentence_map()

		# 
		self.lines_map = {} #  index: [timeline, chinese, english]
		self.words_map = {} #  word: set(index1, index2)
		self.output_name = None 
		self.directory = None 

		self.sentence_example = collections.defaultdict(list)
		self.pics = {}  # sentence_index: pic_link

		self.lines_map, self.words_map, self.output_name, self.directory = self.src2lines_word(src)
		

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
		word = word.strip('",!.?-').lower() 
		if "'" in word:
			word = word.split("'")[0]
		return word


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
		if english and english[-1] in (".", "!", "?"):
			return True 
		return False 


	def is_word(self, word):
		"""
		word: str 
		r: Boolean
		"""
		pattern_right = r'[a-zA-Z]+[-\']?[a-zA-Z]+'
		if re.fullmatch(pattern_right, word) == None:
			return False 
		return True 

	def split_line(self, line):
		"""
		23
		00:00:01,530 --> 00:00:03,740
		真想知道曼尼现在在做什么
		I wonder what Manny's doing right now.
		---
		re: int, time, chinese, english 
		"""
		return line.split("\n")

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
			group = self.split_line(line)
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

				# count example of sentence pattern
				for pattern, notes in self.sentence_map.items():
					# print(pattern, English)
					# print()
					p = re.compile(pattern)
					if p.search(English):
						# print(pattern, notes, English)
						self.sentence_example[notes[0]].append(position[0])  # number of pattern
						# print("pattern...")
				position = []
				content = []


		return lines_map, words_map, name, directory


# --------- init above -------------

	def is_tag(self, word):
		"""
		word: str 
		r: word_tags: str
		"""
		tags = [
		["TOEFL", False],
		["IELTS", False],
		["GRE", False],
		["CET4", False],
		["CET6", False]
		]

		if word in self.toefl:
			tags[0][1] = True
		if word in self.ielts:
			tags[1][1] = True 
		if word in self.gre:
			tags[2][1] = True 
		if word in self.cet4:
			tags[3][1] = True 
		if word in self.cet6:
			tags[4][1] = True 


		word_tags = ""
		for key, val in tags:
			if val == True:
				word_tags += "`" + key + "`" + " "

		return word_tags 


	def create_table(self, word, sentence):
		"""
		word: str
		sentence: set(str)
		r: cur_table: str 
		"""
		count = 2
		word_tags = self.is_tag(word)

		pronounce = ipa.convert(word)
		
		word_notes = "* [" + pronounce + "] " + "\n"
		word_notes += "* " + str(self.all_words_map[word]) + "+"+ "\n"
		word_notes += "* " + word_tags 

		cur_table = "## " + word + "\n"
		cur_table += word_notes + "\n\n"
		

		# if "How.I.Met.Your.Mother" in self.src: 
		# 	# timeline: 00:14:50,790 --> 00:14:53,757
		# 	sen = next(iter(sentence))

		# 	timeline, chinese, english = self.lines_map[sen]
		# 	# print(timeline)

		# 	if sen in self.pics:
		# 		link = self.pics[sen]
		# 	else:
		# 		left = timeline.split("-->")[0].strip("")
		# 		start_time = left.split(",")[0].strip("")
		# 		pic = sen + '.jpg'
		# 		video = 'How.I.Met.Your.Mother.-.1x02.-.Purple.Giraffe.rmvb'
		# 		create_pic = 'ffmpeg -ss ' + start_time + ' -i ' + video + ' -vframes 1 -q:v 2 ' + pic
		# 		upload_imgur = '/Users/wangzhixiang/.nvm/versions/node/v11.2.0/bin/imgur-upload ' + pic 
		# 		subprocess.Popen(create_pic, shell=True, stdout=subprocess.PIPE).stdout.read()
		# 		link = subprocess.Popen(upload_imgur, shell=True, stdout=subprocess.PIPE).stdout.read()
		# 		# output: b'http://imgur.com/zjSIQ83\n'
		# 		link = str(link).lstrip("b'").rstrip("\\n'")
			
		# 	self.pics[sen] = link
		# 	screenshot = "![" + sen + "]("+ link +")"
		# 	cur_table += screenshot + "\n\n"


		cur_table += self.table_title


		for i, sen in enumerate(sentence):
			if i > count:
				break 
			# print(self.lines_map)
			# print(sen)
			timeline, chinese, english = self.lines_map[sen]
			english = english.replace(word, "<b>" + word + "</b>")
			cur_table += "|" + se n + "|" + timeline + "|" + chinese + "|" + english + "|" + "\n"
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

		for word in self.base:
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
		baseline = 7 # 42 
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


	def update_words_txt(self):
		"""
		"""
		self.vocabulary.update_words_txt(self.all_words_map)	

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

	def render_summary_of_sentence(self, new_sentences):
		"""
		new_sentences: str
		"""
		summary = "The number of selected sentences is " + str(len(new_sentences)) + "\n\n"

		for sentence in new_sentences:
			summary += "1. " + sentence + "\n"

		return summary

	def to_sentence(self):
		"""
		"""
		baseline = 0 # 42 
		markdown = "# " + "New pattern exmaple from " + self.output_name + "\n"
		new_sentences = []
		tables = ""

		for _, notes in self.sentence_map.items():
			pattern_index = notes[0]
			if pattern_index in self.sentence_example and notes[-1] < baseline:
				sentence = self.sentence_example[pattern_index]
				word = notes[2] # to change, example + notes
				cur_table = self.create_table(word, sentence) 
				tables += cur_table + "\n"
				new_sentences.append(word)

				notes[-1] += len(sentence)

		summary = self.render_summary_of_sentence(new_sentences) + "\n"
		markdown += summary + tables 

		output_file_path = self.directory + "/" + "new-sentences-" + self.output_name + ".md"

		with open(output_file_path, mode="w", encoding="utf-8") as f:
			f.write(markdown)


if __name__ == "__main__":
	file = "/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/notes-generator/sources/"
	file += "How.I.Met.Your.Mother/"
	file += "How.I.Met.Your.Mother.S01E05.srt"

	# file += "movies/"
	# file += "Bird.Box.srt"
	note = NOTE(file)
	note.to1368md()
	# note.to_sentence()
	# note.to_quizlet( )
	note.to_new_words_md()
	note.update_words_txt()

    # parser = argparse.ArgumentParser()
    # parser.add_argument("-f", "--file", nargs = 1, help="src to markdown")
    # args = parser.parse_args()
    # if args.file:
    # 	src2md(args.file[0])

