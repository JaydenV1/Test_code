import unittest
from Common.handel_path import project_path
from testCase.test_create_OptionTrade import TestCreateOption
import os

file_path = os.path.join(project_path, r"testCase")
print('路径：', file_path)
# suit = unittest.TestLoader().discover('./', 'test_create_OptionTrade.py')


suit = unittest.TestSuite()
suit.addTest(TestCreateOption("test_option_006"))
runner = unittest.TextTestRunner()
runner.run(suit)
