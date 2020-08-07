print ("welcome to the text adventure")

options = ["a", "b", "c" ]

name = input("Hello, what is your name? \n ")

print(f"Hello {name}! Let's start the adventure.")

def start():

  print("It's a beautiful sunny summer day but then you hear a loud ")

  for i in range(3):
    print("BOOM")
    print("What's that noise? You look outside of your window and see a ginormous, reptilian, angry dinosaur wreaking havoc onto your city.")

  scene1 = input("What do you do? \n A) Check your phone for social media updates \nB) Grab your family and get into the car \nC) Hide under the bed") 
  while scene1 not in options:
    print ("not valid put a b c") 
    scene1 = input("What do you do? \n A) Check your phone for social media updates \nB) Grab your family and get into the car \nC) Hide under the bed") 



def scene1_socialMedia():
  print("You checked twitter, facebook, snapchat and everything was blank, nothing updated. No news appeared about the monster inside the city. Looks like the entire network is out.")
scene2 = input("What do you do next?")

def scene1_car():
  print("You head to the car with your parents and siblings. All of the sudden ")

  if scene1 == "A":
      scene1_socialMedia()
    elif scene1 == "B":
      scene1_car()
  elif scene1 == "C":
    print("hide bed")
  else:
    print("not valid try again")


if scene2 == "A":
  scene2_socialMedia()
elif scene2 == "B":
  scene1_car()
elif scene2 == "C":
  print("hide bed")
else:
  print("try again, choose a,b or c ")


def main():
  start()

main()

