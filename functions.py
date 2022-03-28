def armstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if num == sum:
       return "Armstrong number"
    else:
       return "not an Armstrong number"

def divisible(num):
    if num % 5==0:
        return "divisible by 5"
    else:
        return "not divisible by 5"

def Largest_of_3num(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z

def even_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__=="__main__":
    # armstrong
    print("to check armstrong or not")
    num=int(input("Enter the Number : "))
    result=armstrong_number(num)
    print(result)

    # divisible by 5 or not
    print("to check divisible by 5 or not")
    num=int(input("Enter the Number : "))
    result=divisible(num)
    print(result)

    # largest among 3 number
    print("to check greatest of 3 numbers")
    x = int(input("Enter num 1 : "))
    y = int(input("Enter num 2 : "))
    z = int(input("Enter num 3 : "))
    result = Largest_of_3num(x, y, z)
    print(result)

    # odd or even
    print("to check odd or even")
    x = int(input("Enter the Number : "))
    result = even_odd(x)
    print(result)