import unittest
from StringFormatter import format

class test_format(unittest.TestCase):
	def test_should_return_formatted_text_with_limit_40_without_justify(self):
		#Arrange
		text = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'
		limit = 40
		justify = False
		expected_result = 'In the beginning God created the heavens\nand the earth. Now the earth was\nformless and empty, darkness was over\nthe surface of the deep, and the Spirit\nof God was hovering over the waters.\n\nAnd God said, "Let there be light," and\nthere was light. God saw that the light\nwas good, and he separated the light\nfrom the darkness. God called the light\n"day," and the darkness he called\n"night." And there was evening, and\nthere was morning - the first day.'

		#Act
		formattedText = format(text, limit, justify)

		#Assert
		self.assertEqual(formattedText, expected_result)

	def test_should_return_formatted_text_with_limit_20_without_justify(self):
		#Arrange
		text = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'
		limit = 20
		justify = False
		expected_result = 'In the beginning God\ncreated the heavens\nand the earth. Now\nthe earth was\nformless and empty,\ndarkness was over\nthe surface of the\ndeep, and the Spirit\nof God was hovering\nover the waters.\n\nAnd God said, "Let\nthere be light," and\nthere was light. God\nsaw that the light\nwas good, and he\nseparated the light\nfrom the darkness.\nGod called the light\n"day," and the\ndarkness he called\n"night." And there\nwas evening, and\nthere was morning -\nthe first day.'

		#Act
		formattedText = format(text, limit, justify)

		#Assert
		self.assertEqual(formattedText, expected_result)
		
	def test_should_throw_ValueErrorException_when_text_has_words_bigger_then_limit(self):
		#Arrange
		text = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'
		limit = 8
		justify = False

		#Act
		#Assert
		with self.assertRaises(ValueError):
			format(text, limit, justify)
		
	def test_should_return_formatted_text_with_limit_40_with_justify(self):
		#Arrange
		text = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'
		limit = 40
		justify = True
		expected_result = 'In the beginning God created the heavens\nand   the  earth.   Now  the  earth  was\nformless  and empty,  darkness was  over\nthe  surface of the deep, and the Spirit\nof  God was  hovering over  the  waters.\n\nAnd  God said, "Let there be light," and\nthere  was light. God saw that the light\nwas  good, and  he separated  the  light\nfrom  the darkness. God called the light\n"day,"   and  the   darkness  he  called\n"night."  And  there  was  evening,  and\nthere  was  morning  -  the  first  day.'
		
		#Act
		formattedText = format(text, limit, justify)
		
		#Assert
		self.maxDiff = None
		self.assertEqual(formattedText, expected_result)
		