class TicTacToe {
    private int[][] board;
    private boolean turnX;
    private boolean finished;

    // Initialize your data structure here.
    public TicTacToe() {
        board = new int[3][3];
        turnX = true;
        finished = false;
    }
    
    public boolean move(int row, int col) throws AlreadyTakenException, GameEndException {
        int turn = turnX ? 1 : 2;
        if(finished){
            throw new GameEndException();
        }
        if(board[row][col] != 0){
            throw new AlreadyTakenException();
        }
        if(turnX){
            board[row][col] = 1;
        }else{
            board[row][col] = 2;
        }
        finished = checkWin(turn);
        turnX = !turnX;
        return finished;
    }
    private boolean checkWin(int turn){
        for(int i = 0; i < 3; i++){
            if(turn == board[i][0] && board[i][0] == board[i][1] && board[i][1] == board[i][2]){
                return true;
            }
        }
        for(int j = 0; j < 3; j++){
            if(turn == board[0][j] && board[0][j] == board[1][j] && board[1][j] == board[2][j]){
                return true;
            }
        }
        if(turn == board[0][0] && board[0][0] == board[1][1] && board[1][1] == board[2][2]){
            return true;
        }
        if(turn == board[0][2] && board[0][2] == board[1][1] && board[1][1] == board[2][0]){
            return true;
        }
        return false;
    }
}
class AlreadyTakenException extends Exception{
        
}
class GameEndException extends Exception{
    
}

/*
// From TA, the checkWin funciton is ugly.

public class TicTacToe {
    private char[][] board;
    private char currentPlayerMark;
    private boolean gameEnd;

    public TicTacToe() {
        board = new char[3][3];
        initialize();
    }

    public char getCurrentPlayer() {
        return currentPlayerMark;
    }

    public void initialize() {
        gameEnd = false;
        currentPlayerMark = 'x';

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '-';
            }
        }
    }

    public boolean isBoardFull() {
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

    public void changePlayer() {
        if (currentPlayerMark == 'x')
            currentPlayerMark = 'o';
        else
            currentPlayerMark = 'x';

    }

    // true means this move wins the game, false means otherwise
    public boolean move(int row, int col) throws AlreadyTakenException, GameEndException {

        if (gameEnd) {
            throw new GameEndException();
        }

        if (board[row][col] != '-') {
            throw new AlreadyTakenException();
        }

        board[row][col] = currentPlayerMark;

        boolean win;

        //check row
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[row][i] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }

        //check column
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }

        //check back diagonal
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[i][i] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }

        //check forward diagonal
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[i][board.length - i - 1] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }
        changePlayer();
        return win;
    }
}


class GameEndException extends Exception{
    public GameEndException() {
        super("Game has been ended, cannot make any more moves");
    }
}

class AlreadyTakenException extends Exception {
    public AlreadyTakenException() {
        super("This place has been taken");
    }
}
*/

/*
class TicTacToe {
    int[][] board;
    boolean isTurn;
    boolean isWin;
    // Initialize your data structure here.
    public TicTacToe() {
        board = new int[3][3];
        isTurn = true;
        isWin = false;
    }
    
    public boolean move(int row, int col) throws AlreadyTakenException, GameEndException {
        if (isWin)
            throw new GameEndException();
        if (board[row][col] > 0)
            throw new AlreadyTakenException();
        if (isTurn)
            board[row][col] = 1;
        else
            board[row][col] = 2;
        isTurn = !isTurn;
        isWin = checkWin();
        return isWin;
    }
    
    private boolean checkWin() {
        if (board[0][0] != 0 && board[0][0] == board[0][1] && board[0][1] == board[0][2]) return true;
        if (board[1][0] != 0 && board[1][0] == board[1][1] && board[1][1] == board[1][2]) return true;
        if (board[2][0] != 0 && board[2][0] == board[2][1] && board[2][1] == board[2][2]) return true;

        if (board[0][0] != 0 && board[0][0] == board[1][0] && board[1][0] == board[2][0]) return true;
        if (board[0][1] != 0 && board[0][1] == board[1][1] && board[1][1] == board[2][1]) return true;
        if (board[0][2] != 0 && board[0][2] == board[1][2] && board[1][2] == board[2][2]) return true;

        if (board[0][0] != 0 && board[0][0] == board[1][1] && board[1][1] == board[2][2]) return true;
        if (board[2][0] != 0 && board[2][0] == board[1][1] && board[1][1] == board[0][2]) return true;
        
        return false;
    }
    
}

class AlreadyTakenException extends Exception {
    public AlreadyTakenException() {}
}

class GameEndException extends Exception {
    public GameEndException() {}
}
*/


/*
public class TicTacToe {
    private char[][] board;
    private char currentPlayerMark;
    private boolean gameEnd;

    public TicTacToe() {
        board = new char[3][3];
        initialize();
    }

    public char getCurrentPlayer() {
        return currentPlayerMark;
    }

    public void initialize() {
        gameEnd = false;
        currentPlayerMark = 'x';

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '-';
            }
        }
    }

    public boolean isBoardFull() {
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

    public void changePlayer() {
        if (currentPlayerMark == 'x')
            currentPlayerMark = 'o';
        else
            currentPlayerMark = 'x';

    }

    // true means this move wins the game, false means otherwise
    public boolean move(int row, int col) throws AlreadyTakenException, GameEndException {

        if (gameEnd) {
            throw new GameEndException();
        }

        if (board[row][col] != '-') {
            throw new AlreadyTakenException();
        }

        board[row][col] = currentPlayerMark;

        boolean win;

        //check row
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[row][i] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }

        //check column
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }

        //check back diagonal
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[i][i] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }

        //check forward diagonal
        win = true;
        for (int i = 0; i < board.length; i++) {
            if (board[i][board.length - i - 1] != currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) {
            gameEnd = true;
            return win;
        }
        changePlayer();
        return win;
    }
}


class GameEndException extends Exception{
    public GameEndException()
    {
        super("Game has been ended, cannot make any more moves");
    }
}

class AlreadyTakenException extends Exception {
    public AlreadyTakenException()
    {
        super("This place has been taken");
    }
}
*/
