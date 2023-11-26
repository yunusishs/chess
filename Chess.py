from tkinter import*

#colour
def _from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

#code simplifier
def x_to_file(x):
    return letters[int((x+size/2)/size)-1]

def y_to_rank(y):
    return 9-int((y+size/2)/size)

def file_to_x(file):
    return letters.index(file)*size+size

def rank_to_y(rank):
    return (9-rank)*size

#board squares

letters='abcdefgh'
size = 64

w = Tk()

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
for r in range(1,9):
    board.create_text(size/4,r*size,text=str(9-r), font=('consolas',16))

for f in letters:
    board.create_text(file_to_x(f),size*9-size/4,text=f.upper(), font=('consolas',16))
    
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

def check_click(event):
    file = x_to_file(event.x)
    rank = y_to_rank(event.y)
    if file not in letters:
        file = None
    if rank not in range(1,9):
        rank = None
    print(file,rank)
    
    
board.bind_all('<Button-1>', check_click)
