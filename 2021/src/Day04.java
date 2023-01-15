import java.util.ArrayList;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day04 {
    public static int Part1() {
        return Solve(true);
    }

    public static int Part2() {
        return Solve(false);
    }

    static int Solve(boolean isPartOne) {
        ArrayList<String> lines = Helper.ReadFile(4);
        ArrayList<BingoBoard> bingoBoards = new ArrayList<>();
        Pattern numPattern = Pattern.compile("\\d+");

        bingoBoards.add(new BingoBoard());
        int currentBoardIndex = 0;
        for (int i = 2; i < lines.size(); i++) {
            if (lines.get(i).equals("")) {
                bingoBoards.add(new BingoBoard());
                currentBoardIndex++;
                continue;
            }
            int counter = 0;
            Matcher m = numPattern.matcher(lines.get(i));
            while (m.find()) {
                bingoBoards.get(currentBoardIndex).numbers[(i - 2) % 5][counter] = Integer.parseInt(m.group());
                counter++;
            }
        }

        HashSet<Integer> winners = new HashSet<>();
        String drawLine = lines.get(0);
        Matcher matcher = numPattern.matcher(drawLine);
        while (matcher.find()) {
            int draw = Integer.parseInt(matcher.group());
            for (int i = 0; i < bingoBoards.size(); i++) {
                if (bingoBoards.get(i).DrawAndCheckWin(draw)) {
                    if (isPartOne) {
                        return bingoBoards.get(i).GetScore() * draw;
                    } else {
                        winners.add(i);
                        if (winners.size() == bingoBoards.size()) {
                            return bingoBoards.get(i).GetScore() * draw;
                        }
                    }
                }
            }
        }
        return -1;
    }
}

class BingoBoard {
    int[][] numbers;
    BingoBoard() {
        numbers = new int[5][5];
    }

    public boolean DrawAndCheckWin(int draw) {
        for (int x = 0; x < numbers.length; x++) {
            for (int y = 0; y < numbers[0].length; y++) {
                if (numbers[x][y] == draw) {
                    numbers[x][y] = -1;
                    return HasWon();
                }
            }
        }
        return false;
    }
    boolean HasWon() {
        for (int x = 0; x < numbers.length; x++) {
            boolean columnWin = true;
            for (int y = 0; y < numbers[0].length; y++) {
                if (numbers[x][y] != -1) {
                    columnWin = false;
                    break;
                }
            }
            if (columnWin) {
                return true;
            }
        }
        for (int y = 0; y < numbers.length; y++) {
            boolean rowWin = true;
            for (int x = 0; x < numbers[0].length; x++) {
                if (numbers[x][y] != -1) {
                    rowWin = false;
                    break;
                }
            }
            if (rowWin) {
                return true;
            }
        }
        return false;
    }

    public int GetScore() {
        int score = 0;
        for (int x = 0; x < numbers.length; x++) {
            for (int y = 0; y < numbers[0].length; y++) {
                if (numbers[x][y] != -1) {
                    score += numbers[x][y];
                }
            }
        }
        return score;
    }
}