/*
Design Tic-Tac-Toe game.

- board has fixed size of 3
- X always take the first move
- If a place already got taken, and one player want to take that place,
an AlreadyTakenException will be thrown
- If one player wins, and somebody try to make another move, a GameEndException will be thrown.

Example
Input:
move(0, 0) // X turn
move(1, 0) // O trun
move(1, 1) // X turn
move(2, 0) // O turn
move(2, 2) // X turn and win
move(0, 0) //throw GameEndException
move(0, 0) // X turn
move(0, 0) // throw AlreadyTakenException
move(1, 0) // O turn
move(1, 1) // X turn
move(2, 0) // o turn
move(2, 2) // X turn and win

You should print blew:

x player wins!
x player wins!
*/

class GameEndException {
public:
    char *what() {
        return "Game has been ended, cannot make any more moves";
    }
}gameEndException;

class AlreadyTakenException {
public:
    char* what() {
        return "This place has been taken";
    }
}alreadyTakenException;

class TicTacToe {
private:
    char board[3][3];
    char currentPlayerMark;
    bool gameEnd;

public:

    TicTacToe() {
        gameEnd = false;
        currentPlayerMark = 'x';

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '-';
            }
        }
    }

    char getCurrentPlayer() {
        return currentPlayerMark;
    }

    bool isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == '-') {
                    return false;
                }
            }
        }
        gameEnd = true;
        return true;
    }

    void changePlayer() {
        if (currentPlayerMark == 'x') {
            currentPlayerMark = 'o';
        } else {
            currentPlayerMark = 'x';
        }
    }

    bool move(int row, int col) {
        if (gameEnd) {
            throw gameEndException;
        }
        if (board[row][col] != '-') {
            throw alreadyTakenException;
        }
        board[row][col] = currentPlayerMark;

        win = checkWin(row, col);
        if (win)
            gameEnd = true;
        else
            changePlayer();
        return win;
    }

    bool checkWin(int row, int col) {
        if (board[row][0] == currentPlayerMark && board[row][0] == board[row][1] && board[row][0] == board[row][2]) {
            return true;
        }
        if (board[0][col] == currentPlayerMark && board[0][col] == board[1][col] && board[0][col] == board[2][col]) {
            return true;
        }
        if(currentPlayerMark == board[0][0] && board[0][0] == board[1][1] && board[1][1] == board[2][2]){
            return true;
        }
        if(currentPlayerMark == board[0][2] && board[0][2] == board[1][1] && board[1][1] == board[2][0]){
            return true;
        }
        return false;
    }
};
