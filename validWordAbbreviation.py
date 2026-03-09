def validWordAbbreviation(word: str, abbr: str) -> bool:
	if len(word) < len(abbr):
		return False

	i,j = 0, 0
	while i < len(word) and j < len(abbr):
		if word[i] == abbr[j]:
			i+=1
			j+=1
		else:
			if abbr[j] == "0":
				return False
			elif abbr[j].isalpha():
				return False
			else:
				skip = 0
				while j < len(abbr) and abbr[j].isdigit():
					skip = skip*10 + int(abbr[j])
					j+=1
				i+=skip
	return i == len(word) and j == len(abbr)

word = "apple"
abbr = "a3e"
assert validWordAbbreviation(word, abbr) == True
