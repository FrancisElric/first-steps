######################################################

def what_word(number, word, i, j):
    if (i % number[j]) == 0:
        return word[j]
    else:
        return ''

def fizz_buzz(last_num, number, word):
    for i in range(1, last_num):
        output = ''
        for j in range(len(number)):
            output += what_word(number, word, i, j)
        if output == '':
            print(i)
        else:
            print(output)

######################################################

word    = ['Fizz', 'Buzz', 'Vazz']
number  = [3, 5, 7]
whenEnd = 100

######################################################

fizz_buzz(whenEnd, number, word)
