# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.



def display_board(board):
    for row in board:
        print("===================")
        print("|  "+list(row[0].values())[0]+
        "  |  "+list(row[1].values())[0]+
        "  |  "+list(row[2].values())[0]+"  |  ")
    print("===================")
  
  
  
def check_status(board,symbol):
    cb=[]
    for i in board:
      temp=[]
      for j in i:
          cb.append(list(j.values())[0])
          
    # row_check
    if ((cb[0]==symbol and cb[1]==symbol and cb[2]==symbol) or
       (cb[3]==symbol and cb[4]==symbol and cb[5]==symbol) or
       (cb[6]==symbol and cb[7]==symbol and cb[8]==symbol)):
       return True
    
    #column_check
    elif ((cb[0]==symbol and cb[3]==symbol and cb[6]==symbol)or
       (cb[1]==symbol and cb[4]==symbol and cb[7]==symbol) or
       (cb[2]==symbol and cb[5]==symbol and cb[8]==symbol)):
       return True
    
    #diagonal check
    elif ((cb[0]==symbol and cb[4]==symbol and cb[8]==symbol) or (cb[2]==symbol and cb[4]==symbol and cb[6]==symbol)):
        return True
    
    else:
        return False
        
        
     
      


              

def change_value(turn,board,pos,symbol):
    if pos in range(1,4):
        row_index=0
    elif pos in range(4,7):
        row_index=1
    else:
        row_index=2
    for i in range(0,len(board[row_index])):
        if list(board[row_index][i].keys())[0]==pos:
            board[row_index][i][pos]=symbol
            break
            
    
    status=check_status(board,symbol)
        
    return status
    
def again_game():
    re=""
    while re not in ['y','n']:
      re=input("\n Do you want to continue!! (y/n)")
      if re not in ['y','n']:
         print("Invalid input, please enter y or n")
    return re
    
    


def main():
    board=[[{1:"#"},{2:"#"},{3:"#"}],
    [{4:"#"},{5:"#"},{6:"#"}],
    [{7:"#"},{8:"#"},{9:"#"}]]
    positions=[1,2,3,4,5,6,7,8,9]
    pos=99
    turn=1
    player_1,player_2="",""
    k="d"
    print("******************")
    print("TIC TAC TOE")
    print("******************")
    while player_1 not in ["x","o"]:
       player_1=input("PLAYER 1, do you want to be x or o :")
       if player_1 not in ["x","o"]:
           print("Sorry, please enter x or o")
       else:
           player_2="o" if player_1 == "x" else "x"
    
    print("Player 1 is",player_1,"and player 2 is",player_2)
    
    print("\n********* Let the Game begin !!!!********************\n")
    
    
    
    while True:
        while pos not in positions:
          display_board(board)
          print("\nPlAYER "+str(turn)+" choose your position")
          print("Available vacant positions",positions)
          print("")
          pos=int(input("Choose any one of the mentioned positions in the above list"))
          if pos not in positions:
              print("Please enter valid or mentioned positions")
          else:
              if turn==1:
                  s=change_value(turn,board,pos,player_1)
              else:
                  s=change_value(turn,board,pos,player_2)
              positions.remove(pos)
              
              # win scenario
              if s:
                 print("\n****************************")
                 print("Player",turn,"wins!!!")
                 print("*****************************")
                 display_board(board)
                 k=again_game()
              
              # if positions expired
              if positions==[] and not s:
                  print("Game has reached draw !!!\n")
                  display_board(board)
                  k=again_game()
                  
              if k =='y':
                 main()
              elif k =='n':
                 print("Goodbye !!!!")
                 break
              else:       
              # Player turns  
                if turn==1:
                    turn=2
                else:
                    turn=1
                
        if k=='n':
            break
                  
                  
                  
main() 
              
              
              
        


  
    
    


    
    
    
    
    
    

    
    
    
    
                
                
            
        
