from pystyle import *

# رسائل البداية
print(Box.Lines('Learn Python with Alwaleed'))
Write.Print('This program is a calculator\n', Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube('Example 2'))

while True:
    try:
        # إدخال الرقم الأول
        number1 = int(Write.Input('Please enter the first number: ', Colors.purple_to_blue))
        # إدخال العملية الحسابية
        operator = Write.Input('Please enter the operator (+, -, *, /): ', Colors.purple_to_blue)
        # إدخال الرقم الثاني
        number2 = int(Write.Input('Please enter the second number: ', Colors.purple_to_blue))

        # تنفيذ العملية الحسابية
        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        elif operator == '*':
            result = number1 * number2
        elif operator == '/':
            if number2 == 0:
                Write.Print("Error: Division by zero is not allowed.\n", Colors.red_to_yellow, interval=0.1)
                continue
            result = number1 / number2
        else:
            Write.Print("Invalid operator. Please use one of (+, -, *, /).\n", Colors.red_to_yellow, interval=0.1)
            continue

        # طباعة النتيجة
        Write.Print(f"The result is: {result}\n", Colors.green_to_blue, interval=0.1)
        break

    except ValueError:
        # التعامل مع الأخطاء
        Write.Print("Invalid input. Please enter valid numbers.\n", Colors.red_to_yellow, interval=0.1)
