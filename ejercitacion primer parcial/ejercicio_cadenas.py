def validar(cadena):
	largo = 8 <= len(cadena) <= 12
	caracter_en_mayus = 0
	caracter_en_minus = 0
	caracter_numerico = 0
	tiene_simbolos = False
	tiene_otros_simbolos = False

	for caracter in cadena:
		if caracter.isalpha():
			if caracter.isupper():
				caracter_en_mayus += 1
			else:
				caracter_en_minus += 1
		elif caracter.isnumeric():
			caracter_numerico += 1
		elif caracter in ["*","-","$","@"]:
			tiene_simbolos = True
		else:
			tiene_otros_simbolos = True
	return largo and caracter_en_mayus >= 1 and caracter_en_minus >= 3 and caracter_numerico >= 2 and tiene_simbolos and not tiene_otros_simbolos

print(validar("Hola1234@"))