"""text_analyzer.py

A command-line tool that analyzes a given text file and reports statistics
like line count, word count, character frequency, the most common word,
and the average word length.

Author: Joseph Catalano
Date: August 30, 2025

Usage:
    python text_analyzer.py <path_to_file>
"""

import sys


def analyze_file(filepath: str) -> None:
    """
    Opens, reads, and analyzes a text file, printing the results.

    Args:
        filepath (str): The path to the text file to be analyzed.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return
    except IOError as e:
        print(f"Error reading file '{filepath}': {e}")
        return

    # --- Analysis ---
    lines = text_content.splitlines()
    words = text_content.split()

    # 1. Line Count
    line_count = len(lines)

    # 2. Word Count
    total_words = len(words)

    # 3. Character Frequency
    character_frequency = {}

    # 4. Word Frequency
    word_frequency = {}

    for char in text_content:
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1

    # 4. Most Common Word
    most_common_word = ""
    max_count = 0
    for word in text_content.split():
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    for word, count in word_frequency.items():
        if count > max_count:
            max_count = count
            most_common_word = word

    # 5. Average Word Length
    total_sum = 0
    for word in text_content.split():
        total_sum += len(word)

    average_word_length = total_sum / total_words

    # --- Reporting ---
    print("--- Text File Analysis ---")
    print(f"File: {filepath}\n")
    print(f"Line Count: {line_count}")
    print(f"Word Count: {total_words}")
    print(f"Most Common Word: '{most_common_word}'")
    print(f"Average Word Length: {average_word_length:.2f} characters")
    print("\n--- Character Frequencies (Top 5) ---")
    sorted_chars = sorted(
        character_frequency.items(), key=lambda item: item[1], reverse=True
    )
    for char, count in sorted_chars[:5]:
        print(f"'{char}': {count}")
    print("--------------------------")


if __name__ == "__main__":
    # Check if a filename was provided on the command line
    if len(sys.argv) < 2:
        print("Usage: python text_analyzer.py <path_to_file>")
    else:
        file_to_analyze = sys.argv[1]
        analyze_file(file_to_analyze)
