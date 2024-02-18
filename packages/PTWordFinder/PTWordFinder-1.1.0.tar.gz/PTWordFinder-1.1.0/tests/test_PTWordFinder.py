import os
import subprocess
import sys
import pytest
from unittest import mock

from unittest.mock import Mock

from ptwordfinder.commands.PTWordFinder import calculate_words
from ptwordfinder.commands.PTWordFinder import calculate_single_word
from ptwordfinder.commands.PTWordFinder import nonblank_lines
from click.testing import CliRunner

# Functional test

# Path to the directory containing the PTWordFinder.py script
path = "ptwordfinder/commands/"  

def test_help():
    # Execute the PTWordFinder.py script with the --help argument to display the help message
    exit_status = os.system(f'python3 {path}PTWordFinder.py --help')
    # Assert that the exit status of the command is 0, indicating successful execution
    assert exit_status == 0
    
#Unit tests 
  
@pytest.mark.parametrize(('files, lines, words, time'),
[
    # Test case 1: Testing with a specific text file, expecting an xfail due to a bug
    pytest.param('tests/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt',
                 'Number of lines : 9513',  # Explanation: Expected number of lines in the file
                 'Found: 166 words',        # Explanation: Expected number of words found in the file
                 'Time elapsed: 0.1 second',# Explanation: Expected time taken to process the file
                 marks=pytest.mark.xfail(reason="some bug")),  # Explanation: Marking this test as xfail due to known bug

    # Test case 2: Testing with a generic text file, no expected failures
    ('tests/test-file.txt',                # Explanation: Path to the text file being tested
     'Number of lines : 4',                # Explanation: Expected number of lines in the file
     'Found: 6 words',                     # Explanation: Expected number of words found in the file
     'Time elapsed: 0.0 second'),          # Explanation: Expected time taken to process the file
],
)
def test_calculate_words(files, lines, words, time):
    ln = lines
    runner = CliRunner()
    result = runner.invoke(calculate_words, ['tests/words-list.txt', files])
    assert result.exit_code == 0
    assert result.output == (f"{lines}\n"  # Explanation: Expected output format including lines, words, and time
                             f"{words}\n"
                             f"{time}\n")
    
    
def test_nonblank_lines_for_multilines():

    # Given
    
    # Mocking the content of a file with multiple lines including different types of characters
    # - multiline string
    # - multiple spaces ale skipped
    # - empty line are not counting
    # - special character not counting
    
    # First line with multiple spaces
    first_line = 'bb bbb, bbb       '
    # Second line with ellipsis surrounded by spaces
    second_line = "    ...   "
    # Third line with parentheses and spaces
    third_line = "  dd d d  (ddd)   d      \n"

    # Creating a multiline string with the above lines
    text='\n'.join((first_line,second_line,third_line))

    # Filename to be used in the test
    filename ='test-file'
 
    # Mocking the file open operation to return the text content 
    text_data = mock.mock_open(read_data=text)
    with mock.patch('%s.open' % __name__,text_data, create=True):
        f = open(filename)
        
    # When
        # Calling the function nonblank_lines with the mocked file object
        result = nonblank_lines(f)
        result=list(result)
    
    # Then
    # Asserting the result against the expected text structure       
    expected_text =[['bb', 'bbb', 'bbb'],[''],['dd', 'd', 'd','ddd','d']]    
    assert result ==  expected_text
 

def test_nonblank_lines_for_one_line():
    # Given
    # Setting up a single line string with leading and trailing spaces
    filename ='test-file'
    text= '     bb bbb, bbb,       '

    # When
    # Mocking the file open operation to return the single line text content  
    text_data = mock.mock_open(read_data=text)
    with mock.patch('%s.open' % __name__,text_data, create=True):
        f = open(filename)
        
         # Calling the function nonblank_lines with the mocked file object
        result = nonblank_lines(f)
        result=list(result)

    # Then
    # Asserting the result against the expected text structure
        expected_text = [['bb', 'bbb', 'bbb']]
    
        assert result ==  expected_text

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def test_file(tmpdir):
    # Create a temporary file with some content for testing
    test_content = "apple banana apple orange"
    test_file_path = tmpdir.join("test_file.txt")
    with open(test_file_path, 'w') as f:
        f.write(test_content)
    return str(test_file_path)

def test_calculate_single_word(runner, test_file):
    # Given: Test file and a runner for invoking the command
    
    # Test case 1
    # When: Testing with a word that appears multiple times
    result = runner.invoke(calculate_single_word, ['apple', test_file])
    # Then: Verify the result for multiple occurrences
    assert result.exit_code == 0
    assert "The word 'apple' appears 2 times in the file" in result.output
    
    # Test case 2
    # When: Testing with a word that appears once
    result = runner.invoke(calculate_single_word, ["banana", test_file])
    assert result.exit_code == 0
    # Then: Verify the result for single occurrence
    assert "The word 'banana' appears 1 times in the file" in result.output
    
    # Test case 3
    # When: Testing with a word that doesn't appear
    result = runner.invoke(calculate_single_word, ["grape", test_file])
    assert result.exit_code == 0
    # Then: Verify the result for word not found
    assert "The word 'grape' appears 0 times in the file" in result.output
    
    # Test case 4
    # When: Testing with a non-existent file
    result = runner.invoke(calculate_single_word, ["apple", "nonexistent_file.txt"])
    assert result.exit_code != 1
    # Then: Verify the error message for non-existent file
    assert "Error: Invalid value for 'SEARCHED_FILE': Path 'nonexistent_file.txt' does not exist." in result.output
    
    # Test case 5
    # Test with an empty file
    empty_file = "empty_file.txt"
    open(empty_file, "w").close()
    result = runner.invoke(calculate_single_word, ["apple", empty_file])
    # Then: Verify the result for an empty file
    assert result.exit_code == 0
    assert "The word 'apple' appears 0 times in the file" in result.output


if __name__ == "__main__":
    sys.exit(calculate_words(sys.argv), calculate_single_word(sys.argv))    
