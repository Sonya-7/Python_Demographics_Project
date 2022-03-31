print("Sonya's Demographics Project")
print("\t\tWelcome!\n")


                     # name
name_min = 2
name_max = 50
name_count = 0
christian_name = 'What is first your name?'
surname = 'What is last your name? '
name_too_short = "Name must be at lease 2 characters. "
name_too_long = "Name can be a maximum of 50 characters. "

while name_min < name_max:
    first_name = input(christian_name).capitalize()
    if len(first_name) < 3:
        print(name_too_short)
    elif len(first_name) > 50:
        print(name_too_long)
    else:
        break
while name_min < name_max:
    last_name = input(surname).capitalize()
    if len(last_name) < 3:
        print(name_too_short)
    elif len(last_name) > 50:
        print(name_too_long)
    else:
        print("Name accepted\n")
        break
print('Welcome! ' + first_name + ', ' + last_name, "\n")


                    #this year
from datetime import date

this_year = date.today().year
today = date.today()
print(f'Today is {today}', "\n")


                      # DOB
try:
    birth_year = int(input('Birth Year: '))
    age = this_year - birth_year
except Exception:
    print("Invalid value. Please enter numbers only. ")
    while True:
        birth_year = int(input('Birth Year: '))
        age = this_year - birth_year
        print(age)
        break
    
reference_list = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
number = input('What is your favorite #? ')
for character in number:
    output1 = ""
    output1 += reference_list.get(character, "(#undefined)") + " "

new_age = int(age) + int(number)
print(f'In {output1}years you will be {new_age}\n')


                     # Emoji call
def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ":)": "\N{grinning face}",
        ":*": "\U0001F48B",
        "<)": "\U0001F618",
        "<3": "\U0001F496",
        "><": "\U0001F921",
        ":(": "\U0001F622",
        "*)": "\U0001F609"
    }
    output2 = ""
    for word in words:
        output2 += emoji.get(word, word) + " "
    return output2


text = input("What is your favorite emoji? ")
print(emoji_converter(text), "\n")


                                # BMI calculation
weight = int(input("What is your current weight: "))
unit = input('(L)bs or (K)g: ')


def lbs_to_kg(weight):
    weight *= 0.45
    return weight


if unit.upper() == "L":
    print(f"you are {int(lbs_to_kg(weight))} kilos\n")
else:
    print(f"you are {weight} kilos\n")

height_feet = float(input("Input height... feet: "))
height_inches = float(input("\t\tinches: "))


def height_in_meters():
    return ((height_inches * 0.0833) + height_feet) * 0.3048


print(f"You are {height_in_meters()} meters\n")
if unit.lower() == "l":
    bmi = lbs_to_kg(weight) / height_in_meters() ** 2
else:
    bmi = weight / height_in_meters() ** 2
if bmi <= 18.5:
    print("Your BMI is: ", bmi, "-underweight\n")
elif 18.5 <= bmi < 25:
    print("Your BMI is: ", bmi, "-normal\n")
elif 25 <= bmi < 30:
    print("Your BMI is: ", bmi, "-overweight\n")
elif bmi >= 30:
    print("Your BMI is: ", bmi, "-obese\n")


              # favorite color
fav_color = input('What is your favorite color?')


            # Summary
print(f'\n\n{last_name}, {first_name} is {age} and has a BMI of {bmi} as at {this_year}. {first_name[0]}{last_name[0]} '
      f'likes the color {fav_color}, and the emoji {emoji_converter(text)}.')


               # thank you email formatting
email = '''
        Thank you for your participation.
        
        Regards,
        Support Team
'''
print(email)