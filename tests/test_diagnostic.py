"""
Test suite for Python Diagnostic Module
"""

import pytest
from src.python_diagnostic import (
    calculate_student_statistics,
    assign_grade,
    count_words,
    clean_student_records
)


class TestCalculateStudentStatistics:
    def test_basic_statistics(self):
        scores = [78, 45, 89, 56, 32, 67, 91, 49]
        result = calculate_student_statistics(scores)
        assert result["total_students"] == 8
        assert result["average_score"] == 63.38
        assert result["highest_score"] == 91
        assert result["lowest_score"] == 32
        assert result["passed_count"] == 5
        assert result["failed_count"] == 3
    
    def test_with_none_values(self):
        scores = [78, None, 89, None, 67]
        result = calculate_student_statistics(scores)
        assert result["total_students"] == 3
    
    def test_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="No valid scores found"):
            calculate_student_statistics([])
    
    def test_invalid_type_raises_error(self):
        with pytest.raises(TypeError, match="Expected a list"):
            calculate_student_statistics("not a list")


class TestAssignGrade:
    def test_grade_a(self):
        assert assign_grade(85) == "A"
        assert assign_grade(92) == "A"
        assert assign_grade(100) == "A"
    
    def test_grade_b(self):
        assert assign_grade(70) == "B"
        assert assign_grade(76) == "B"
        assert assign_grade(84) == "B"
    
    def test_grade_c(self):
        assert assign_grade(60) == "C"
        assert assign_grade(65) == "C"
        assert assign_grade(69) == "C"
    
    def test_grade_d(self):
        assert assign_grade(50) == "D"
        assert assign_grade(55) == "D"
        assert assign_grade(59) == "D"
    
    def test_grade_f(self):
        assert assign_grade(0) == "F"
        assert assign_grade(25) == "F"
        assert assign_grade(49) == "F"
    
    def test_invalid_negative_score(self):
        with pytest.raises(ValueError, match="between 0 and 100"):
            assign_grade(-5)
    
    def test_invalid_high_score(self):
        with pytest.raises(ValueError, match="between 0 and 100"):
            assign_grade(105)
    
    def test_invalid_type(self):
        with pytest.raises(TypeError, match="must be a number"):
            assign_grade("ninety")


class TestCountWords:
    def test_basic_word_count(self):
        text = "hello world hello"
        freq, top3 = count_words(text)
        assert freq["hello"] == 2
        assert freq["world"] == 1
    
    def test_case_insensitivity(self):
        text = "Hello hello HELLO"
        freq, top3 = count_words(text)
        assert freq["hello"] == 3
    
    def test_punctuation_removal(self):
        text = "Hello, world! Hello..."
        freq, top3 = count_words(text)
        assert "hello" in freq
        assert "world" in freq
    
    def test_top_three_words(self):
        text = "apple banana apple cherry banana apple"
        freq, top3 = count_words(text)
        assert top3[0] == ("apple", 3)
        assert top3[1] == ("banana", 2)
    
    def test_empty_string_raises_error(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            count_words("")
    
    def test_invalid_type_raises_error(self):
        with pytest.raises(TypeError, match="Expected a string"):
            count_words(123)


class TestCleanStudentRecords:
    def test_basic_cleaning(self):
        records = [
            {"name": "huda", "score": 78},
            {"name": "haram", "score": None},
            {"name": "jhanzaib", "score": 92},
            {"name": "", "score": 65},
            {"name": "izhar", "score": 110},
            {"name": "ibtisam", "score": 48}
        ]
        cleaned, avg = clean_student_records(records)
        assert len(cleaned) == 3
        assert avg == 72.67
    
    def test_remove_missing_names(self):
        records = [
            {"name": "", "score": 80},
            {"name": None, "score": 90},
            {"name": "Valid", "score": 75}
        ]
        cleaned, avg = clean_student_records(records)
        assert len(cleaned) == 1
        assert cleaned[0]["name"] == "Valid"
    
    def test_remove_invalid_scores(self):
        records = [
            {"name": "A", "score": -10},
            {"name": "B", "score": 150},
            {"name": "C", "score": 75}
        ]
        cleaned, avg = clean_student_records(records)
        assert len(cleaned) == 1
        assert cleaned[0]["name"] == "C"
    
    def test_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="No valid records found"):
            clean_student_records([])
    
    def test_invalid_type_raises_error(self):
        with pytest.raises(TypeError, match="Expected a list"):
            clean_student_records("not a list")


class TestEdgeCases:
    def test_boundary_scores(self):
        assert assign_grade(0) == "F"
        assert assign_grade(49) == "F"
        assert assign_grade(50) == "D"
        assert assign_grade(59) == "D"
        assert assign_grade(60) == "C"
        assert assign_grade(69) == "C"
        assert assign_grade(70) == "B"
        assert assign_grade(84) == "B"
        assert assign_grade(85) == "A"
        assert assign_grade(100) == "A"
    
    def test_mixed_types_in_scores(self):
        scores = [78, "invalid", 89, None, 56]
        result = calculate_student_statistics(scores)
        assert result["total_students"] == 3
