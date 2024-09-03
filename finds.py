import csv
num_attr = 6
a = []
print("\n the given training data set\n")
csvfile = open("tennis.csv",'r')
reader = csv.reader(csvfile)
for row in reader:
    a.append(row)
    print(row)
print("the intial hypothesis ")
hypothesis = ['0']*num_attr
print(hypothesis)
for j in range(0,num_attr):
    hypothesis[j]=a[0][j]
for i in range(0,len(a)):
    if(a[i][num_attr]=="yes"):
        for j in range(0,num_attr):
            if(a[i][j]!=hypothesis[j]):
                hypothesis[j]='?'
            else:
                hypothesis[j]=a[i][j]
    print("for training instance no: ",i,"the hypothesis is",hypothesis)
print("the maximally specific hypothesis is",hypothesis)