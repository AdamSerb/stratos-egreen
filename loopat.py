'''
successful = False
for number in range(1,4,1):
    print('attempt', number)
    if successful:
        print('successful')
        break
else:
   print('attempted 3 times and failed.')
'''

for x in range(5):
    for y in range(3):
        print(f"{x};{y}")