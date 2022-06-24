class Hint:
    def __init__(self,Location,puzzle,ans):
        self.locate=Location
        self.hint=puzzle
        self.ans=ans
    def location(self):
        return self.locate
    def hints(self):
        return self.hint
    def answer(self):
        return self.ans

print("Hey, Representative from the Hiding Team!!")
print("We really hope you have a lovely time playing this online Treasure Hunt 😃🤩")
print("But, before that....")
print("We request you to make the game exciting at your end by providing us with hints/cues (We promise to not reveal any of those to the Finding Team, Have Faith 😌) that you'd want to give to the Finding Team, to make their Search; exciting & challenging!!")
print('\n')
cues=int(input("Please enter the Number of Hints you'd like to give to the Finding Team: "))

try:
    assert type(cues)==int
except Exception:
    print("Haha! It's good to be playful while playing a game, but please provide us with a lovely looking integral/numerical value 😁")
    cues=int(input("Please enter the Number of Hints you'd like to give to the Finding Team: "))

for i in range(cues):
    try:
        print('\n')
        print("A typical hint consists of giving an appropriate nearby place/location of finding the next hint along with a puzzle/riddle for the Finding Team to decode/solve!")
        print("P.S. : 'Hints would be given as it is to the other team, so please frame accordingly!' ")
        print('\n')
        Location=str(input(f'Please give a suitable location/place for finding the next hint,i.e., Hint {i+2}: '))
        Riddle=str(input(f'Please give a riddle/puzzle for Hint {i+1}: '))
        print('\n')
        Answer=str(input(f'Please provide an answer to the corresponding hint,i.e., Hint {i+1} (We promise not to reveal the Answer until the Finding Team themselves discover it 🤝): '))
        print('\n')
        H=Hint(Location,Riddle,Answer)
        with open(f'/Users/varul18/Desktop/Ip_Project/Hint{i+1}.txt',"w") as f:
            f.write(str(H.location()))
            f.write('\n')
            f.write(str(H.hints()))
        with open(f'/Users/varul18/Desktop/Ip_Project/Answer_to_Hint{i+1}.txt',"w") as f:
            f.write(str(H.answer()))
    except ValueError:
        print(f'Sorry to say, Hint {i+1} was wrecked due to Invalid Input at your end 🫠')
        print("Please don't be playful with us, coz u can not handle our playfullness 😎 !!")
        print("Do provide us with correct input on the next turn 🌹🤓")