import os
import random
for i in range(1200):
    # d = str(i) + 'days ago' epochconverter.com
    d = str(random.randint(1494261675, 1620493218))
    with open('bot.txt', 'a') as file:
        file.write (d+'\n')
    os.system('git add bot.txt')
    os.system('git commit --date="'+d+'" -m "slice mesh' + d + '"')

os.system('git push -u origin master')
