import string
import random
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
# print(alphabet_list)

no = random.randint(0,26)
n = alphabet_list[no]

# alpha = input('Enter Alphabet : ')
score = 20
while score > 0:
    alpha = input('Enter Alphabet : ')
    # n = 'j'
    if n == alpha:
        print('Correct')
        score += 10
        print(f'Score - {score}\n You WON.')
        break
    else:
        print('wrong guess!!')
        score -= 5
        print(f'Score - {score}')
        continue
if score == 0:
    print('You loss')
