



import unittest
from lib import *
from lib.Question import Question
from lib.Node import Node

class TestValidator(unittest.TestCase):
# class TestValidator(colour_runner.runner.ColourTextTestResult):
# class TestValidator(unittest.TestCase):
	# python3 -m unittest tests.py [-v]

	def setUp(self):
		self.mixed_set_half = [
			[0, 1, 2, 3, 4],
			[1, 1, 2, 3, 4],
			[1, 1, 2, 3, 4],
			[0, 1, 2, 3, 4]
		]

		self.uniform_set = [
			[0, 1, 2, 3, 4],
			[0, 1, 2, 3, 4],
			[0, 1, 2, 3, 4],
			[0, 1, 2, 3, 4],
			[0, 1, 2, 3, 4]
		]

		self.mixed_set_1_5 = [
			[0, 1, 2, 3, 4],
			[1, 3, 2, 1, 1],
			[1, 2, 3, 4, 4],
			[1, 1, 2, 4, 7],
			[1, 2, 3, 3, 4],
			[1, 1, 5, 3, 4]
		]

	
	def test_class_count(self):
		_, counts, _, _ = process_classes(self.mixed_set_half)

		self.assertEqual(counts[0], 2)
		self.assertEqual(counts[1], 2)

	def test_gini(self):
		gini_mixed = gini(self.mixed_set_half)
		gini_uniform = gini(self.uniform_set)

		self.assertEqual(gini_mixed, 0.5)
		self.assertEqual(gini_uniform, 0.0)

	def test_entropy(self):
		entropy_mixed = entropy(self.mixed_set_1_5)

		self.assertEqual(round(entropy_mixed, 2), 0.65) 

	def test_split(self):
		question = Question(1, 2)
		true_rows, _ = split(self.mixed_set_1_5, question)

		self.assertEqual(true_rows, [
			[1, 2, 3, 4, 4],
			[1, 2, 3, 3, 4] 
		])

	






def run_tests():
	print("Executing unit tests...\n")
	unittest.main(verbosity=2)  # executes unit tests on execution
                                # 0: quiet, 
                                # 1: dots or F, 
                                # 2: test functions names

   
if __name__ == '__main__':
	run_tests()
