import unittest
import os
from file_utils import get_file_size, copy_file

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        # Creating temporary files for testing
        self.source_path = 'source.txt'
        self.destination_path = 'destination.txt'
        with open(self.source_path, 'w') as file:
            file.write("This is a test file.")

    def tearDown(self):
        # Removing temporary files after testing
        if os.path.exists(self.source_path):
            os.remove(self.source_path)
        if os.path.exists(self.destination_path):
            os.remove(self.destination_path)

    def test_get_file_size(self):
        # Checking file size retrieval
        size = get_file_size(self.source_path)
        self.assertEqual(size, 20)

    def test_get_file_size_nonexistent_file(self):
        # Checking for non-existent file
        size = get_file_size('nonexistent_file.txt')
        self.assertEqual(size, -1)

    def test_copy_file(self):
        # Checking file copying
        result = copy_file(self.source_path, self.destination_path)
        self.assertEqual(result, "File successfully copied.")

        # Checking if the copied file exists
        self.assertTrue(os.path.exists(self.destination_path))

        # Checking the content of the copied file
        with open(self.destination_path, 'r') as file:
            content = file.read()
        self.assertEqual(content, "This is a test file.")

    def test_copy_file_nonexistent_source(self):
        # Checking copying of a non-existent file
        result = copy_file('nonexistent_source.txt', self.destination_path)
        self.assertEqual(result, "File not found")

if __name__ == '__main__':
    unittest.main()
