# 🧠 Your Task: Tokenize the story from 'story.txt' using NLTK's sent_tokenize and word_tokenize functions

# Make sure required NLTK resources are available
from functools import reduce
from nltk.tokenize import sent_tokenize,word_tokenize
import re

# 1. Open and read the story text
file = open("./story.txt")
text_from_file = (file.read()).lower()
file.close()

# [(r'([\w])(?=\1)',''),(r'</?div>|[💻|💡|"|*|&|#|>|,|-]*', ''),(r'\s{2,}',' '),(r' *\.','.')]
# 2. (Optional) Remove any unwanted characters using re.sub
# For example: remove extra whitespace or punctuation symbols
janitor = [(r'(http://\S+)',' '),(r'div|[💻💡]|"|[^a-z0-9.\s\']',''),(r'\s{2,}',' '),(r'\.{2,}|\s*\.','.')]
broom = lambda dirt,bunnies : re.sub(bunnies[0],bunnies[1],dirt)
never_ending_story = reduce(broom, janitor, text_from_file)
# dirt = accumulator or in this case cleaned text file
# bunnies = representative of the tuple in janitor this holds the regex and what to replace it with 
# print(never_ending_story)

# 3. Tokenize the story into sentences
# TODO: Replace the line below with a call to sent_tokenize
sentences = sent_tokenize(never_ending_story)
# print(sentences)

# 4. Tokenize the story into words
# TODO: Replace the line below with a call to word_tokenize
words = word_tokenize(never_ending_story)

# 5. Print results
print("=== Sentences ===")
print(sentences)
print("\n=== Words ===")
print(words)
