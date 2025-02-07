import tkinter  #tk-interface(graphical user interface libary)
def set_tile(row,column):
    global curr_player
    if(game_over):
        return
    if board[row][column]["text"]!="":
        return 
    board[row][column]["text"]=curr_player
    if curr_player==player0:
        curr_player=playerx
    else:
        curr_player=player0
    lebel["text"]=curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns,game_over
    turns += 1
    #horizontally,check 3 rows
    for row in range(3):
        if(board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"] and board[row][0]["text"]!=""):
            lebel.config(text=board[row][0]["text"]+" is the winner",foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_light_gray)
            game_over=True
            return 
    #vertically,check 3 columns
    for column in range(3):
        if(board[0][column ]["text"]==board[1][column]["text"]==board[2][column]["text"] and board[0][column ]["text"]!=""):
            lebel.config(text=board[0][column]["text"]+" is the winner",foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow,background=color_light_gray)
            game_over=True
            return 
    #diagonally
    if(board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]and board[0][0]["text"]!="" ):
        lebel.config(text=board[0][0]["text"]+" is the winner",foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow,background=color_light_gray)
        game_over=True
        return 
    
def new_game():
    pass
playerx="x"
player0="0"
curr_player=playerx
board=[[0,0,0],
       [0,0,0,],
       [0,0,0]]
color_blue="#4584b6"
color_yellow="#ffde57"
color_gray="#343434"
color_light_gray="#646464"
turns=0
game_over=False
#window setup
window=tkinter.Tk()  #create a window
window.title("Tic tac toe")
window.resizable(False,False)
frame=tkinter.Frame(window)
lebel=tkinter.Label(frame,text=curr_player+"'s trun",font=("consolas",20),background=color_gray,foreground="white")
lebel.grid(row=0,column=0,columnspan=3,sticky="we")
for row in range (3):
    for column in range(3):
        board[row][column]=tkinter.Button(frame,text="",font=("consolas",50,"bold"),background=color_gray,foreground=color_blue,width=4,height=1,command=lambda row=row,column=column:set_tile(row,column))  #if you have a grid of tiles (like a Tic-Tac-Toe board), and each tile is associated with a specific row and column, this command ensures that when a tile is clicked, the appropriate function (set_tile) is called with the correct coordinates
        board[row][column].grid(row=row+1,column=column)
button=tkinter.Button(frame,text="restart",font=("Consolas",20),background=color_gray,foreground="white",command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")
frame.pack()
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_heaight=window.winfo_screenheight()
winddow_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_heaight/2)-(window_height/2))
#formate "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{winddow_x}+{window_y}")
window.mainloop()