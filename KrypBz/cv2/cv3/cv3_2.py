INPUT = "UYCKTLTAERJNNJBDAUOUYGIJNNZRCRSQOHGUOCSWSRSQOQOIYRODRJHNPYOEDLDXDVPWOZHRVFGTYACEJLRWOAZRVFQQZUOTOCFNFLFNNJBNHVHNXAIERVNWYJVTOKCEYJVJBLQNDHQQTLZNGYOONHHNLLUAAMBJSTSMZLFXUHGLIPZJTPBDRJHNPYOEDLDXDVPWOZHRDCCSIJOSTYCSIJNWARCENHNJKSOMETSAAUWWACFQNPHNNHVXDUMPEUSAAACASSCEDHBNHVXJZFYJ"
key_length = 4
alphabet_size = 26

def to_index(char):
	return ord(char) - ord('A')
	
def to_char(num, alphabet_size):
	return chr(num%alphabet_size + ord('A'))
	
def to_indeces(text):
	retval = []
	for a in text:
		retval.append(to_index(a))
	return retval

def coincidence_index(text, alphabet_size):
	indeces = []
	for i in range(alphabet_size):
		indeces.append(0)
	for c in text:
		indeces[to_index(c)] += 1
	result = 0
	for i in indeces:
		i = i/len(text)
		result += i*i
	return result

def monoaphinne_indeces(text, alphabet_size):
	indeces = to_indeces(text)
	retval = ""
	for i in range(alphabet_size):
		text2 = ""
		for j in range(len(indeces)):
			text2 += to_char(indeces[j] + i%alphabet_size, alphabet_size)
		print(text2)
		retval += str(i) + " :\t" + str(coincidence_index(text2, alphabet_size)) + '\n'
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
