class VOCABULARY:

	def __init__(self):
		self.gre = {} # "word": "definition"
		
		self.vocabulary_path = "/Users/wangzhixiang/Developer/github/a-growing-cs/cornerstone/19-english/notes-generator/vocabulary/"
		self.gre_txt = self.vocabulary_path + "GRE.txt"
		
	def get_gre(self):
		"""
		file: GRE.txt
		r: gre_words_map: {}
		"""
		file = self.gre_txt
		gre_words_map = {}
		with open(file, encoding='utf-8') as f:
			read_data = f.read()

		word_list  = read_data.strip("").split("\n")
		for word_define in word_list:
			word, define = word_define.split(" - ")
			word = word.strip("")
			define = define.strip("")
			gre_words_map[word] = define

		return gre_words_map

if __name__ == "__main__":
	vocabulary = VOCABULARY()