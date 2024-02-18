import sys
import time
import click
import re


@click.command()
@click.argument('words_input_file', type=click.File('r'))
@click.argument('searched_file', type=click.File('r'))
def calculate_words(words_input_file, searched_file):

    """Count the occurrence of specific words in "Pan Tadeusz" poem.

    Args:
        words_input_file (file): A file containing a list of words to search for.
        searched_file (file): The text file of "Pan Tadeusz" poem.
    """
    # Open and process the list of words to search for
    file = words_input_file.readlines()
    word_list = [elt.strip() for elt in file]
    word_set = set(word_list)

    counter = 0
    word_counter = 0

    start_time = time.time()

    # Calculate the total number of lines and words
    for line in nonblank_lines(searched_file):
        # Ignore empty lines
        if not '' in line:
            counter += 1
        
        for word in line:
            if word in word_set:
                word_counter += 1

    stop_time = time.time()

    print("Number of lines : %d" % counter)
    print("Found: %d words" % word_counter)
    print("Time elapsed: %.1f second" % (stop_time - start_time))


def nonblank_lines(text_file):
    """[summary]
    Generate non-blank lines from a text file.
    - erased blank lines from begin and end of string
    - it also remove all nonalphanumerical characters
    - exclude space character

    Input: any string text from opened file

    Args:
        text_file (file): The input text file.

    Yields:
    list: Non-blank lines of the text file.
    example : ['word','','word']
    """ 
    
    stripped=''

    for lines in text_file:
        line = lines.strip()
        # Extract alphanumeric characters
        # Split line only by one space multiple spaces are skipped in the list
        text = re.split(r'\s{1,}',line)
        stripp=[]
        for item in text:
            stripped=  ''.join(ch for ch in item if (ch.isalnum()))
            
            stripp.append(stripped)
        
        if stripp:
            yield stripp


@click.command()
@click.argument('word')
@click.argument('searched_file', type=click.Path(exists=True))
def calculate_single_word(word, searched_file):
    """Count how many times a word appears in a file.

    Args:
        word (str): The word to search for.
        searched_file (str): The path to the file to search in.
    """
    try:
        # Initialize a counter to keep track of occurrences
        count = 0
        
        # Open the file in read mode
        with open(searched_file, 'r') as file:
            # Read the content of the file
            file_content = file.read()
            
            # Split the content into words
            words_in_file = file_content.split()
            
            # Iterate through the words in the file
            for w in words_in_file:
                # Check if the word is in the file
                if word == w:
                    # Increment the counter if the word is found
                    count += 1
        
        # Print the count of occurrences
        click.echo(f"The word '{word}' appears {count} times in the file '{searched_file}'.")
    
    except FileNotFoundError:
        # If the file is not found, print an error message and return a non-zero exit code
        click.echo(f"Error: Path '{searched_file}' does not exist.", err=True)
        sys.exit(1)