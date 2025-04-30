num_rows = 5#int(input("Enter the number of rows: "))
for i in range(1, num_rows + 1):
    for j in range(i):
        print('*', i, end='')
        
       
num_rows = int(input("Enter the number of rows: "))
i = 1
while i <= num_rows:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1
    
    
    
    
  