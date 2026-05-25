# 1) ახსენი კომენტარების სახით რა არის while loop

# 2) შექმენი ცვლადი secret_pass რომელშიც შეინახავ რაიმე მნიშვნელობას, მომხმარებელს შემოატანინე პაროლი, სანამ ეს პაროლები არ დაემთხვევა იქამდე დაუბეჭდე 'try again' და თავიდან შემოატანინე
# როცა სწორად შემოიტანს დაუბეჭდე 'access granted'


# while loop არის ციკლი,რომელიც კოდს ამეორბეს იქამდე მანამ არ იქნება სწორი.


# secret_pass = 'python'
# password_inp = input('enter pass: ')

# while secret_pass != password_inp:
#       print('try again')
#       password_inp = input('enter pass: ')

# print('access granted')


# 3) მოსწავლეს შემოატანინე მიღებული ქულა(int)
# თუ ქულა არის:
# 90-100 --> 'A'
# 70-89 --> 'B'
# 50-69 --> 'C'
# <50 --> 'F-'


# point=int(input('enter your point:'))

# if point >= 90 and point >= 100:
#     print('A')
# elif point >= 70 and point >= 89:
#     print('B')
# elif point >=50 and point >= 69:
#     print('C')
# elif point < 50:
#     print('F')
# else:
#     print(0)


# 4) შექმენი სია names რომელშიც გექნება მოცემული 5 სახელი, შემდეგ index - ის დახმარებით დაბეჭდე პირველი და ბოლო ელემენტი ამ სიის. ასევე index - ის დახმარებით შეცვალე სიის მესამე ელემენტი


# name=['Tako','gio','salome','natali','tekla']
# print(name[0], name[4])
# name[2] = 'any'