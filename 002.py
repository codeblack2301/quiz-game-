questian_num = 0
score = 0
questians = ('1-what is the best food in the world',
             '2-what contry is the largest',
             '3-whats the age of the oldest person in russia',
             '4-what is the hottest planet in the solar system')
options = (('a-pizza','b-hamburguer','c-strogonnof','d-rice and beans'),
           ('a-brasil','b-usa','c-india','d-none of them'),
           ('a-110','b-114','c-115','d-118'),
           ('a-mercury','b-venus','c-earth','d-jupter'))

answers = ('a','d','b','b')

for questian in questians:
    print('--------------')
    print(questian)
    for option in options[questian_num]:
        print(option)
          

    
    
    guess = input('type the answers: (a,b,c,d)')
    if guess == answers[questian_num]:
        score+=1
        print('right')
    else:
        print('wrong')
    questian_num+=1

print(f'your score:{score} congrats!!')





