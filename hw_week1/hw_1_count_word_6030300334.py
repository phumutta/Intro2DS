from collections import Counter
data = [line.strip() for line in open("C:/Users/phumu/Desktop/AllWork/DATA SCI/message.txt", 'r')]
x=data[0]

tmp=x.split(" ")
count=Counter(tmp)

count.most_common()

i=0
k=0
for key in count.keys():
    k+=1
print("จำนวนคำ : ",k,)
for k,v in count.most_common(5):
    i+=1
    print("อันดับ",i,"",k)

