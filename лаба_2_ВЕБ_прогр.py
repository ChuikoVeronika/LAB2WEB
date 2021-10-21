def palindrom():
    num = int(input("Введите число:")) 
    temp = num
    rev = 0 
    while(num > 0):
        dig = num % 10 
        rev = rev * 10 + dig 
        num = num // 10
        if(temp == rev):
            print("Введенное число является палиндромом")
            return
    print("Введенное число НЕ является палиндромом")


def delenie235():
    lst = []
    tw = []
    th = []
    f = []
    for e in input("Введите числа:").split():
        lst.append(int(e))
    for i in lst:
        if i%2 == 0:
            tw.append(i)
        if i%3 == 0:
            th.append(i)
        if i%5 == 0:
            f.append(i)
    print ("Список для чисел, делящихся на 2: ", tw)
    print ("Список для чисел, делящихся на 3: ", th)
    print ("Список для чисел, делящихся на 5: ", f)

def perevorot():
    n1 = int(input("Введите целое число: "))
    n2 = 0
    while n1 > 0:
        d = n1 % 10
        n1 = n1 // 10
        n2 = n2 * 10
        n2 = n2 + d
    print('Обратное ему число:', n2)

def sqrt():
    A = float(input("Число: "))
    n = int(input("Степень: "))
    x = A/2
    for i in range(1000):
        x = 1/n*((n-1)*x+A/x**(n-1))
    return x

def trufal(n):
   if n < 2:
       return False
   if n == 2:
       return True
   limit = n**(1/2)
   i = 2
   while i <= limit:
       if n % i == 0:
           return False
       i += 1
       return True
   

def ob(y):
    if y == '1':
        f = palindrom()
        print(f)
    elif y=='2':
        f = delenie235()
    elif y =='3':
        f = perevorot()
    elif y =='4':
        print(sqrt())
    elif y == '5':
        print(trufal(int(input("Число: "))))

print ("Выберите задание")
y=input()
ob(y)



