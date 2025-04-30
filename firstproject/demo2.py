file=open('file.txt','w+')
file.write("python practicing here ")
print(file.tell())# to check where is my pointer
file.seek(0)# to set our pointer
data=file.read()
print(data)
file.close()


file=open("images.jpg",'rb')
file1=open('images1.jpg','wb')
for i in file:
    file1.write(i)