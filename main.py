import string
import random
import os
import time as t
from termcolor import colored as cl

nitrotype = input(cl('boost or classic: ', 'white'))
if nitrotype == 'boost':
  codecount = 24
elif nitrotype == 'classic':
  codecount = 16
else:
  print(cl(nitrotype + ' is an invalid choice.', 'red'))
  t.sleep(2)
  os.system('python3 main.py')

speed = input('slow or fast: ')
if speed == 'slow':
  speed = 0.4
elif speed == 'fast':
  speed = 0.1
else:
  print(cl(speed + ' is an invalid choice.', 'red'))
  t.sleep(2)
  os.system('python3 main.py')

print(cl('generating ' + nitrotype + ' nitro codes...\n', 'green'))

f = open(nitrotype + 'Codes.txt', 'w+')
f.write('do not expect any of these to work, but there always is a chance.\n\n')
f.close()

while True:
  def get_random_string(length):
      random_list = []
      for i in range(length):
          random_list.append(random.choice(string.ascii_uppercase + string.digits))
      return ''.join(random_list)
  code = 'https://discord.gift/' + get_random_string(codecount).lower()

  print(code)

  f = open(nitrotype + 'Codes.txt', 'a+')
  f.write(code + '\n')
  f.close()
  t.sleep(speed)