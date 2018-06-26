#Hibah Wasim
#project5_game_logic.py

def blank(rows, cols):
    board = []
    for r in range(rows):
        board.append([])
        for c in range(cols):
            board[r].append(Piece('.', r, c))
    return board

class Piece():
    def __init__(self, color: str, row, col):
        self.color = color
        self.row = row
        self.col = col

    def cord(self):
        return (self.row, self.col)
        
    def changeColor(self):
        if self.color == "B":
            self.color = "W"
        elif self.color == "W":
            self.color = "B"
        return self.color
    

class Game_state:
    def __init__(self, rows, columns, turn, board):
        self._rows = rows
        self._columns = columns
        self.turn = turn
        self._board = board

    def place(self, row, col, color):
        self._board[row][col].color = color

    def get_color(self, row, col):
        if self._board[row][col].color == 'W':
            return 'white'
        elif self._board[row][col].color == 'B':
            return 'black'

    def get_rows(self):
        return self._rows

    def get_columns(self):
        return self._columns

    def get_turn(self) -> str:
        if self.turn == 'B':
            return 'Black'
        else:
            return 'White'
        
    def opposite_turn(self) -> str:
        if self.turn == 'B':
            return 'W'
        else:
            return 'B'

    def opposite_color(self, color) -> str:
        if color == 'B':
            return 'W'
        return 'B'

    def is_game_over(self) -> bool:
        count = 0
        for element in range(self._rows):
            for index in range(self._columns):
                if self._board[element][index].color != '.':
                    count += 1
            
        if count == (self._rows * self._columns):
            return True
        else:
            return False

    def can_make_move(self) -> bool:
        count = 0
        for element in range(self._rows):
            for index in range(self._columns):

                if self._board[element][index].color == '.':
                    x, y = self._board[element][index].cord()
                    directions_8 = self.get_directions(x, y)
                   
                    for i in directions_8:
                        valid = self.check_valid(i)
                        if valid == True:
                            count += 1
                           
        if count >= 1:
            return True
        else:
            return False

    def make_move(self, x: int, y: int) -> None:
        self._board[x][y].color = self.turn
        self.turn = self.opposite_turn()

    def withinGrid(self, x, y) -> bool:
        if ((x < self._rows and x >= 0) and (y < self._columns and y >= 0)):
            return True
        else:
            return False

    def get_left_dir(self, x: int, y: int) -> [Piece]:
        left_dir = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x+ step * 0, y + step  * -1):
                    piece = self._board[x + step * 0][y + step  * -1]
                    left_dir.append(piece)

            except IndexError:
                pass
        return left_dir

    def get_right_dir(self, x: int, y: int) -> [Piece]:
        right_dir = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x + step * 0, y + step):
                    piece = self._board[x + step * 0][y + step]
                    right_dir.append(piece)
            except IndexError:
                pass
        return right_dir

    def get_up_dir(self, x: int, y: int) -> [Piece]:
        up_dir = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x + step * -1, y + step  * 0):
                    piece = self._board[x + step * -1][y + step  * 0]
                    up_dir.append(piece)
            except IndexError:
                pass   
        return up_dir

    def get_down_dir(self, x: int, y: int) -> [Piece]:
        down_dir = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x + step, y + step  * 0):
                    piece = self._board[x + step][y + step  * 0]
                    down_dir.append(piece)

            except IndexError:
                pass
        return down_dir
    
    def get_upper_right(self, x: int, y: int) -> [Piece]:
        upper_right = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x + step * -1, y + step):
                    piece = self._board[x + step * -1][y + step]
                    upper_right.append(piece)
            
            except IndexError:
                pass   
        return upper_right

    def get_upper_left(self, x: int, y: int) -> [Piece]:
        upper_left = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x + step * -1, y + step  * -1):
                    piece = self._board[x + step * -1][y + step  * -1]
                    upper_left.append(piece)
            
            except IndexError:
                pass
        return upper_left

    def get_lower_right(self, x: int, y: int) -> [Piece]:
        lower_right = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x + step, y + step):
                    piece = self._board[x + step][y + step]
                    lower_right.append(piece)
            
            except IndexError:
                pass
        return lower_right

    def get_lower_left(self, x: int, y: int) -> [Piece]:
        lower_left = []
        for step in range(1, self._rows):
            try:
                if self.withinGrid(x + step, y + step  * -1):
                    piece = self._board[x + step][y + step  * -1]
                    lower_left.append(piece)
            
            except IndexError:
                pass
        return lower_left

    def check_valid(self, list_directions) -> bool:
        if(len(list_directions) == 0):
            return False
        try:
            if list_directions[0].color != self.opposite_color(self.turn):
                return False
            else:
                for element in list_directions[1:]:
                    if element.color == self.turn:
                        return True
                    elif element.color == '.':
                        return False
                return False
            
        except IndexError:
            return False

    def _flip(self, list_directions) -> None:
        for element in list_directions:
            x, y = element.cord()
            if ((self._board[x][y].color != '.') and (self._board[x][y].color != self.turn)): 
                self._board[x][y].changeColor()
            elif (self._board[x][y].color == self.turn):
                break
        
    def get_directions(self, x: int, y: int) -> list:
        directions_8 = []
        left = self.get_left_dir(x, y)
        right = self.get_right_dir(x,y)
        up = self.get_up_dir(x,y)
        down = self.get_down_dir(x,y)
        upper_right = self.get_upper_right(x, y)
        upper_left = self.get_upper_left(x,y)
        lower_right = self.get_lower_right(x,y)
        lower_left = self.get_lower_left(x,y)

        directions_8.append(left)
        directions_8.append(right)
        directions_8.append(up)
        directions_8.append(down)
        directions_8.append(upper_right)
        directions_8.append(upper_left)
        directions_8.append(lower_right)
        directions_8.append(lower_left)

        return directions_8

    def check_move(self, x: int, y: int) -> bool:
        directions_8 = self.get_directions(x, y)
        count = 0

        if self.withinGrid(x, y) == False:
            return False
        
        if self._board[x][y].color != '.':
            return False
        
        for element in directions_8:
            valid = self.check_valid(element)
            if valid == True:
                count += 1
                self._flip(element)

        if count >= 1:
            return True
        else:
            return False
        
    def print_board(self) -> None:
        count = 1
        for element in range(len(self._board)):
            for index in range(len(self._board[element])):
                if index != (self._columns - 1):
                    print(self._board[element][index].color + ' ' , end = '')
                else:
                    print(self._board[element][index].color)
                    
    def get_num_pieces(self, color: str) -> int:
        count = 0
        for element in range(len(self._board)):
            for index in range(len(self._board[element])):
                if self._board[element][index].color == color:
                    count += 1      
        return count

    def winner(self, sign) -> None:
        B = self.get_num_pieces('B')
        W = self.get_num_pieces('W')

        if sign == '<':
            if B < W:
                print("WINNER: B")
                return  'B'
            elif W < B:
                print("WINNER: W")
                return 'W'
            elif B == W:
                print("WINNER: NONE")
                return 'NONE'
        elif sign == '>':
            if B > W:
                print("WINNER: B")
                return 'B'
            elif W > B:
                print("WINNER: W")
                return 'W'
            elif B == W:
                print("WINNER: NONE")
                return 'NONE'
                
            
def build_board(string_board) -> [list]:
    board = []
    for i in range(len(string_board)):
        board.append([])
    for x in range(len(string_board)):
        for y in range(len(string_board[x])):
            if string_board[x][y] == '.':
                board[x].append(Piece('.', x, y))
            elif string_board[x][y] == 'B':
                board[x].append(Piece('B', x, y))
            elif string_board[x][y] == 'W':
                board[x].append(Piece('W', x, y))

    return board
