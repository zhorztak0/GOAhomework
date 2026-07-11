# 2) კომენტარების სახით ახსენით თუ რა დანიშნულება აქვთ .append(); .insert() და .pop() ფუნქციებს.

# .append() - ფუნქცია საშუალებას გვაძლევს,რომ სიას ბოლოს დავამატოთ ახალი ელემენტი.
# .insert() - ფუნქცია საშუალებას გვაძლევს,რომ სიაში ნებისმიერ ინდექსზე ჩავამატოთ ახალი ელემენტი.
# .pop() - ფუნქცია საშუალებას გვაძლევს,რომ სიიდან ამოვაგდოთ ელემენტი კონკრეტული ინდექსიდან.


# 3) შექმენით რამდენიმე ელენტისგან შემდგარი სია, თქვენი დავალებაა დაბეჭდოთ ამ სიის სიგრძე, ანუ სიაში არსებული ელემენტების რაოდენობა.


fruit=['apple','orange','Peach','blueberry']
fruit_len=len(fruit)
print(fruit_len)


# 4) შექმენით ხარიელი სია სადაც მომხმარებელს 5-ჯერ შემოატანინენებთ რიცხვს, შემდეგ კი დაამატებთ მას სიის ბოლოში append() ფუნქციით.

numbers=[]

for i in range(5):
    number=int(input('Enter number:'))
    numbers.append(number)

print(numbers)


# 5) მოცემულია სია:
# colors = ["red", "green", "blue", "yellow", "purple"]
# თქვენი დავალებაა სიიდან წაშალოთ ბოლო ელემენტი .pop() მეთოდის დახმარებით, შემდეგ კი დაბეჭდოთ განახლებული სია.

colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop(4)
print(colors)


# 6) მოცემულია სია:
# animals = ["dog", "cat", "elephant", "lion"]
# თქვენი დავალებაა insert() მეთოდით ჩასვათ სიტყვა "monkey" სიაში მეორე პოზიციაზე, რის შემდეგაც დაბეჭდავთ განახლებულ სიას.

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(2,"monkey")
print(animals)


# 7) შემქნით ცარიელი სია, სადაც 3-ჯერ input-ის სახით მომხმარებელს შეაყვანინებთ სამი სტუდენტის სახელს და დაამატებთ 
# სიაში append() ფუნქციით. შემდეგ კი ჩასვით "Teacher" სიის თავში, წაშალეთ ბოლო სტუდენტი და დაბეჭდეთ სიის სიგრძე, 
# ასვეე საბოლოო სია.


students_list=[]

for i in range(3):
    students=input('Enter students name:')
    students_list.append(students)

students_list.insert(0,"Teacher")

students_list.pop()

students_list_len=len(students_list)
print(students_list_len)
print(students_list)