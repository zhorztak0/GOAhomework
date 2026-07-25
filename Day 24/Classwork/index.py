# 1) შექმენით ფუნქცია სახელად greet, რომელიც დაბეჭდავს მისალმების ტექსტებს. "Hello World!" და "Hello {name}".

def greet():
    print("Hello World!")

greet()

name='tako'

def greet(name):
    print(f"hello {name}")

greet(name)


# 2) შექმენი ფუნქცია double, რომელიც მიიღებს პარამეტრად 1 ცალ რიცხვს და თქვენი დავალებაა დააბრუნებინოთ ამ ფუნქციას აკვადრატებული რიცხვი.

def double(num):
    return num ** 2

print(double(5))


# 3) შექმენი ფუნქცია checkOdd, რომელიც მიიღებს პარამეტრად 1 ცალ რიცხვს და თქვენი დავალებაა დააბრუნებინოთ ფუნქიას "ლუწი" თუ რიცხვი ლუწია, და "კენტი" თუ კენტია.

def checkOdd(num):
    if num % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"
    
print(checkOdd(4))
print(checkOdd(3))


# 4) შექმენი ფუნქცია BMI, რომელიც პარამეტრად მიიღებს 2 ცალ რიცხვს (height, weight), თქვენი დავალებაა დააბრუნოთ ამ ადამიანის BMI --> formula: weight / (height * height)

def BMI(height, weight):
    return weight / (height * height)

print(BMI(1.60,50))


# 5) შექმენი ფუნქცია getNameByUpper, რომელიც პარამეტრად მიიღებს მომხმარებლის სახელს. თქვენი დავალებაა ფუნქციაში დააბრუნოთ მომხმარებლის საწყისი სახელი მაღალ რეგისტრში (upperCase). ფუნქციას არგუმენტად გამოძახებისას გადაეცით input-ის მეშვეობით შემოტანილი მომხმარებლის სახელი.

def getNameByUpper(name):
    return name.upper()


user_name=input('Enter your name:')

print(getNameByUpper(user_name))

