import string


def generate_pattern(size):
  '''prints a pattern based off an alphabet slice of length `size`'''
  alphabet = string.ascii_lowercase[:size]
  reverse_alphabet = alphabet[::-1]
  alphabet_palindrome = reverse_alphabet + alphabet[1:]
  max_line_length = len('-'.join(alphabet_palindrome))
  ascending_rows = []


  def create_row(letters):
    filled_row = letters.center(max_line_length, '-')
    ascending_rows.append(filled_row)


  for index, char in enumerate(reverse_alphabet):
    if index == 0:
      create_row(char)
    else:
      letters = reverse_alphabet[:index + 1] + alphabet[len(alphabet) - index:]
      dashed_letters = '-'.join(letters)
      create_row(dashed_letters)
  
  descending_rows = (ascending_rows[::-1])[1:]
  rows = ascending_rows + descending_rows
 
  for row in rows:
    print(row)


generate_pattern(10)
