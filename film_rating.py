# Film rating exercise
print('Welcome to ShowBox Pictures!')
user_age = int(input('Please enter your age'))

if user_age >= 18:
    print('Based on your age you can view movies rated')
    print('PEGI G, PEGI PG, PEGI 12, PEGI 15 PEGI 18')
elif user_age >= 15:
    print('Based on your age you can view movies rated')
    print('PEGI G, PEGI PG, PEGI 12, PEGI 15')
elif user_age >= 12:
    print('Based on your age you can view movies rated')
    print('PEGI G, PEGI PG, PEGI 12')
elif user_age >= 5:
    print('Based on your age you can view movies rated')
    print('PEGI G, PEGI PG')