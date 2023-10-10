import unittest
import os
from DebianContribution import fetch_and_parse_debian_news

class TestDebianContribution(unittest.TestCase):
    def test_fetch_and_parse_debian_news(self):
        # Define a temporary file path for testing
        test_output_file = "test_debian_news.md"
        
        # Call the function to be tested
        fetch_and_parse_debian_news(test_output_file)
        
        # Check if the test output file was created
        self.assertTrue(os.path.isfile(test_output_file))
        
        # Check if the file is not empty
        with open(test_output_file, "r", encoding="utf-8") as file:
            content = file.read()
            self.assertTrue(len(content) > 0)
        
        # Clean up: Remove the test output file
        os.remove(test_output_file)

if __name__ == "__main__":
    unittest.main()

