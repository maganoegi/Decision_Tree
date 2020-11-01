



import unittest
from lib import *
import lib.Question, lib.Node

class TestValidator(unittest.TestCase):
# class TestValidator(colour_runner.runner.ColourTextTestResult):
# class TestValidator(unittest.TestCase):
	# python3 -m unittest tests.py [-v]


	
	def test_class_count(self):
		rows = [
			[0, 1, 2, 3, 4],
			[1, 1, 2, 3, 4],
			[0, 1, 2, 3, 4],
			[0, 1, 2, 3, 4],
			[1, 1, 2, 3, 4],
		]
		total, class_0, class_1 = count_classes(rows)

		self.assertEqual(total, 5)
		self.assertEqual(class_0, 3)
		self.assertEqual(class_1, 2)


def run_tests():
	print("Executing unit tests...\n")
	unittest.main(verbosity=2)  # executes unit tests on execution
                                # 0: quiet, 
                                # 1: dots or F, 
                                # 2: test functions names

   
if __name__ == '__main__':
	run_tests()
