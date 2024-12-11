from pystyle import *

# رسائل البداية
print(Box.Lines('Learn Python with Alwaleed'))
Write.Print('This program is for the login page.\n', Colors.purple_to_red, interval=0.1)
Write.Print('Write username and password.\n\n', Colors.purple_to_blue, interval=0.1)
print(Box.DoubleCube('Example1'))

# الرسائل والقوائم
message = '''Enter your choice:
1 - Add admin
2 - Delete admin
3 - Show admins
4 - Exit
'''

admin_list = []

# إضافة إدمن
def add_admin():
    admin_name = input('Enter admin name: ')
    admin_list.append(admin_name)
    print(f"Admin '{admin_name}' added successfully.")

# حذف إدمن
def delete_admin():
    admin_name = input('Enter admin name to delete: ')
    if admin_name in admin_list:
        admin_list.remove(admin_name)
        print(f"Admin '{admin_name}' deleted successfully.")
    else:
        print(f"Admin '{admin_name}' not found in the list.")

# عرض الإدمنز
def show_admin():
    if admin_list:
        print("Admin list:", admin_list)
    else:
        print("No admins found.")

# البرنامج الرئيسي
while True:
    username = Write.Input('Write username: ', Colors.white_to_blue)
    password = Write.Input('Write password: ', Colors.white_to_blue)
    
    if username == 'alwaleed' and password == '12345678':
        Write.Print('Welcome, admin!\n', Colors.purple_to_blue, interval=0.1)
        
        while True:
            choice = int(Write.Input(message, Colors.blue_to_red))
            
            if choice == 1:
                add_admin()
            elif choice == 2:
                delete_admin()
            elif choice == 3:
                show_admin()
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                exit()  # للخروج من البرنامج
            else:
                print("Invalid choice. Please try again.")
    else:
        Write.Print('Username or password is incorrect.\n', Colors.purple_to_blue,interval=0.1)

        



