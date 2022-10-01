## PROBLEM
"""
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

Input
The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

Output
Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.
"""

## SOLUTION
## Created with my 9-year-old friend + student, Brayden Lin.
num_of_words = int(input())
word_list = []
i = 0
while i < num_of_words: 
  word = input()
  word_list.append(word)
  i += 1

i = 0

for i in word_list:
  if len(i) > 10:
    ## the variable "hi" is a concatenated string of the first character, the last character, and the number of characters in between.
    hi = i[0] + str(len(i)-2) + i[-1]
    print(hi)
  else:
    ## ultimately it doesn't matter if it's a short word, soooooooooo
      print(i)
