"""List comprehension exercises"""


# def get_vowel_names():
#     """Return a list containing all names given that start with a vowel."""

def get_vowel_names(names_list_input):
    """Return a list containing all names given that start with a vowel."""
    vowel_names_return= []
    vowel_names_return = [name_ for name_ in names_list_input if name_[0].lower() in 'aeiou']  
    return  vowel_names_return


def power_list(input_list):
    """Return a list that contains each number raised to the i-th power."""
    power_index = []
    power_index = [number**i for i,number in enumerate(input_list)]
    return power_index

def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    # flatten_list = []
    # for row in matrix:
    #     for i in row:
    #         item.append(i)
    flatten_list = [i
          for row in matrix 
          for i in row]
    return(flatten_list)


def reverse_difference(nums):
    """Return list subtracted from the reverse of itself.""
    return(nums)"""
    return([(n-m) for n,m in zip(nums,nums[::-1])])


def matrix_add(matrix1,matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    return([
            [(n-m) 
            for n,m in zip(row1,row2)]
            for row1,row2 in zip(matrix1,matrix2)
            ])


def transpose(matrix):
    """Return a transposed version of given list of lists."""
    return([
        list(row)
        for row in zip(*matrix)
    ])

def get_factors(num):
    """Return a list of all factors of the given number."""
    return([r for r in range(1,num+1) if num%r ==0])

def triples(num_input):
    """Return list of Pythagorean triples less than input num."""
    return([(a,b,c)
     for a in range(1,num_input)
     for b in range(a+1,num_input)
     for c in range(b+1,num_input)
     if a**2 +b**2 == c**2])