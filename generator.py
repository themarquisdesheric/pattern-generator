import string


def generate_pattern(size):
  alphabet = string.ascii_lowercase[:size]
  reverse_alphabet = alphabet[::-1]
  alphabet_palindrome = reverse_alphabet + alphabet[1:]
  max_line_length = len('-'.join(alphabet_palindrome))
  ascending_rows = []


  def create_row(letters):
    dash_count = max_line_length - len(letters)
    dashes = (dash_count // 2) * '-'
    return dashes + letters + dashes


  for index, char in enumerate(reverse_alphabet):
    if index == 0:
      ascending_rows.append(create_row(char))
    else:
      letters = reverse_alphabet[:index + 1] + alphabet[len(alphabet) - index:]
      dashed_letters = '-'.join(letters)
      ascending_rows.append(create_row(dashed_letters))
  # concat descending rows to the ascending rows
  rows = ascending_rows + (ascending_rows[::-1])[1:]
 
  for row in rows:
    print(row)


generate_pattern(10)
