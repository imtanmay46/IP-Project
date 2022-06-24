secret=str(input("Enter the Treasure you'd want to hide: "))
dict={'a':'@','e':'#','i':'!','o':'$','u':'*'}
string=''
for i in secret:
    if i in dict:
        string+=dict[i]
    else:
        string+=i
with open("/Users/varul18/Desktop/Ip_Project/Secret.txt","w") as f:
    f.write(f'{string}')