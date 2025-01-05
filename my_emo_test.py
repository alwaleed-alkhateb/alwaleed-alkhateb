import emoji
from pystyle import *

print(Box.Lines('Learn Python with Alwaleed'))
Write.Print('This program for emoji\n', Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube('Example 7'))
# استخدام الرموز التعبيرية

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :black_heart:'))
print(emoji.emojize('Python is :white_heart:'))
print(emoji.emojize('Python is :stop_sign:'))



print(emoji.demojize('Python is :👉:'))
print(emoji.demojize('Python is :❌:'))
print(emoji.demojize('Python is :🛑:'))