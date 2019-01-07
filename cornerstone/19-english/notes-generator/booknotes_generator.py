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

	def __init__(self, txt):
		self.txt = txt 

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

		self.gre_below = self.gre | self.toefl | self.ielts | self.base | self.cet4 | self.cet6 

	def clean(self, word):
		"""
		word: str
		r: str 
		"""
		word = word.strip('",!.?-()\\n').lower() 
		if "'" in word:
			word = word.split("'")[0]
		return word

	def is_word(self, word):
		"""
		word: str 
		r: Boolean
		"""
		pattern_right = r'[a-zA-Z]+[-\']?[a-zA-Z]+'
		if re.fullmatch(pattern_right, word) == None:
			return False 
		return True 

	def words_of_txt(self):

		words_set = set()

		with open(book_path, encoding='utf-8') as f:
			read_data = f.read()

		words = read_data.split(" ")

		for word in words:
			word = self.clean(word)
			if self.is_word(word):
				words_set.add(word)

		# print(len(words_set))
		for word in words_set:
			if word not in self.gre_below:
				print(word)


if __name__ == "__main__":
	book_path = "/Users/wangzhixiang/Desktop/models-of-life.txt"

	note = NOTE(book_path)
	note.words_of_txt()
