def cal(firstNumber,secondNumber,operation='+'):
    if operation=='+':
        return str(firstNumber+secondNumber)
    elif operation=='-':
        return str(firstNumber-secondNumber)
    elif operation=="*":
        return str(firstNumber*secondNumber)
    elif operation=="/":
        return str(firstNumber/secondNumber)

print('Please input two numbers ')
firstnumber=float(input('firstnumber is : '))
secondenumber=float(input('secondnumber is : '))
operation=input('Pleas input your operation (+ or - or * or / ) :' )
number=cal(firstNumber=firstnumber,secondNumber=secondenumber,operation=operation)
print(number)
