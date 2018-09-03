import string

def format(text, limit, justify):
	separator = ' '
	slice_start = 0
	formatted_text = str()
	
	#substitui os caracteres que quebra de linha para que o algoritmo possa identificá-los como palavras separadas
	text_without_line_break = text.replace('\n', ' \n ')

	#separa o texto inserido usando espaço como separador das palavras
	words = text_without_line_break.split(separator)	

	#percorre as itens do array de palavras do texto inserido para poder cortá-lo em partes de tamanho menor que o limite inserido
	for x in range(1,len(words)):
		line = ''

		#se o texto possui palavras com quantidade de caracteres maior que o limite inserido, é acionado uma exceção
		if len(words[x]) > limit:
			raise ValueError('The text has words bigger than the limit!')

		#se o item selecionado é uma quebra de linha, junta as palavras do intervalo percorrido até a quebra e gera a linha
		elif words[x] =='\n':
			line = LineFormatter(words[slice_start:x], limit, justify, separator) + '\n'
			slice_start = x+1

		#se o intervalo percorrido possui tamanho maior que o limite, junta as palavras do intervalo e gera a linha
		elif len(separator.join(words[slice_start:x+1])) > limit:
			line = LineFormatter(words[slice_start:x], limit, justify, separator) + '\n'
			slice_start = x

		#se o item percorrido é a última palavra do array, gera a linha do intervalo percorrido
		elif x == len(words) -1:
			line = LineFormatter(words[slice_start:], limit, justify, separator)

		#verifica se a linha gerada está dentro dos limites definidos para texto normal (tamanho menor que limite) ou justificado (tamanho igual ao limite)
		if line != '' and line != '\n':
			if justify == True and x < len(words) -1:
				assert len(line) == limit + 1
			else:
				assert len(line) <= limit + 1

		#concatena a linha gerada no resultado final
		formatted_text += line

	#retorna a string formatada
	return formatted_text



#Função para justificar linhas
#Padrão: percorre as palavras da esquerda para a direita e insere um espaço a cada duas palavras. Depois o inverso pela outra direção.
#Exemplos: (caractere '_' representa o espaço adicionado)
#|and the earth. Now the earth was        |
#|and _the earth. Now the earth was       |
#|and  the earth._ Now the earth was      |
#|and  the earth.  Now the_ earth was     |
#|and  the earth.  Now the  earth _was    |
#|and  the earth.  Now _the  earth  was   |
#|and  the _earth.  Now  the  earth  was  |
#|and_  the  earth.  Now  the  earth  was |
#|and   the  earth._  Now  the  earth  was|
#|and   the  earth.   Now  the  earth  was|

#|formless and empty darkness was over    |
#|formless_ and empty darkness was over   |
#|formless  and empty_ darkness was over  |
#|formless  and empty  darkness was_ over |
#|formless  and empty  darkness _was  over|
#|formless  and empty  darkness  was  over|
def LineFormatter(words, limit, justify, separator):
	word_count = len(words)	- 1
	line = ''

	#percorre o array de palavras para acrescentar espaços para justificar a linha
	if  justify == True and word_count > 0:
		index = 0
		increment = 2

		while limit > len(separator.join(words)):
			#sentido: esquerda para direita
			if increment == 2:				
				if index < word_count:
					words[index] = words[index] + separator
					index += increment
				else: #chegou ao fim da linha
					increment = -2
					if index > word_count:
						index = word_count -1
			#sentido: direita para esquerda
			else:
				if index > 0:
					words[index] = separator + words[index]
					index += increment
				else: #chegou ao início da linha
					increment = 2			
					if index < 0:
						index = 1

	return separator.join(words)