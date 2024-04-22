def sum(a,b,c):
  return a + b + c
def printboard(astate,bstate):
  zero='X' if astate[0] else ('O' if bstate[0] else 0)
  one='X' if astate[1] else ('O' if bstate[1] else 1)
  two='X' if astate[2] else ('O' if bstate[2] else 2)
  three='X' if astate[3] else ('O' if bstate[3] else 3)
  four='X' if astate[4] else ('O' if bstate[4] else 4)
  five='X' if astate[5] else ('O' if bstate[5] else 5)
  six='X' if astate[6] else ('O' if bstate[6] else 6)
  seven='X' if astate[7] else ('O' if bstate[7] else 7)
  eight='X' if astate[8] else ('O' if bstate[8] else 8)
  
  print(f"{zero} | {one} | {two} ")
  print(f"--|---|---")
  print(f"{three} | {four} | {five} ")
  print(f"--|---|---")
  print(f"{six} | {seven} | {eight} ")

def checkwin(astate,bstate):
  awins=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
  for win in awins:
    if sum(astate[win[0]],astate[win[1]],astate[win[2]]) == 3:
      print("A won the match")
      return 1
    if sum(bstate[win[0]],bstate[win[1]],bstate[win[2]]) == 3:
      print("B won the match")
      return 0
      
  return -1
  
if __name__ == "__main__":
  
  astate = [0,0,0,0,0,0,0,0,0]
  bstate = [0,0,0,0,0,0,0,0,0]
  turn = 1
  print("Welcome To Tic-Tax-too Game")
  while True:
    printboard(astate,bstate)
    if turn == 1:
      print("A's Chance")
      value=int(input("Please enter a Value: "))
      astate[value] = 1
    else:
      print("B's Chance")
      value=int(input("Please enter a Value: "))
      bstate[value] = 1
    cwin=checkwin(astate,bstate)
    if cwin != -1:
      print("Match over")
      break
    turn = 1 - turn 

  
