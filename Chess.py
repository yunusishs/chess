from tkinter import*

w = Tk()
#colour
def _from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

#code simplifier
def x_to_file(x):
    if perspective == 'white':
        return letters[int((x+size/2)/size)-1]
    elif perspective == 'black':
        return letters[8-int((x+size/2)/size)]

def y_to_rank(y):
    if perspective == 'white':
        return 9-int((y+size/2)/size)
    elif perspective == 'black':
        return int((y+size/2)/size)

def file_to_x(file):
    if perspective == 'white':
        return letters.index(file)*size+size
    elif perspective == 'black':
        return (7-letters.index(file))*size+size

def rank_to_y(rank):
    if perspective == 'white':
        return (9-rank)*size
    elif perspective == 'black':
        return (rank)*size

#perspective

perspective = 'white'
def flip_board():
    global perspective
    if perspective == 'white':
        perspective = 'black'
    elif perspective == 'black':
        perspective = 'white'
    setup()

board_flipper = Button(w, text='flip board', font=('consolas',8), command=flip_board)
board_flipper.pack()

def setup():
    global white_pieces, black_pieces, file_holders, rank_holders
    print(perspective)
    #reset board        
    for wp in white_pieces:
        board.delete(wp)
    for bp in black_pieces:
        board.delete(bp)
    white_pieces = []
    for f in letters:
        white_pieces.append(pawn(f, 2, 'white'))
        
    white_pieces.append(knight('b', 1, 'white'))
    white_pieces.append(knight('g', 1, 'white'))
    white_pieces.append(bishop('c', 1, 'white'))
    white_pieces.append(bishop('f', 1, 'white'))
    white_pieces.append(rook('a', 1, 'white'))
    white_pieces.append(rook('h', 1, 'white'))
    white_pieces.append(queen('d', 1, 'white'))
    white_pieces.append(king('e', 1, 'white'))

    black_pieces = []

    for f in letters:
        black_pieces.append(pawn(f, 7, 'black'))
        
    black_pieces.append(knight('b', 8, 'black'))
    black_pieces.append(knight('g', 8, 'black'))
    black_pieces.append(bishop('c', 8, 'black'))
    black_pieces.append(bishop('f', 8, 'black'))
    black_pieces.append(rook('a', 8, 'black'))
    black_pieces.append(rook('h', 8, 'black'))
    black_pieces.append(queen('d', 8, 'black'))
    black_pieces.append(king('e', 8, 'black'))
    #reset coords
    for r in rank_holders:
        board.delete(r)
    for f in file_holders:
        board.delete(f)
    rank_holders = []
    file_holders = []

    for r in range(1,9):
        if perspective == 'white':
            rank_holders.append(board.create_text(size/4,r*size,text=str(9-r), font=('consolas',16)))
        if perspective == 'black':
            rank_holders.append(board.create_text(size/4,r*size,text=str(r), font=('consolas',16)))


    for f in letters:
        file_holders.append(board.create_text(file_to_x(f),size*9-size/4,text=f.lower(), font=('consolas',16)))
    
#board squares

letters='abcdefgh'
size = 64


board = Canvas(w, width=size*9,height=size*9)
board.pack()

for r in range(1,9):
    for f in letters:
        square_color = ''
        if r%2 == (letters.index(f))%2:
            square_color = _from_rgb((236,238,212))
        if r%2 != (letters.index(f))%2:
            square_color = _from_rgb((116,150,84))
        board.create_rectangle(file_to_x(f)+size/2,rank_to_y(r)+size/2, file_to_x(f)-size/2,rank_to_y(r)-size/2, fill=square_color, outline=square_color)

# this places the coordinates
rank_holders = []
file_holders = []

for r in range(1,9):
    rank_holders.append(board.create_text(size/4,r*size,text=str(9-r), font=('consolas',16)))

for f in letters:
    file_holders.append(board.create_text(file_to_x(f),size*9-size/4,text=f.lower(), font=('consolas',16)))
    

