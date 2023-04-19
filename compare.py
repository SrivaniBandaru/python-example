word = input('enter a line or string: ')


def vowels(x):
    result = []
    for i in x:
        if i in 'aeiou':
            result.append(i)
    return result


def consonent(x):
    result = []
    for i in x:
        if i not in 'aeiou':
            result.append(i)
    return result

if len(word) > 0:
    ask = input('enter "y" to compare: ')
    print(ask)
    response = ask
    if response == 'y' or 'Y':
        ask_1 = input('enter 1 to compare vowels and 2 for consonents: ')
        if int(ask_1) == 1:
            result = vowels(word)
            if len(result) > 0:
                print(f'vowels : {result} exists in given word : {word}')
            else:
                print(f'vowels not found in the given word : {word}')
        if int(ask_1) == 2:
            result = consonent(word)
            if len(result) > 0:
                print(f'cononents : {result} exists in given word : {word}')
            else:
                print(f'cononents not found in the given word : {word}')
            print(result)