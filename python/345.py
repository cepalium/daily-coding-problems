# --------------------------
# Author: Tuan Nguyen
# Date created: 20200422
#!345.py
# --------------------------
"""
You are given a set of synonyms, such as (big, large) and (eat, consume). 
Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

* "He wants to eat food."
* "He wants to consume food."

Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): 
consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?
"""


def check_equivalent_sentences(sentence_1, sentence_2, synonyms):
    """Returns True if sentence_1 is equivalent with sentence_2 w.r.t pair of synonyms"""
    words_1, n1 = split_sentence_into_words(sentence_1)
    words_2, n2 = split_sentence_into_words(sentence_2)
    if n1 != n2:  # there must be words without equivalence
        return False
    equivalence_map = build_equivalence_map(synonyms)
    for i in range(n1):
        if not check_equivalent_words(words_1[i], words_2[i], equivalence_map):
            return False
    return True


def split_sentence_into_words(sentence):
    import re

    sentence = re.sub(
        r"[^\w\s]", "", sentence
    )  # remove punctuation from sentence
    words = sentence.split(" ")
    return words, len(words)


def check_equivalent_words(word_1, word_2, equivalence_map):
    if word_1 == word_2:  # the same word at same position in 2 sentence
        return True
    if (
        word_1 not in equivalence_map.keys()
        or word_2 not in equivalence_map.keys()
    ):
        return False
    word_1_equals = equivalence_map[word_1]
    word_2_equals = equivalence_map[word_2]
    if word_1 not in word_2_equals or word_2 not in word_1_equals:
        return False
    return True


def build_equivalence_map(synonyms):
    equivalence_map = initialize_equivalence_map(synonyms)
    for pair in synonyms:
        a, b = pair[0], pair[1]
        equivalence_map[a].append(b)
        equivalence_map[b].append(a)
    return equivalence_map


def initialize_equivalence_map(synonyms):
    equivalence_map = {}
    for pair in synonyms:
        a, b = pair[0], pair[1]
        equivalence_map[a] = []
        equivalence_map[b] = []
    return equivalence_map


# ----- Unit Tests -----
def test1():
    sentence_1 = "He wants to eat food."
    sentence_2 = "He wants to consume food."
    synonyms = [("eat", "consume")]
    assert check_equivalent_sentences(sentence_1, sentence_2, synonyms) == True


def test2():
    sentence_1 = "Tom eats a big hamburger."
    sentence_2 = "Tom eats a large hamburger."
    synonyms = [("big", "large")]
    assert check_equivalent_sentences(sentence_1, sentence_2, synonyms) == True


def test3():
    sentence_1 = "Jimmy goes to supermarket."
    sentence_2 = "Jimmy goes to work."
    synonyms = [("supermarket", "mall")]
    assert (
        check_equivalent_sentences(sentence_1, sentence_2, synonyms) == False
    )


if __name__ == "__main__":
    test1()
    test2()
    test3()
