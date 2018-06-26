#Hibah Wasim
#10316611
#project5_user_interface.py
#ICS 32 Project 5

import project5_game_logic
import tkinter


class Game_over:
    def __init__(self, sign: str, num_black: int, num_white:int):
        self._sign = sign
        self._black = num_black
        self._white = num_white
        self._game_window = tkinter.Toplevel()

        game_over_label = tkinter.Label(
            master = self._game_window, text = "GAME OVER!")
        game_over_label.grid(row = 0, column = 0, padx = 100, pady = 100, sticky = tkinter.S)

        self._game_window.rowconfigure(0, weight = 1)
        self._game_window.columnconfigure(0, weight = 1)

        self._winner_text = tkinter.StringVar()
        self._winner_text.set('Winner: ')
        
        winner_label = tkinter.Label(
            master = self._game_window, textvariable = self._winner_text)
        winner_label.grid(row = 1, column = 0, padx = 100, pady = 100, sticky = tkinter.N)

        self._winner_text.set(f'{self.winner(self._sign)} WINS')

    def show(self) -> None:
        self._game_window.grab_set()
        self._game_window.wait_window()

    def winner(self, sign) -> None:
        if self._sign == '<':
            if self._black < self._white:
                return  'BLACK'
            elif self._white < self._black:
                return 'WHITE'
            elif self._black == self._white:
                return 'NO ONE'
        elif self._sign == '>':
            if self._black > self._white:
                return 'BLACK'
            elif self._white > self._black:
                return 'WHITE'
            elif self._black == self._white:
                return 'NO ONE'

class Dialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        self.Rows = 0
        self.Columns = 0
        self.first_move = ''
        self.winner = ''

        heading = tkinter.Label(
            master = self._dialog_window, text = "Select Board Options")
        heading.grid(row = 0, columnspan = 2)
        
        row_label = tkinter.Label(
            master = self._dialog_window, text = "Number of Rows")
        row_label.grid(row = 1, column = 0)

        self._entryRows = tkinter.StringVar()
        self._entryRows.set('4')
        enter_rows = tkinter.OptionMenu(self._dialog_window, self._entryRows,
                                        '4', '6', '8', '10', '12', '14', '16')
        enter_rows.grid(row = 1, column = 1)

        column_label = tkinter.Label(
            master = self._dialog_window, text = "Number of Columns")
        column_label.grid(row = 2, column = 0)

        self._entryColumns = tkinter.StringVar()
        self._entryColumns.set('4')
        enter_columns = tkinter.OptionMenu(self._dialog_window, self._entryColumns,
                                        '4', '6', '8', '10', '12', '14', '16')
        enter_columns.grid(row = 2, column = 1)

        move_label = tkinter.Label(
            master = self._dialog_window, text = "First Move")
        move_label.grid(row = 3, column = 0)

        self._entryFirstMove = tkinter.StringVar()
        self._entryFirstMove.set('B')
        enter_first_move = tkinter.OptionMenu(self._dialog_window, self._entryFirstMove,
                                              'B', 'W')
        enter_first_move.grid(row = 3, column = 1)

        winner_label = tkinter.Label(
            master = self._dialog_window, text = "Win with more or less pieces?")
        winner_label.grid(row = 4, column = 0)

        self._entryWinner = tkinter.StringVar()
        self._entryWinner.set('>')

        enter_winner = tkinter.OptionMenu(self._dialog_window, self._entryWinner,
                                              '>', '<')
        enter_winner.grid(row = 4, column = 1)

        btEnter = tkinter.Button(self._dialog_window, text = "ENTER",
                                 command = self.processButton)
        btEnter.grid(row = 5, column = 1, padx = 10, pady = 10)


        self._dialog_window.rowconfigure(0, weight = 0)
        self._dialog_window.rowconfigure(1, weight = 0)
        self._dialog_window.rowconfigure(2, weight = 0)
        self._dialog_window.rowconfigure(3, weight = 0)
        self._dialog_window.rowconfigure(4, weight = 0)
        self._dialog_window.rowconfigure(5, weight = 0)
        self._dialog_window.columnconfigure(0, weight = 0)
        self._dialog_window.columnconfigure(1, weight = 0)


    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def processButton(self):
        self.Rows = int(self._entryRows.get())
        self.Columns = int(self._entryColumns.get())
        self.first_move = self._entryFirstMove.get()
        self.winner = self._entryWinner.get()
        
        self._dialog_window.destroy()
                
    
    

