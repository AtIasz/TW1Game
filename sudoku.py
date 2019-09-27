pgTop="╔"+("═"*5+"╦")*2+"═"*5+"╗"
pgBwLine="╠"+("═"*5+"╬")*2+"═"*5+"╣"
pgBot="╚"+("═"*5+"╩")*2+"═"*5+"╝"
#def DrawGame():

  #  print(pgTop)
  #  pgLine="║"+"-"*5+"║"+"-"*5+"║"+"-"*5+"║"
  #  for i in range(3):
  #      print(pgLine)
  #  print(pgBwLine)
  #  for i in range(3):
  #      print(pgLine)
  #  print(pgBwLine)
  #  for i in range(3):
  #      print(pgLine)
  #  print(pgBot)
    # "╬" "╣" "║" "╗" "╝" "╚" "╔" "╩" "╦" "╠" "═" "│"
def andyouPrintItOut():
    print(pgTop)
    print(placeList[0])
    print(placeList[1])
    print(placeList[2])
    print(pgBwLine)
    print(placeList[3])
    print(placeList[4])
    print(placeList[5])
    print(pgBwLine)
    print(placeList[6])
    print(placeList[7])
    print(placeList[8])
    print(pgBot)
whereList=["030000000","000195000","008000060","800060000","400800001","000020000","060000280","000419005","000000070"]
'''
numOzeros=0
for i in range(len(whereList)):
    for j in range(len(whereList[i])):
        if whereList[i][j]=="0":
            numOzeros+=1
while numOzeros!=0:
    try:
        move=str(input(""))


    except ValueError:
'''
        
placeList=["","","","","","","","",""]
ritenou=""
for i in range(len(whereList)): 
    ritenou=""
    for j in range(len(whereList[i])):
        if whereList[i][j]!="0":
            ritenou+=whereList[i][j]
        else:
            ritenou+="-"
    placeList[i]+=("║"+ritenou[0]+"_"+ritenou[1]+"_"+ritenou[2]+"║"+ritenou[3]+"_"+ritenou[4]+"_"+ritenou[5]+"║"+ritenou[6]+"_"+ritenou[7]+"_"+ritenou[8]+"║")
    #for j in range()

andyouPrintItOut()
