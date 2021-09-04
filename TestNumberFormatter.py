from mytest import NumberFormatter
import unittest.mock
import unittest


class TestNumberFormatter(unittest.TestCase):

	def setUp(self):
		self.formatter = NumberFormatter()

	@unittest.mock.patch('builtins.input', side_effect='+855')
	def testPlus(self, mock):
		self.assertEqual(self.formatter.parseInt(), 855)

	@unittest.mock.patch('builtins.input', side_effect='-855')
	def test_minus(self, mock):
		self.assertEqual(self.formatter.parseInt(), -855)

	@unittest.mock.patch('builtins.input', side_effect='855')
	def test_int(self, mock):
		self.assertEqual(self.formatter.parseInt(), 855)

	@unittest.mock.patch('builtins.input', side_effect='')
	def test_empty(self, mock):
		self.assertEqual(self.formatter.parseInt(), 'Your string is empty')


if __name__ == "__main__":
	unittest.main()