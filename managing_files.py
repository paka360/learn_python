'''#with open('Paka_intro.txt') as file_object:
    #contents = file_object.read()
    #print(contents) 

filename = 'Paka_intro.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

filename1 = 'pi.txt'
with open(filename1) as file_object:
    for line in file_object:
        print(line.rstrip())

filename1 = 'pi.txt'
with open(filename1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#Writing to a file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I am gradually getting comfortable with programming.\n')
    file_object.write('I should be able to write my own programs at the end of the month.\n')
    file_object.write('I guess persistence really does pay off.')

#Appending to a file
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write('I love the way I am free to create whatever I want to create with a few strokes of the keyboard\n')
    file_object.write('I also love the idea that the only thing limiting me is my imagination. Like I once read in a book as long as I can my imagine it, It can be done.')

#Exercise
#Guest Book
prompt = input("Hello, Welcome to Nabs Lodge. Please provide your name:")
filename = 'guest_book.txt'

while prompt != 'quit':
    with open(filename, 'a') as file_object:
        file_object.write(prompt.title() + '\n')
    prompt = input("Hello, Welcome to Nabs Lodge. Please provide your name:")

#Programming Poll
prompt2 = input('Why do you like programming?')
filename = 'poll_responses.txt'

while prompt2.lower() != 'quit': 
    with open(filename, 'a') as file_object:
        file_object.write(prompt2 + '\n') 
    prompt2 = input('Why do you like programming?')'''

'''
#Exceptions
#print(5/0)

#Using try-except Blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#Using Excetions to prevent crashes
#The ZeroDivisionError
#Test code
print("Give me two numbers, amd I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    answer = int(first_number) / int(second_number)
    print("\nanswer: " + str(answer))

#Resistant Code
print("Give me two numbers, amd I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print("\nanswer: " + str(answer))
'''

'''
#The FileNotFoundError Exception
#Test code
filename = 'alice.txt'

with open(filename) as file_object:
    contents = file_object.read()
'''

'''
#Resistant Code
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
'''

'''
#Analyzing Text
filename = 'programming.text'
try:
    with open (filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + "does not exist."
    print(msg)
else:
    #Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
'''
    

#To work with multiple files make the code into a function.

def count_words(filename):
    try:
        with open (filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + "does not exist."
        print(msg)
    else:
    #Count the approximate number of words in the file
       words = contents.split()
       num_words = len(words)
       print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'programming.text'
count_words(filename)
