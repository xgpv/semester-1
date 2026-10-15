# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
# calculate the number of words

# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount
import sys
wordcount = 0
try:
    filename = input("Enter the filename: ")
except FileNotFoundError:
    sys.exit("No file found.")

with open(f'{filename}.txt', 'r') as file1:
    for line in file1:
        line = (line.strip().split())
        for word in line:
           wordcount += 1
         
    print(f'There are {wordcount} words in file {filename}.txt.')
    wordcount = 0
    

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210