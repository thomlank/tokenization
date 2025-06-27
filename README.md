# 📘 Assignment: Tokenizing a Story with NLTK

Welcome to your first text pre-processing assignment! In this project, you’ll apply your knowledge of tokenization to process a short story using Python and the Natural Language Toolkit (NLTK).

## 🎯 Objective

Read a short story from a `.txt` file and:

1. Tokenize it into sentences using `sent_tokenize()`
2. Tokenize it into words using `word_tokenize()`
3. (Optional) Clean the story using `re.sub()` to remove unwanted characters

## 📁 Files Provided

- `story.txt`: A short story about a beginner coder.
- `main.py`: A starter Python script where you will write your code.
- `README.md`: You’re reading it now!

## ✅ Steps

1. **Install NLTK** if you haven’t already:

    ```bash
    pip install nltk
    ```

2. **Download NLTK resources** in `main.py`:
    The script already includes the `nltk.download('punkt')` command for tokenizer models.

3. **Read the file**: Use Python’s file reading tools to load `story.txt`.

4. **Clean the text (optional)**: Use `re.sub()` to remove any characters you don’t want included in your analysis.

5. **Tokenize the story**:
    - Use `sent_tokenize()` to break the story into sentences.
    - Use `word_tokenize()` to break the story into individual words.

6. **Print the results** to compare and see the difference between sentence and word tokenization.

## 🤔 Questions to Think About

- How does `sent_tokenize()` determine where a sentence ends?
- How does punctuation affect `word_tokenize()`?
- How could this process help a chatbot better understand user input?

## 💡 Bonus Challenge

- Count how many sentences and how many words are in the story.
- Print the most frequent word (ignoring common stopwords like "the", "and", etc.)

Happy tokenizing! 🧠💬
