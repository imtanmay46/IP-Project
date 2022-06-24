from time import sleep

def result():
    result=str(input("Guess the answer to the Hint to unlock the key for the next: "))
    return result

def FileReader():
    global i
    try:
        with open(f'/Users/varul18/Desktop/Ip_Project/Hint{i+2}.txt',"r") as f:
            m1=f.read()
            i+=1
            return m1
    except FileNotFoundError:
        return 'No more hints exist!!'

i=0
def Hint_Provider():
    global i
    try:
        with open(f'/Users/varul18/Desktop/Ip_Project/Answer_to_Hint{i+1}.txt',"r") as f:
            data=f.read()
    except FileNotFoundError:
        return 'No more hints exist!!'
    if data==result():
        print("Right Answer! Here comes your next hint...")
        print(FileReader())
        i+=1
        Hint_Provider()
    else:
        print("Try Again!!")
        Hint_Provider()


print("Welcome to Treasure Hunt, Finding Team 🤝 🤩 !!")
go=str(input("So, are you ready to start? (Yes/No): ")).lower()
if go=='yes':
    print("It's Showtime !!")
    print('\n')
    with open(f'/Users/varul18/Desktop/Ip_Project/Hint1.txt',"r") as f:
        m1=f.read()
        print(m1)
    print('\n')
    Hint_Provider()
elif go=='no':
    sleep(10)
    print("We please request you to start now, you're running short on time !!")
    print('\n')
    with open(f'/Users/varul18/Desktop/Ip_Project/Hint1.txt',"r") as f:
        m1=f.read()
        print(m1)
    print('\n')
    print(Hint_Provider())
else:
    print("Sorry, Wrong choice!")
    print("Please try again...")
    go=str(input("So, are you ready to start? (Yes/No): ")).lower()
    if go=='yes':
        print("It's Showtime !!")
        print('\n')
        with open(f'/Users/varul18/Desktop/Ip_Project/Hint1.txt',"r") as f:
            m1=f.read()
            print(m1)
        print('\n')
        print(Hint_Provider())
    elif go=='no':
        sleep(10)
        print("We please request you to start now, you're running short on time !!")
        print('\n')
        with open(f'/Users/varul18/Desktop/Ip_Project/Hint1.txt',"r") as f:
            m1=f.read()
            print(m1)
        print('\n')
        print(Hint_Provider())
    else:
        print("For selecting neither 'Yes' or 'No', we have imposed a 30 sec time penalty on you 🙂")
        sleep(30)
        go=str(input("So, are you ready to start? (Yes/No): ")).lower()
        if go=='yes':
            print("It's Showtime !!")
            print('\n')
            with open(f'/Users/varul18/Desktop/Ip_Project/Hint1.txt',"r") as f:
                m1=f.read()
                print(m1)
            print('\n')
            print(Hint_Provider())
        else:
            print("Times up, guys... You managed to upset the Hiding Team 🥲🫠")
            print("Game Over !!")