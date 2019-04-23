# alphabetRef = "abcdefghijklmnopqrstuvwxyz"

# def is_pangram(sentence):
# 	sentenceSet = set()
# 	for x in sentence.lower():
# 		if x in alphabetRef:
# 			sentenceSet.add(x)
# 	return len(sentenceSet) == len(alphabetRef)

#### improved version ####
def is_pangram(sentence):
	return set(sentence.lower())>=set('abcdefghijklmnopqrstuvwxyz')