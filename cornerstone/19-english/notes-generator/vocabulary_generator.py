"""
change GRE into set 
"""

import collections

class VOCABULARY:

	def __init__(self):
		self.gre = set() # "word": "definition"
		
		self.vocabulary_path = "/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/notes-generator/vocabulary/"
		self.gre_txt = self.vocabulary_path + "GRE.txt"
		self.toefl_txt = self.vocabulary_path + "TOEFL.txt"
		self.ielts_txt = self.vocabulary_path + "IELTS.txt"

		self.base_txt = self.vocabulary_path + "Base.txt"
		self.cet4_txt = self.vocabulary_path + "CET4.txt"
		self.cet6_txt = self.vocabulary_path + "CET6.txt"
		self.all_words = self.vocabulary_path + "words.txt"
		self.sentence_txt = self.vocabulary_path + "sentences-pattern.txt"

		
	def get_word_set(self, file):
		"""
		file: xxx.txt
		r: gre_words_set: set()
		"""
		words_set = set()
		with open(file, encoding='utf-8') as f:
			read_data = f.read()
		word_list  = read_data.strip("").split("\n")
		for word in word_list:
			if word != "":
				words_set.add(word)
		return words_set 


	def get_gre(self):
		"""
		file: GRE.txt
		r: gre_words_map: set()
		"""
		return self.get_word_set(self.gre_txt)


	def get_toefl(self):
		return self.get_word_set(self.toefl_txt)


	def get_ielts(self):
		return self.get_word_set(self.ielts_txt)


	def get_base_words(self):
		return self.get_word_set(self.base_txt)


	def get_cet4(self):
		return self.get_word_set(self.cet4_txt)


	def get_cet6(self):
		return self.get_word_set(self.cet6_txt)


	def get_all_words_map(self):
		"""
		file: words.txt
		r: all_words_map: {str:int}
		"""
		all_words_map = collections.defaultdict(int)
		file = self.all_words

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


	def update_words_txt(self, words_map):
		"""
		"""
		content = ""
		new_words = dict(sorted(words_map.items()))
		for key, val in new_words.items():
			content += key + " " + str(val) + "\n"

		output_file_path = self.all_words
		with open(output_file_path, mode="w", encoding="utf-8") as f:
			f.write(content)


	def get_sentence_map(self):
		"""
		file: words.txt
		r: all_words_map: {str:int}
		"""
		# print("txt2sentence_map...")
		file = self.sentence_txt 
		sentence_map = {}
		with open(file, encoding='utf-8') as f:
			read_data = f.read()
		# print(read_data)
		sentence_list  = read_data.strip("").split("\n")

		# print(sentence_list)
		for sentence in sentence_list:
			group = sentence.split("||")
			# print(group)
			if len(group) == 5:
				index, ex, pattern, note, count = [i.strip('" ') for i in group]
				sentence_map[pattern] = [index, ex, note, int(count)]
		# print(sentence_map)
		return sentence_map

if __name__ == "__main__":
	vocabulary = VOCABULARY()
	gre = vocabulary.get_gre()
	# print(gre)