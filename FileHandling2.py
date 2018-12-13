

f = open('mine.jpg','rb')

f1 = open('image.jpg','wb')
for i in f:
    f1.write(i)

