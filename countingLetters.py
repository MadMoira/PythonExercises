'''
Example:
Input: aaaaabbbbccccccaaaaaaa
Output: 5a4b6c7a
'''


def count_continue_repeated_letters(test_string):

    output_string = ''
    string_length = len(test_string)
    current_letter = None
    count = 0

    for letter_index in range(string_length):

        # If letters are different, modify the current letter
        if current_letter != test_string[letter_index]:
            current_letter = test_string[letter_index]
            count += 1

        # Ending case
        if letter_index + 1 == string_length:
            output_string += str(count) + current_letter
            break

        if test_string[letter_index] != test_string[letter_index+1]:
            output_string += str(count) + current_letter
            count = 0
        else:
            count += 1

    return output_string

result = count_continue_repeated_letters('aaaaabbbbccccccaaaaaaa')
print(result)
