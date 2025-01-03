from pystyle import *

# رسائل البداية
print(Box.Lines('Learn Python with Alwaleed'))
Write.Print('This program is for the multiplication table.\n', Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube('Example 3'))

while True:
    user_input = Write.Input('Enter a number (or Q to quit): ', Colors.purple_to_blue)
    
    # التحقق مما إذا كان المستخدم يريد الخروج
    if user_input.upper() == 'Q':
        Write.Print("Exiting the program. Goodbye!\n", Colors.green_to_blue, interval=0.1)
        break

    try:
        # تحويل الإدخال إلى عدد صحيح
        number1 = int(user_input)

        # طباعة جدول الضرب
        for i in range(1, 11):
            print(f"{number1} X {i} = {number1 * i}")
    except ValueError:
        # التعامل مع الإدخال غير الصحيح
        Write.Print("Invalid input. Please enter a number or 'Q' to quit.\n", Colors.red_to_yellow, interval=0.1)
