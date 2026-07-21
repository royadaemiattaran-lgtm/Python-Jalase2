# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pyc


alphabetString='ABCDEFGHIJKLMNOPQRSTUYZ'
print(alphabetString[0])
print(alphabetString[12])
print(alphabetString[0:13])
print(alphabetString[0:13:2])
print(alphabetString[:13])
print(alphabetString[2:])
print(alphabetString[-1])
print(alphabetString[-13])
print(alphabetString[13])
print(alphabetString[-1:-10])
print(alphabetString[-3:5:-1])
name='mahdi'
age=18
print('my name is mahdi,i am 18')
print('my name is', name,',i am', age)
print('my name is {} , i am {}'.format(name,age))
print('my name is {1} , i am {0}'.format(name,age))
for number in range (16):
    print('{} to the power of 2 is: {}'.format(number,number**2))

    for number in range(16):
        print('{0:>3} to the power of 2 is: {1:>4}'.format(number, number ** 2))

    print('=' * 40)

age=13
if age>18 :
    print('be senne ghanoni residi')
elif age>15 and age<=18:
    print('B')
elif 12<age<15:
    print('D')
else:
    print('C')


if age :
       print('E')

print('=' *40)

for number in range(1, 101):
    if number % 3 == 0:
        print("Hope")
    elif number % 5 == 0:
        print("Wheeze")
    else:
        print(number)

print('=' *40)



alphabetString='ABCDEFGHIJKLMNOPQRSTUYZ'
for char in  alphabetString:
    print(char)


print('=' *40)


for i in range(len(alphabetString)):
    print(alphabetString[i])

print('=' *40)

for i in range(len(alphabetString) - 1, -1, -1):
    print(alphabetString[i])

print('=' * 40)


for number in range(2, 1001):

    for i in range(2, number):
        if number % i == 0:
            break

    else:
        print(number)


print('=' * 40)




for ind,char in enumerate(alphabetString):
    print('character #{}:{}'.format(ind,char))

print('=' * 40)


counter=0
while counter<5:
    print(f'the count is:{counter}')
    counter=counter+1