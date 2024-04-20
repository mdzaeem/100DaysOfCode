
import random

def swap(a, b):
    return b, a

def display(a,b):
  global returnChoice
  print(data[a]['follower_count'])
  print(data[b]['follower_count'])
  if returnChoice==1:
    print(f"You are right current score is {score}")
    # print(logo)
    print(f"Compare A : {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']} ")
    # print(vs)
    print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']} ")
    return 1
  else:
    # clear()
    print(f"Sorry, that's wrong. Final score: {score}")
    return 0

def compare():
  global score,choice,b,a
  if choice.lower()=='a':
    if data[a]["follower_count"] > data[b]["follower_count"]:
      del data[b]
      score+=1
      a, b = swap(a, b)
      return 1
    else: return 0
  elif choice.lower()=='b':
    if data[a]["follower_count"] < data[b]["follower_count"]:  
      score+=1
      del data[a]  
    #   a=b
      a, b = swap(a, b)
      return 1
    else: return 0


# print(logo)
#printing random
a=random.randint(0,len(data)-1)
b=a
while b == a:
  b=random.randint(0,len(data)-1)

# first display
# print(logo)
print(f"Compare A : {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']} ")
# print(vs)
print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']} ")
print(data[a]['follower_count'])
print(data[b]['follower_count'])
# loop
score=0
returnChoice=1
while returnChoice==1:
  choice=input("Who has more followers? Type 'A' or 'B': ")
  returnChoice=compare()
  if returnChoice==0:
    display(a,b)
    break
  else:
    while b == a:
      b=random.randint(0,len(data)-1)
    display(a,b)