from enum import Enum
import math
import re


def count_letters(text: str):
    return sum(c.isalpha() for c in text)


def count_words(text: str):
    return len(text.split())


def count_sentences(text: str):
    return len(re.split(r"[.!?]", text))


def split_into_paragraphs(text: str) -> list[str]:
    return text.split("\n\n")


def split_into_sentences(text: str) -> list[str]:
    return re.split(r"[.!?]", text)


def is_above_threshold(value: int, max_level: int) -> bool:
    return value >= max_level


def rate_text(text: str) -> int:
    paragraphs = split_into_paragraphs(text)
    levels = [
        calculate_ARI(count_letters(p), count_words(p), count_sentences(p))
        for p in paragraphs
    ]
    return max(levels)


def calculate_ARI(letter_count: int, word_count: int, sentence_count: int):
    if word_count == 0 or sentence_count == 0:
        return 0

    average_word_length = letter_count / word_count
    average_sentence_length = word_count / sentence_count
    raw_level = 4.71 * average_word_length + 0.5 * average_sentence_length - 21.43
    rounded_level = int(math.ceil(raw_level))
    return max(rounded_level, 0)
