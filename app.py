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

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print("La position de la 1 dans l'alphabet est : ", position('1'))
print("La position de la lettre a dans l'alphabet est : ", position('a'))
print("la position de la lettre d dans l'alphabet est : ", position('d'))