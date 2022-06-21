from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bidding_details={}
check= True

def find_the_higgest_bidder():
  high=0
  for i in bidding_details:
    bid_amount= bidding_details[i]
    if bid_amount>high:
      high=bid_amount
      highest_bidder=i
    
  print(f"highest bidder is {highest_bidder} and the bidding ammount:{high}  ")
  #print(bidding_details)
while check==True:
  name = input("please enter bider name: th")
  bid = int(input("please enter the bidding ammount: $"))
  bidding_details[name]=bid
  direction= input("please enter 'yes' if you want add more bidders or 'no' if you dont want to\n").lower()
  if direction== 'yes':
    clear()
    check= True
  elif direction== 'no':
    check=False
    find_the_higgest_bidder()
  else:
    print("wrong input")