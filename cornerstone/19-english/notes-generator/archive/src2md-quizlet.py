"""
src -> markdown 
"""

import argparse

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

	markdown = "# " + name + "\n"


	lines = block[11:]
	i = 0
	while i < len(lines):
		group = lines[i].split("\n")
		if len(group) == 4: 
			index, timeline, chinese, english = group
			while i+1 < len(lines) and english[-1] not in (".", "!", "?"):
				i += 1 
				g = lines[i].split("\n")
				if len(g) == 4: 
					a, b, c, d = g
					chinese += " " + c 
					english += " " + d
			markdown += "|" + index + "|" + chinese + "||" + english + "\n"
		i += 1
		
	markdown += "\n"

	output_file_path = directory + "/" + "quizlet" + "-" + name + ".md"

	with open(output_file_path, mode="w", encoding="utf-8") as f2:
		f2.write(markdown)
	return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", nargs = 1, help="src to markdown")
    args = parser.parse_args()
    if args.file:
    	src2md(args.file[0])

