"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations
from collections import Counter, defaultdict, deque



def normalize_username(name: str) -> str:
    return name.strip().lower().replace(' ', '_')
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    raise NotImplementedError


def is_valid_age(age: int) -> bool:
    if age < 18 or age > 120:
        return False
    return True
    """Return True if age is in [18, 120], otherwise False."""
    raise NotImplementedError


def truthy_values(values: list[object]) -> list[object]:
    true_values = []
    for value in values:
        if value:
            true_values.append(value)
    return true_values
    """Return a new list containing only truthy values from input."""
    raise NotImplementedError

def sum_until_negative(numbers: list[int]) -> int:
    n=0
    for number in numbers:
        if number > 0:
            n += number
        else:
            break
    return n
    # """Return sum of numbers until the first negative value (exclusive)."""
    # raise NotImplementedError


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 3 != 0]

    """Return numbers excluding values divisible by 3."""
    raise NotImplementedError


def first_even_or_none(numbers: list[int]) -> int | None:
    for number in numbers:
        if number % 2 == 0:
            return number
        else:
            return None
    """Return the first even number, or None if no even number exists."""
    raise NotImplementedError


def squares_of_even(numbers: list[int]) -> list[int]:
    n = [number**2 for number in numbers if number % 2 == 0]
    """Return squares of all even numbers in input order."""
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    words_lengths = {}
    for word in words:
        words_lengths[word] = len(word)
    return words_lengths
#     """Return dict mapping each word to its length."""
#     raise NotImplementedError


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    return list(zip(keys, values))
    raise NotImplementedError


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    """Build and return {'name': name, 'role': role, 'active': active}."""
    user = {}
    user['name'] = name
    user['role'] = role
    user['active'] = active
    return user
    raise NotImplementedError


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags safely (no shared mutable default across calls)."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
    raise NotImplementedError


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    """Invert mapping. Assume values are unique."""
    inverted = {}
    for key, value in mapping.items():
        inverted[value] = key
    return inverted
    raise NotImplementedError


def unique_sorted_tags(tags: list[str]) -> list[str]:
    """Return unique tags sorted ascending."""
    return sorted(set(tags))
    raise NotImplementedError



def count_words(words: list[str]) -> dict[str, int]:
    """Count occurrences of each word using collections.Counter."""
    return dict(Counter(words))
    raise NotImplementedError


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    """Group scores by student name using collections.defaultdict(list)."""
    groups = defaultdict(list)
    for name, score in records:
        groups[name].append(score)
    return dict(groups)
    raise NotImplementedError


def rotate_queue(items: list[str], steps: int) -> list[str]:
    q = deque(items)
    q.rotate(steps)
    return list(q)
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    raise NotImplementedError


def safe_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None
    """Convert string to int, returning None if conversion fails."""
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    """Read a text file with a context manager and return non-empty stripped lines."""
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]
    raise NotImplementedError


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    """Return top `n` scores in descending order."""
    return sorted(scores, reverse=True)[:n]
    raise NotImplementedError


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    """Return True if every score is >= threshold."""
    return all(score >= threshold for score in scores)
    raise NotImplementedError
