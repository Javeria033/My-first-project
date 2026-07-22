"""
AI Internship Day 1 - Python Diagnostic Module
Student Performance Analyzer with Error Handling
"""

import string
from typing import List, Dict, Union, Optional, Tuple


def calculate_student_statistics(scores):
    """
    Calculate statistics for a list of student scores.
    """
    if not isinstance(scores, list):
        raise TypeError(f"Expected a list, got {type(scores).__name__}")
    
    valid_scores = []
    for score in scores:
        if score is None:
            continue
        if isinstance(score, (int, float)):
            valid_scores.append(score)
    
    if len(valid_scores) == 0:
        raise ValueError("No valid scores found in the list")
    
    total_students = len(valid_scores)
    average_score = round(sum(valid_scores) / total_students, 2)
    highest_score = max(valid_scores)
    lowest_score = min(valid_scores)
    passed_count = sum(1 for s in valid_scores if s >= 50)
    failed_count = total_students - passed_count
    
    return {
        "total_students": total_students,
        "average_score": average_score,
        "highest_score": highest_score,
        "lowest_score": lowest_score,
        "passed_count": passed_count,
        "failed_count": failed_count
    }


def assign_grade(score):
    """
    Assign a letter grade based on the score.
    """
    if not isinstance(score, (int, float)):
        raise TypeError(f"Score must be a number, got {type(score).__name__}")
    
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def count_words(text):
    """
    Count word frequencies in a given text.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, got {type(text).__name__}")
    
    if len(text.strip()) == 0:
        raise ValueError("Text cannot be empty")
    
    text = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    
    if len(words) == 0:
        raise ValueError("No valid words found after cleaning")
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    top_three = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]
    
    return word_freq, top_three


def clean_student_records(records):
    """
    Clean student records by removing invalid entries.
    """
    if not isinstance(records, list):
        raise TypeError(f"Expected a list, got {type(records).__name__}")
    
    cleaned_records = []
    valid_scores = []
    
    for record in records:
        if not isinstance(record, dict):
            continue
        
        name = record.get("name")
        score = record.get("score")
        
        if name is None or name == "":
            continue
        
        if score is None:
            continue
        
        if not isinstance(score, (int, float)):
            continue
        if score < 0 or score > 100:
            continue
        
        cleaned_records.append({"name": name, "score": score})
        valid_scores.append(score)
    
    if len(cleaned_records) == 0:
        raise ValueError("No valid records found after cleaning")
    
    average_score = round(sum(valid_scores) / len(valid_scores), 2)
    
    return cleaned_records, average_score


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("   STUDENT PERFORMANCE ANALYZER")
    print("=" * 50)
    print("1. Calculate Student Statistics")
    print("2. Assign Grade")
    print("3. Count Word Frequencies")
    print("4. Clean Student Records")
    print("5. Run All Tasks")
    print("6. Exit")
    print("=" * 50)


def run_all_tasks():
    """Run all diagnostic tasks with sample data."""
    print("\n" + "=" * 50)
    print("TASK 1: Student Statistics")
    print("=" * 50)
    scores = [78, 45, 89, 56, 32, 67, 91, 49]
    print(f"Input scores: {scores}")
    stats = calculate_student_statistics(scores)
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 50)
    print("TASK 2: Grade Classification")
    print("=" * 50)
    test_scores = [92, 76, 65, 55, 42]
    for score in test_scores:
        try:
            grade = assign_grade(score)
            print(f"  Score {score} -> Grade {grade}")
        except ValueError as e:
            print(f"  Score {score} -> Error: {e}")
    
    print("\n" + "=" * 50)
    print("TASK 3: Word Frequency Counter")
    print("=" * 50)
    text = "Artificial intelligence is changing the world. Intelligence systems are becoming more powerful."
    print(f"Input text: {text}")
    freq, top3 = count_words(text)
    print(f"  Top 3 words: {top3}")
    
    print("\n" + "=" * 50)
    print("TASK 4: Data Cleaning")
    print("=" * 50)
    student_records = [
        {"name": "huda", "score": 78},
        {"name": "haram", "score": None},
        {"name": "jhanzaib", "score": 92},
        {"name": "", "score": 65},
        {"name": "izhar", "score": 110},
        {"name": "ibtisam", "score": 48}
    ]
    print(f"Input records: {student_records}")
    cleaned, avg = clean_student_records(student_records)
    print(f"  Cleaned records: {cleaned}")
    print(f"  Average score: {avg}")
    print("=" * 50)


def main():
    """Main function."""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "all":
        run_all_tasks()
        return
    
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break
        
        if choice == "1":
            try:
                scores_input = input("Enter scores separated by spaces: ")
                scores = [float(x) for x in scores_input.split()]
                stats = calculate_student_statistics(scores)
                for key, value in stats.items():
                    print(f"  {key}: {value}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                score = float(input("Enter a score (0-100): "))
                grade = assign_grade(score)
                print(f"  Grade: {grade}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            try:
                text = input("Enter text to analyze: ")
                freq, top3 = count_words(text)
                print(f"  Word frequencies: {freq}")
                print(f"  Top 3 words: {top3}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            print("Using sample data...")
            student_records = [
                {"name": "huda", "score": 78},
                {"name": "haram", "score": None},
                {"name": "jhanzaib", "score": 92},
                {"name": "", "score": 65},
                {"name": "izhar", "score": 110},
                {"name": "ibtisam", "score": 48}
            ]
            cleaned, avg = clean_student_records(student_records)
            print(f"  Cleaned records: {cleaned}")
            print(f"  Average score: {avg}")
        
        elif choice == "5":
            run_all_tasks()
        
        elif choice == "6":
            print("Thank you!")
            break
        
        else:
            print("Invalid choice. Enter 1-6.")


if __name__ == "__main__":
    main()
