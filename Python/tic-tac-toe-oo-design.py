class TicTacToe:
    def __init__(self):
        self.board = [['-']*3 for _ in range(3)]
        self.currentPlayer = 'x';
        self.gameEnd = False

    """
    @return: nothing
    """
    def getCurrentPlayer(self):
        return self.currentPlayer
        
    def move(self, r, c):
        if self.gameEnd:
            raise RuntimeError('Game has been ended, cannot make any more moves')
            
        if self.board[r][c] != '-':
            raise RuntimeError('This place has been taken')
            
        self.board[r][c] = self.currentPlayer
        
        if self.board[r] == [self.currentPlayer] * 3 or \
            self.board[0][c] == self.board[1][c] == self.board[2][c] == self.currentPlayer or \
            self.board[0][0] == self.board[1][1] == self.board[2][2] == self.currentPlayer or \
            self.board[0][2] == self.board[1][1] == self.board[2][0] == self.currentPlayer:
            self.gameEnd = True
            return True 
            
        self.currentPlayer = 'x' if self.currentPlayer == 'o' else 'o'
        return False