#pieces        
white_pawn = PhotoImage(file="white pawn.gif")
white_knight = PhotoImage(file="white knight.gif")
white_bishop = PhotoImage(file="white bishop.gif")
white_rook = PhotoImage(file="white rook.gif")
white_queen = PhotoImage(file="white queen.gif")
white_king = PhotoImage(file="white king.gif")
black_pawn = PhotoImage(file="black pawn.gif")
black_knight = PhotoImage(file="black knight.gif")
black_bishop = PhotoImage(file="black bishop.gif")
black_rook = PhotoImage(file="black rook.gif")
black_queen = PhotoImage(file="black queen.gif")
black_king = PhotoImage(file="black king.gif")

def pawn(file, rank, color):
    if color == 'white':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=white_pawn)
    if color == 'black':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=black_pawn)

def knight(file, rank, color):
    if color == 'white':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=white_knight)
    if color == 'black':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=black_knight)

def bishop(file, rank, color):
    if color == 'white':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=white_bishop)
    if color == 'black':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=black_bishop)

def rook(file, rank, color):
    if color == 'white':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=white_rook)
    if color == 'black':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=black_rook)

def queen(file, rank, color):
    if color == 'white':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=white_queen)
    if color == 'black':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=black_queen)

def king(file, rank, color):
    if color == 'white':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=white_king)
    if color == 'black':
        return board.create_image(file_to_x(file),rank_to_y(rank), image=black_king)
    
#piece placement

white_pieces = []
for f in letters:
    white_pieces.append(pawn(f, 2, 'white'))
    
white_pieces.append(knight('b', 1, 'white'))
white_pieces.append(knight('g', 1, 'white'))
white_pieces.append(bishop('c', 1, 'white'))
white_pieces.append(bishop('f', 1, 'white'))
white_pieces.append(rook('a', 1, 'white'))
white_pieces.append(rook('h', 1, 'white'))
white_pieces.append(queen('d', 1, 'white'))
white_pieces.append(king('e', 1, 'white'))

black_pieces = []

for f in letters:
    black_pieces.append(pawn(f, 7, 'black'))
    
black_pieces.append(knight('b', 8, 'black'))
black_pieces.append(knight('g', 8, 'black'))
black_pieces.append(bishop('c', 8, 'black'))
black_pieces.append(bishop('f', 8, 'black'))
black_pieces.append(rook('a', 8, 'black'))
black_pieces.append(rook('h', 8, 'black'))
black_pieces.append(queen('d', 8, 'black'))
black_pieces.append(king('e', 8, 'black'))

#movement
selection = board.create_rectangle(0,0,0,0, outline='black',width=3)

def check_click(event):
    file = x_to_file(event.x)
    rank = y_to_rank(event.y)
    if file not in letters:
        file = None
    if rank not in range(1,9):
        rank = None
    if not(rank == None or file == None):
        for piece in white_pieces:
            if x_to_file(board.coords(piece)[0])==file and y_to_rank(board.coords(piece)[1])==rank:
                board.coords(selection,file_to_x(file)+size/2,rank_to_y(rank)+size/2, file_to_x(file)-size/2,rank_to_y(rank)-size/2)
                if board.itemcget(piece, 'image') == 'pyimage1':
                    print('')
                if board.itemcget(piece, 'image') == 'pyimage2':
                    print('N')
                if board.itemcget(piece, 'image') == 'pyimage3':
                    print('B')
                if board.itemcget(piece, 'image') == 'pyimage4':
                    print('R')
                if board.itemcget(piece, 'image') == 'pyimage5':
                    print('Q')
                if board.itemcget(piece, 'image') == 'pyimage6':
                    print('K')
        for piece in black_pieces:
            if x_to_file(board.coords(piece)[0])==file and y_to_rank(board.coords(piece)[1])==rank:
                board.coords(selection,file_to_x(file)+size/2,rank_to_y(rank)+size/2, file_to_x(file)-size/2,rank_to_y(rank)-size/2)
                if board.itemcget(piece, 'image') == 'pyimage7':
                    print('')
                if board.itemcget(piece, 'image') == 'pyimage8':
                    print('N')
                if board.itemcget(piece, 'image') == 'pyimage9':
                    print('B')
                if board.itemcget(piece, 'image') == 'pyimage10':
                    print('R')
                if board.itemcget(piece, 'image') == 'pyimage11':
                    print('Q')
                if board.itemcget(piece, 'image') == 'pyimage12':
                    print('K')
    
board.bind_all('<Button-1>', check_click)

