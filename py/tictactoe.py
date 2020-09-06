board =[' ' for x in range(10)]


def insertLetter(letter,pos):
    board[pos]= letter

def spaceisfree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isboardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def isWinner(b,l):
    return ((b[1]== b[2] and b[2]==b[3] and b[3]==l) or
    (b[4]== b[5] and b[5]==b[6] and b[6]==l) or
    (b[7]== b[8] and b[8]==b[9] and b[9]==l) or
    (b[1]== b[4] and b[4]==b[7] and b[7]==l) or
    (b[2]== b[5] and b[5]==b[8] and b[8]==l) or
    (b[3]== b[6] and b[6]==b[9] and b[9]==l) or
    (b[1]== b[5] and b[5]==b[9] and b[9]==l) or
    (b[3]== b[5] and b[5]==b[7] and b[7]==l))

def playermove():
    run = True
    while run:
        move=input('Please select the position to put "X" from 1-9')
        try:
            move =int(move)
            if move>0 and move<10:
                if spaceisfree(move):
                    run =False
                    insertLetter('X',move)

                else:
                    print("Sorry , space occupied already")
            else:
                print("Type a valid number between 1 to 9 ")

        except:
            print("Please type a number")

def computermove():
    possiblemoves=[x for x , letter in enumerate(board) if letter == ' ' and x!=0]
    move=0

    for let in ['0','X']:

        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if isWinner(boardcopy, let):
                move =i
                return move
    corners0pen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            corners0pen.append(i)

    if len(corners0pen)>0:
            move=selectRandom(corners0pen)
            return move

    if 5 in possiblemoves:
        move =5
        return move
        edgesopen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)
    if len(edgesopen)>0:
            move= selectRandom(edgesopen)
            return move
def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the Game")
    printBoard(board)

    while not(isboardfull(board)):
        if not(isWinner(board,'O')):
            playermove()
            printBoard(board)
        else:
            print("Sorry you loose!")
            break

        if not(isWinner(board,'X')):
            move=computermove()
            if move==0:
                print(" ")
            else:
                insertLetter('O',move)
                print("CPu placed at postion ",move,':')
                printBoard(board)
        else:
            print("You win")

    if isboardfull(board):
        print("It's a Tie")


while True:
    x =input("Do you want to play again(y/n)")
    if x.lower()=='y':
        board=[' ' for x in range(10)]
        print('-------------------')
        main()
    else:
        break
