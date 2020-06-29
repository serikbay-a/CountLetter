def in_input(m,text):
    nums = []
    i=0    
    while i<m:
        try:
            i=i+1  
            n = float(input(text))
            nums.append(n)
        except ValueError:
            print('Можно вводить только числа')
            i=i-1  
    return nums

def count_letters_RU(text):
    first = 0
    last = 0
   
    for i in range(0,10000):
        if chr(i) == 'А':
            first = i
        elif chr(i) == 'я':
            last = i
            break 

    alphabet=[]

    for i in range(first,last+1):
        alphabet.append(chr(i))
    for i in range(0,10000):
        if chr(i) == 'Ё':
            alphabet.append(chr(i))
        elif chr(i) == 'ё':
            alphabet.append(chr(i))
            break
    alphabet.insert(alphabet.index('е')+1,alphabet.pop(-1))
    alphabet.insert(alphabet.index('Е')+1,alphabet.pop(-1))
    counter={}
    for letter in alphabet:
        n=text.count(letter)
        if n!=0:
            counter[letter]=n
    return counter


# from my_lib import count_letters_RU
# import os
# import sys
# import codecs

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# # home_dir = os.getcwd()
# # print('my_lib.py' in os.listdir(home_dir))
# # test_dir = os.path.join(home_dir,'test')
# # if 'test' not in os.listdir(home_dir):
# #   os.mkdir(test_dir)
# # filename = os.path.join(test_dir,'war_peace.txt')
# f = open('war_peace.txt','r')
# data = f.read()
# print(count_letters_RU(data))
# f.close()