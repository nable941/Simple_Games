import random

class tictactoe():
    def __init__(self) -> None:
        self.boardstate = {"a1":" ", "a2":" ", "a3":" ",
                           "b1":" ", "b2":" ", "b3":" ",
                           "c1":" ", "c2":" ", "c3":" "}
        self.boardvalue = {"a1":0, "a2":0, "a3":0,
                           "b1":0, "b2":0, "b3":0,
                           "c1":0, "c2":0, "c3":0}
        self.gamestate = 0
        self.turn = 0

    def print_board(self):
        print("  1 2 3")
        print("A \033[4m"+ self.boardstate['a1']+"|"+self.boardstate['a2']+"|"+self.boardstate['a3']+"\033[0m")
        print("B \033[4m"+ self.boardstate['b1']+"|"+self.boardstate['b2']+"|"+self.boardstate['b3']+"\033[0m")
        print("C "+ self.boardstate['c1']+"|"+self.boardstate['c2']+"|"+self.boardstate['c3'])


    def comp_move(self):
        #check if there are any available moves left and up turn counter else it is a tie
        if self.turn <9:
            self.turn +=1
        else:
            self.gamestate = 3
            return
        #Check for possible winning moves first
        if (self.boardvalue['a1']+self.boardvalue['a2']+self.boardvalue['a3'])==10:
            if self.boardvalue['a1']==0:
                self.boardvalue['a1']= 5
                self.boardstate['a1']= "O"
                self.gamestate = 2
            elif self.boardvalue['a2']==0:
                self.boardvalue['a2']= 5
                self.boardstate['a2']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['a3']= 5
                self.boardstate['a3']= "O"
                self.gamestate = 2
            return
        if (self.boardvalue['b1']+self.boardvalue['b2']+self.boardvalue['b3'])==10:
            if self.boardvalue['b1']==0:
                self.boardvalue['b1']= 5
                self.boardstate['b1']= "O"
                self.gamestate = 2
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['b3']= 5
                self.boardstate['b3']= "O"
                self.gamestate = 2
            return
        if (self.boardvalue['c1']+self.boardvalue['c2']+self.boardvalue['c3'])==10:
            if self.boardvalue['c1']==0:
                self.boardvalue['c1']= 5
                self.boardstate['c1']= "O"
                self.gamestate = 2
            elif self.boardvalue['c2']==0:
                self.boardvalue['c2']= 5
                self.boardstate['c2']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['c3']= 5
                self.boardstate['c3']= "O"
                self.gamestate = 2
            return
        if (self.boardvalue['a1']+self.boardvalue['b2']+self.boardvalue['c3'])==10:
            if self.boardvalue['a1']==0:
                self.boardvalue['a1']= 5
                self.boardstate['a1']= "O"
                self.gamestate = 2
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['c3']= 5
                self.boardstate['c3']= "O"
                self.gamestate = 2
            return
        if (self.boardvalue['c1']+self.boardvalue['b2']+self.boardvalue['a3'])==10:
            if self.boardvalue['c1']==0:
                self.boardvalue['c1']= 5
                self.boardstate['c1']= "O"
                self.gamestate = 2
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['a3']= 5
                self.boardstate['a3']= "O"
                self.gamestate = 2
            return
        if (self.boardvalue['a1']+self.boardvalue['b1']+self.boardvalue['c1'])==10:
            if self.boardvalue['a1']==0:
                self.boardvalue['a1']= 5
                self.boardstate['a1']= "O"
                self.gamestate = 2
            elif self.boardvalue['b1']==0:
                self.boardvalue['b1']= 5
                self.boardstate['b1']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['c1']= 5
                self.boardstate['c1']= "O"
                self.gamestate = 2
            return
        if (self.boardvalue['a2']+self.boardvalue['b2']+self.boardvalue['c2'])==10:
            if self.boardvalue['a2']==0:
                self.boardvalue['a2']= 5
                self.boardstate['a2']= "O"
                self.gamestate = 2
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['c2']= 5
                self.boardstate['c2']= "O"
                self.gamestate = 2
            return
        if (self.boardvalue['a3']+self.boardvalue['b3']+self.boardvalue['c3'])==10:
            if self.boardvalue['a3']==0:
                self.boardvalue['a3']= 5
                self.boardstate['a3']= "O"
                self.gamestate = 2
            elif self.boardvalue['b3']==0:
                self.boardvalue['b3']= 5
                self.boardstate['b3']= "O"
                self.gamestate = 2
            else:
                self.boardvalue['c3']= 5
                self.boardstate['c3']= "O"
                self.gamestate = 2
            return
        #check for blocks next
        if (self.boardvalue['a1']+self.boardvalue['a2']+self.boardvalue['a3'])==2:
            if self.boardvalue['a1']==0:
                self.boardvalue['a1']= 5
                self.boardstate['a1']= "O"
            elif self.boardvalue['a2']==0:
                self.boardvalue['a2']= 5
                self.boardstate['a2']= "O"
            else:
                self.boardvalue['a3']= 5
                self.boardstate['a3']= "O"
            return
        if (self.boardvalue['b1']+self.boardvalue['b2']+self.boardvalue['b3'])==2:
            if self.boardvalue['b1']==0:
                self.boardvalue['b1']= 5
                self.boardstate['b1']= "O"
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
            else:
                self.boardvalue['b3']= 5
                self.boardstate['b3']= "O"
            return
        if (self.boardvalue['c1']+self.boardvalue['c2']+self.boardvalue['c3'])==2:
            if self.boardvalue['c1']==0:
                self.boardvalue['c1']= 5
                self.boardstate['c1']= "O"
            elif self.boardvalue['c2']==0:
                self.boardvalue['c2']= 5
                self.boardstate['c2']= "O"
            else:
                self.boardvalue['c3']= 5
                self.boardstate['c3']= "O"
            return
        if (self.boardvalue['a1']+self.boardvalue['b2']+self.boardvalue['c3'])==2:
            if self.boardvalue['a1']==0:
                self.boardvalue['a1']= 5
                self.boardstate['a1']= "O"
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
            else:
                self.boardvalue['c3']= 5
                self.boardstate['c3']= "O"
            return
        if (self.boardvalue['c1']+self.boardvalue['b2']+self.boardvalue['a3'])==2:
            if self.boardvalue['c1']==0:
                self.boardvalue['c1']= 5
                self.boardstate['c1']= "O"
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
            else:
                self.boardvalue['a3']= 5
                self.boardstate['a3']= "O"
            return
        if (self.boardvalue['a1']+self.boardvalue['b1']+self.boardvalue['c1'])==2:
            if self.boardvalue['a1']==0:
                self.boardvalue['a1']= 5
                self.boardstate['a1']= "O"
            elif self.boardvalue['b1']==0:
                self.boardvalue['b1']= 5
                self.boardstate['b1']= "O"
            else:
                self.boardvalue['c1']= 5
                self.boardstate['c1']= "O"
            return
        if (self.boardvalue['a2']+self.boardvalue['b2']+self.boardvalue['c2'])==2:
            if self.boardvalue['a2']==0:
                self.boardvalue['a2']= 5
                self.boardstate['a2']= "O"
            elif self.boardvalue['b2']==0:
                self.boardvalue['b2']= 5
                self.boardstate['b2']= "O"
            else:
                self.boardvalue['c2']= 5
                self.boardstate['c2']= "O"
            return
        if (self.boardvalue['a3']+self.boardvalue['b3']+self.boardvalue['c3'])==2:
            if self.boardvalue['a3']==0:
                self.boardvalue['a3']= 5
                self.boardstate['a3']= "O"
            elif self.boardvalue['b3']==0:
                self.boardvalue['b3']= 5
                self.boardstate['b3']= "O"
            else:
                self.boardvalue['c3']= 5
                self.boardstate['c3']= "O"
            return
        #Otherwise look for random spot. if available take it otherwise look for new random spot
        needsspot = True
        row = {1:"a", 2:"b",3:"c"}
        while needsspot:
            ran1 = random.randint(1,3)
            ran2 = str(random.randint(1,3))
            randkey = row[ran1] + ran2
            if self.boardvalue[randkey] == 0:
                self.boardvalue[randkey] = 5
                self.boardstate[randkey]= "O"
                needsspot = False
        return

    def player_move(self, grid):
        allowed = ["a1","a2","a3",
                   "b1","b2","b3",
                   "c1","c2","c3"]
        if grid in allowed:
            if self.boardvalue[grid]== 0:
                self.boardvalue[grid] = 1
                self.turn += 1
                self.boardstate[grid]="X"
                return
            else:
                print("That space is taken.")
                move = input("Which square do you want? ")
                return self.player_move(move)
        else:
            print("That is not a valid square.")
            move = input("Which square do you want? ")
            return self.player_move(move)

    def check_player_win(self):
        if (self.boardvalue['a1']+self.boardvalue['a2']+self.boardvalue['a3'])==3:
            self.gamestate = 1
        elif (self.boardvalue['b1']+self.boardvalue['b2']+self.boardvalue['b3'])==3:
            self.gamestate = 1
        elif (self.boardvalue['c1']+self.boardvalue['c2']+self.boardvalue['c3'])==3:
            self.gamestate = 1
        elif (self.boardvalue['a1']+self.boardvalue['b2']+self.boardvalue['c3'])==3:
            self.gamestate = 1
        elif (self.boardvalue['c1']+self.boardvalue['b2']+self.boardvalue['a3'])==3:
            self.gamestate = 1
        elif (self.boardvalue['a1']+self.boardvalue['b1']+self.boardvalue['c1'])==3:
            self.gamestate = 1
        elif (self.boardvalue['a2']+self.boardvalue['b2']+self.boardvalue['c2'])==3:
            self.gamestate = 1
        elif (self.boardvalue['a3']+self.boardvalue['b3']+self.boardvalue['c3'])==3:
            self.gamestate = 1
        elif self.turn == 9:
            self.gamestate = 3

    def check_gamestate(self):
        if self.gamestate > 0:
            if self.gamestate == 1:
                print("Player wins!")
                game.print_board()
                playgame = False
                return playgame
            elif self.gamestate == 2:
                print("Computer wins!")
                game.print_board()
                playgame = False
                return playgame
            else:
                print("tie game!")
                game.print_board()
                playgame = False
                return playgame
        playgame = True
        return playgame

playgame = True
game = tictactoe()
while playgame:
    game.print_board()
    move = input("Pick your square. ")
    game.player_move(move)
    game.print_board()
    game.check_player_win()
    playgame = game.check_gamestate()
    if not playgame:
        break
    print("My turn!")
    game.comp_move()
    playgame = game.check_gamestate()