class OthelloApplication:
    def __init__(self):
        self.new_board = project5_game_logic.blank(4, 4)
        self.board = project5_game_logic.Game_state(4, 4, 'B', self.new_board)
        
        self._rows = 0
        self._columns = 0
        
        self._root_window = tkinter.Tk()
        self._root_window.title("Othello")

        self._rule_label = tkinter.Label(
            master = self._root_window, text = 'FULL')
        self._rule_label.grid(row = 0, column = 0)

        self._white_button = tkinter.Button(
            master = self._root_window, text = 'Initialize White',
            command = self._on_white_clicked, state = tkinter.NORMAL)
        self._white_button.grid(row = 1, column = 0, sticky = tkinter.W)

        self._black_button = tkinter.Button(
            master = self._root_window, text = 'Initialize Black',
            command = self._on_black_clicked, state = tkinter.NORMAL)
        self._black_button.grid(row = 1, column = 0)

        self._start_button = tkinter.Button(
            master = self._root_window, text = 'Start Game',
            command = self._on_start_clicked)
        self._start_button.grid(row = 1, column = 0, sticky = tkinter.E)


        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 500,
            background = 'green')
        self._canvas.grid(
            row = 2, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._turn_text = tkinter.StringVar()
        self._turn_text.set('Turn: ')

        self._turn_label = tkinter.Label(
            master = self._root_window, textvariable = self._turn_text)
        self._turn_label.grid(row = 3, column = 0, sticky = tkinter.W)

        self._black_text = tkinter.StringVar()
        self._black_text.set('Black: ')

        self._black_label = tkinter.Label(
            master = self._root_window, textvariable = self._black_text)
        self._black_label.grid(row = 3, column = 0)

        self._white_text = tkinter.StringVar()
        self._white_text.set('White: ')

        self._white_label = tkinter.Label(
            master = self._root_window, textvariable = self._white_text)
        self._white_label.grid(row = 3, column = 0, sticky = tkinter.E)
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)

        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 0)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)

        self._show_dialog()

        self.new_board = project5_game_logic.blank(self._rows, self._columns)
        self.board = project5_game_logic.Game_state(self._rows, self._columns, self._first_move, self.new_board)
        self._turn_text.set(f'Turn: {self.board.get_turn()}')
        num = int(self.board.get_num_pieces('B'))
        self._black_text.set('Black: {}'.format(num))
        num2 = int(self.board.get_num_pieces('W'))
        self._white_text.set('White: {}'.format(num2))

    def run(self) -> None:
        self._root_window.mainloop()

    def _show_dialog(self) -> None:
        dialog = Dialog()
        dialog.show()
        self._rows = dialog.Rows
        self._columns = dialog.Columns
        self._first_move = dialog.first_move
        self._winner = dialog.winner
        self._canvas.delete(tkinter.ALL)
        self.draw_board()
            
    def draw_board(self):
        if self._rows != 0 and self._columns!=0:

            width = self._canvas.winfo_width()
            height = self._canvas.winfo_height()
            
            cell_width = width / self._columns
            cell_height = height / self._rows

            for r in range(self._rows):
                for c in range(self._columns):
                    x0 = c * cell_width
                    y0 = r * cell_height
                    x1 = x0 + cell_width
                    y1 = y0 + cell_height
                    self._canvas.create_rectangle(x0, y0, x1, y1, fill = '', outline = 'white')

    def _on_white_clicked(self):
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)


    def draw_white_piece(self, row:int, column:int, cell_width, cell_height):
        x0 = column*cell_width
        y0 = row * cell_height
        x1 = x0 + cell_width
        y1 = y0 + cell_height
        self.board.place(row, column, 'W')
        self._canvas.create_oval(x0, y0, x1, y1, fill = 'white', outline = 'white')
        num2 = int(self.board.get_num_pieces('W'))
        self._white_text.set('White: {}'.format(num2))

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        cell_width = self.get_cell_width()
        cell_height = self.get_cell_height()
    
        column = int(event.x/cell_width)
        row = int(event.y/cell_height)

        self.draw_white_piece(row, column, cell_width, cell_height)


    def _on_black_clicked(self):
        self._canvas.bind('<Button-1>', self._on_canvas_clickedb)


    def draw_black_piece(self, row:int, column:int, cell_width, cell_height):
        x0 = column*cell_width
        y0 = row * cell_height
        x1 = x0 + cell_width
        y1 = y0 + cell_height
        
        self.board.place(row, column, 'B')
        self._canvas.create_oval(x0, y0, x1, y1, fill = 'black', outline = 'black')
        
        num = int(self.board.get_num_pieces('B'))
        self._black_text.set('Black: {}'.format(num))

    def _on_canvas_clickedb(self, event: tkinter.Event) -> None:
        cell_width = self.get_cell_width()
        cell_height = self.get_cell_height()
        
        column = int(event.x/cell_width)
        row = int(event.y/cell_height)

        self.draw_black_piece(row, column, cell_width, cell_height)

    def get_cell_width(self):
        width = self._canvas.winfo_width()
        cell_width = width / self._columns
        return cell_width

    def get_cell_height(self):
        height = self._canvas.winfo_height()
        cell_height = height / self._rows
        return cell_height

    def _on_start_clicked(self):
        self._white_button['state'] = tkinter.DISABLED
        self._black_button['state'] = tkinter.DISABLED
        num = int(self.board.get_num_pieces('B'))
        num2 = int(self.board.get_num_pieces('W'))

        if self.board.is_game_over() == False:
            if self.board.can_make_move() == False:
                self.board.turn = self.board.opposite_turn()
                self._turn_text.set(f'Turn: {self.board.get_turn()}')
                
                if self.board.can_make_move() == False:
                    game = Game_over(self._winner, num, num2)
                    game.show()
                self._canvas.bind('<Button-1>', self._play_game)

            else:
                self._canvas.bind('<Button-1>', self._play_game)
            

           
        else:
            game = Game_over(self._winner, num, num2)
            game.show()
            self._turn_text.set(f'Turn: {self.board.get_turn()}')
            self._black_text.set('Black: {}'.format(num))
            self._white_text.set('White: {}'.format(num2))

    def _play_game(self, event: tkinter.Event):
        cell_width = self.get_cell_width()
        cell_height = self.get_cell_height()
        
        column = int(event.x/cell_width)
        row = int(event.y/cell_height)

        num = int(self.board.get_num_pieces('B'))
        num2 = int(self.board.get_num_pieces('W'))

        if self.board.is_game_over() == False:
            if self.board.can_make_move() == False:
                self.board.turn = self.board.opposite_turn()
                self._turn_text.set(f'Turn: {self.board.get_turn()}')
                
                if self.board.can_make_move() == False:
                    game = Game_over(self._winner, num, num2)
                    game.show()

            
            validity = self.board.check_move(row, column)
            if (validity) == True:
                self.board.make_move(row, column)

                for row in range(self._rows):
                    for col in range(self._columns):
                        if self.board.get_color(row, col) == 'white':
                            self.draw_white_piece(row, col, cell_width, cell_height)
                        if self.board.get_color(row, col) == 'black':
                            self.draw_black_piece(row, col, cell_width, cell_height)

                num = int(self.board.get_num_pieces('B'))
                num2 = int(self.board.get_num_pieces('W'))
                self._black_text.set('Black: {}'.format(num))
                self._white_text.set('White: {}'.format(num2))

                if self.board.is_game_over() == True:
                    game = Game_over(self._winner, num, num2)
                    game.show()
                    
            else:
                pass
        else:
            game = Game_over(self._winner, num, num2)
            game.show()

        self._turn_text.set(f'Turn: {self.board.get_turn()}')
        self._black_text.set('Black: {}'.format(num))
        self._white_text.set('White: {}'.format(num2))
        
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._canvas.delete(tkinter.ALL)
        self.draw_board()
        if self._rows != 0 and self._columns!=0:
            cell_width = self.get_cell_width()
            cell_height = self.get_cell_height()

            for row in range(self._rows):
                for col in range(self._columns):
                    if self.board.get_color(row, col) == 'white':
                        self.draw_white_piece(row, col, cell_width, cell_height)
                    if self.board.get_color(row, col) == 'black':
                        self.draw_black_piece(row, col, cell_width, cell_height)


if __name__ == '__main__':
    OthelloApplication().run()
