

class VOCABULARY:

	def __init__(self):
		self.gre = {} # "word": "definition"
		self.vocabulary_path = "/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/notes-generator/vocabulary/"
		self.gre_txt = self.vocabulary_path + "GRE-words2.txt"
		self.gre = self.txt2gre_word(self.gre_txt)


	def txt2gre_word(self, file):
		"""
		file: GRE.txt
		r: gre_words_map: {}
		"""
		gre_words_map = {}
		with open(file, encoding='utf-8') as f:
			read_data = f.read()
		word_list  = read_data.strip("").split("\n")
		n = len(word_list)
		for i in range(0, n, 2):
			word = word_list[i]
			define = word_list[i+1] 
			gre_words_map[word] = define

		self.gre2txt(gre_words_map)

		return gre_words_map

	def gre2txt(self, words):
		"""
		words: "words":"define"
		""" 
		txt = ""
		for key, val in words.items():
			txt += key + " - " + val + "\n"

		output_file_path = self.vocabulary_path + "/" + "GRE" + ".txt"

		with open(output_file_path, mode="w", encoding="utf-8") as f:
			f.write(txt)


vocabulary = VOCABULARY()