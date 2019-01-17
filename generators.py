"""Generator Exercises."""


def is_prime():
    """Return True if candidate number is prime."""


def all_together():
    """String together all items from the given iterables."""


def interleave():
    """Return iterable of one item at a time from each list."""


def translate():
    """Return a transliterated version of the given sentence."""


def parse_ranges(range_string):
    """Return a list of numbers corresponding to number ranges in a string"""
    pairs = (num_pairs.split('-')
        for num_pairs in range_string.split(',')
    )
    return(
                num
                for (start,stop) in pairs
                for num in range(int(start), int(stop)+1)
            )
    

def first_prime_over():
    """Return the first prime number over a given number."""


def is_anagram(string1,string2):
    """Return True if the given words are anagrams."""
    letters1 = (letter.lower()
     for letter in sorted(string1)
     if letter.isalpha()
     )
    letters2 = (letter.lower()
     for letter in sorted(string2)
     if letter.isalpha()
     )
    return(
        sorted(letters1)==sorted(letters2)
    )