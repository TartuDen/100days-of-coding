from replit import clear
import time
total_bidders={}
more="y"

def get_bidder(name, bid):
  if type(name)== type(""):
    if type(float(bid))==type(1.0):
      total_bidders[name.upper()]=float(bid)
def winner_is():
  ki=""
  v=0
  for k in total_bidders:
    if total_bidders[k]>v:
      v=total_bidders[k]
      ki=k      
  print(f"And the winner is {ki} with the highest bid {v}")


while more.lower()=="y":
  print("Welcome to the secret auction program.")
  temp_name=input("Your name is: ")
  temp_bid=input("Your bid is:  ")
  get_bidder(temp_name, (temp_bid))
  more=input("Again? Y / N: ")
  clear()
winner_is()
# time.sleep(1)