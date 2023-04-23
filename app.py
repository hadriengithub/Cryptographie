def position(x):
	i = 0
	if x not in alphabet:
		return -1;
	else:
		for lettre in alphabet:
			if lettre == x:
				return i
			else:
				i += 1

def decalage(x,n):
	if position(x) + n >= len(alphabet) - 1:
		return alphabet[position(x) + n - len(alphabet)]
	else:
		return alphabet[position(x) + n]

def codage(texte, n):
	encoded_text = ''
	for char in texte:
		if char == ' ':
			encoded_text += ' '
		else:
			encoded_text = encoded_text + decalage(char, n)
	print('Non-encoded text : ', texte)
	print('Encoded text : ', encoded_text)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

codage('hello world !', 3)
