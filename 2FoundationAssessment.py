# # PLEASE USE COMMENT ON/OFF TO WORK PROGRAM WITHOUT ALL ANSWERS SHOWING
#
# # QUESTION 2.1
def word_isogram(word):
    if word != str(word):
        print("Your word is not a string.")
    else:
        pass

    word = word.lower()
    letters_in_word = set()
    for letter in word:
        if letter in letters_in_word:
            return False
        letters_in_word.add(letter)

    else:
        return True


# print(word_isogram('isogram'))
# print(word_isogram('uncopyrightable'))
# print(word_isogram('ambidextrously'))


# QUESTION 2.2
def test_file():
    print(word_isogram('ball'))  # Will return false as there are two l's in this word, testing lower case letters
    print(word_isogram('ABC'))  # Will return true as there are no repeated letters, testing upper case letters
    print(word_isogram('123'))  # Will return true as it is  as a string and no repeats, testing integers
    print(word_isogram('123ABCC'))  # Will return false as there are two C's, testing alphanumeric with repetition
    print(word_isogram('£!*'))  # Will return false as there are no repeats, testing symbols
    print(word_isogram('Hi Pam'))  # Will return true, testing strings with spaces
    print(word_isogram('  '))  # Will return false as there are two spaces, testing spaces alone


test_file()


def allocation(number_of_students):
    allocated = {}
    max_size_of_class = 30
    min_number_of_students = 2

    if min_number_of_students > number_of_students:
        print('The inputted number of students is too low.')

    number_of_classes = ((number_of_students + max_size_of_class - 1) // max_size_of_class)
    size_of_classes = (number_of_students // number_of_classes)
    leftover_students = (number_of_students % number_of_classes)

    for student in range(leftover_students):
        if int(student) > int(leftover_students):
            allocated["Class " + str(student+1)] = (size_of_classes + 1)

        else:
            allocated["Class" + str(student + 1)] = size_of_classes
    print("With " + str(number_of_students) + " students, there are " + str(number_of_classes) + " classes")

    for student in range(number_of_classes):
        print("Class " + (str(student+1)) + " has: " + str(allocated))
        # Couldn't print off number of students per class


print(allocation(60))
print(allocation(90))



