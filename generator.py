import string


def generate_pattern(symbols=[], separator='-', size=12, centerpiece=''):
  '''
  prints a pattern based off of provided symbols
  if no symbols provided, uses alphabet slice of length `size`
  '''
  symbols = symbols if symbols else string.ascii_lowercase[:size]
  reverse_symbols = symbols[::-1]
  max_symbols_palindrome = reverse_symbols + symbols[1:]
  # derive width of pattern by creating row at its widest
  max_row_length = len(separator.join(max_symbols_palindrome))
  ascending_rows = []
 

  def create_row(letters):
    filled_row = letters.center(max_row_length, separator)
    ascending_rows.append(filled_row)

 
  for index, char in enumerate(reverse_symbols):
    if index == 0:
      create_row(char)
    else:
      if centerpiece and index == len(reverse_symbols) - 1:
        symbols_palindrome = reverse_symbols[:index] + [centerpiece] + symbols[len(symbols) - index:]
      else:
        symbols_palindrome = reverse_symbols[:index + 1] + symbols[len(symbols) - index:]
      separated_symbols_palindrome = separator.join(symbols_palindrome)
      create_row(separated_symbols_palindrome)
  # concat descending rows to the ascending rows
  rows = ascending_rows + (ascending_rows[::-1])[1:]

  for row in rows:
    print(row)


# print alphabet range
for num in range(2, 27):
  generate_pattern(size=num)
  print('\n')


# print emoji pattern
# emojis = [emoji for emoji in '🥵😱😧']
# generate_pattern(symbols=emojis * 2, separator='💀', centerpiece='👹')