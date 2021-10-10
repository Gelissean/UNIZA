INPUT = "UYCKTLTAERJNNJBDAUOUYGIJNNZRCRSQOHGUOCSWSRSQOQOIYRODRJHNPYOEDLDXDVPWOZHRVFGTYACEJLRWOAZRVFQQZUOTOCFNFLFNNJBNHVHNXAIERVNWYJVTOKCEYJVJBLQNDHQQTLZNGYOONHHNLLUAAMBJSTSMZLFXUHGLIPZJTPBDRJHNPYOEDLDXDVPWOZHRDCCSIJOSTYCSIJNWARCENHNJKSOMETSAAUWWACFQNPHNNHVXDUMPEUSAAACASSCEDHBNHVXJZFYJ"
key_length = 4
alphabet_size = 26
slovak_probabilities = [0.0995, 0.0118, 0.0266, 0.0436, 0.0698, 0.0113, 0.0017, 0.0175, 0.0711, 0.0157, 0.0406, 0.0262, 0.0354, 0.0646, 0.0812, 0.0179, 0.0000, 0.0428, 0.0463, 0.0432, 0.0384, 0.0314, 0.0000, 0.0004, 0.0170, 0.0175]

def pow(a,i):
	retval = 1
	for j in range(i):
		retval *= a
	return retval

def find_min(a):
	min_index = 0
	min_val = 999
	for i in range(len(a)):
		if a[i] < min_val:
			min_index = i
			min_val = a[i]
	return min_val, min_index

def to_index(char):
	return ord(char) - ord('A')
	
def to_char(num, alphabet_size):
	return chr(num%alphabet_size + ord('A'))
	
def to_indeces(text):
	retval = []
	for a in text:
		retval.append(to_index(a))
	return retval

def coincidence_index_comparison(text, alphabet_size):
	indeces = []
	for i in range(alphabet_size):
		indeces.append(0)
	for c in text:
		indeces[to_index(c)] += 1
	result = 0
	for j in range(alphabet_size):
		i = indeces[j]/len(text)
		result += pow(i - slovak_probabilities[j], 2)
	return result

def monoaphinne_indeces(text, alphabet_size):
	indeces = to_indeces(text)
	retval = ""
	indeces2 = []
	for i in range(alphabet_size):
		text2 = ""
		print(text2)
		for j in range(len(indeces)):
			text2 += to_char(indeces[j] + i%alphabet_size, alphabet_size)
		print(text2)
		temp = coincidence_index_comparison(text2, alphabet_size)
		indeces2.append(temp)
		retval += str(i) + " :\t" + str(temp) + '\n'
	a,b = find_min (indeces2)
	retval += "Closest value is at " + str(b) + " : " + str(a)
	return retval
	
def desifruj(text, key_length, alphabet_size):
	groups = []
	for i in range(key_length):
		groups.append("")
	i = 0
	for c in text:
		groups[i] += c
		i = (i+1)%key_length
	i = 0	
	for a in groups:
		print("group " + str(i))
		print(monoaphinne_indeces(a, alphabet_size))
		i += 1
		
if  __name__ == "__main__":
	desifruj(INPUT, key_length, alphabet_size)
