import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day13 {
    public static long Part1() {
        return Solve(true);
    }

    public static long Part2() {
        return Solve(false);
    }

    static long Solve(boolean isPartOne) {
        int maxX = 0;
        int maxY = 0;
        ArrayList<String> lines = Helper.ReadFile(13, false);
        for (String line : lines) {
            if (line.length() == 0) {
                break;
            }
            String[] splitStr = line.split(",");
            int x = Integer.parseInt(splitStr[0]);
            int y = Integer.parseInt(splitStr[1]);
            if (x > maxX) {
                maxX = x;
            }
            if (y > maxY) {
                maxY = y;
            }
        }
        boolean[][] dotGrid = new boolean[maxY + 1][maxX + 1];
        boolean startFoldingInstructions = false;
        Pattern numPattern = Pattern.compile("\\d+");
        ArrayList<Fold> folds = new ArrayList<>();

        for (String line : lines) {
            if (line.length() == 0) {
                startFoldingInstructions = true;
                continue;
            }
            if (startFoldingInstructions) {
                Matcher m = numPattern.matcher(line);
                int foldPos = 0;
                if (m.find()) {
                    foldPos = Integer.parseInt(m.group());
                }
                Fold fold = new Fold(line.contains("x") ? Axis.X : Axis.Y, foldPos);
                folds.add(fold);
            } else {
                String[] splitStr = line.split(",");
                int x = Integer.parseInt(splitStr[0]);
                int y = Integer.parseInt(splitStr[1]);
                dotGrid[y][x] = true;
            }
        }

        // Start folding
        for (Fold fold : folds) {
            FoldPaper(fold, dotGrid);
            if (isPartOne) {
                return GetDotCount(dotGrid);
            }
        }
        PrintDotSection(dotGrid);

        return -1;
    }

    static void PrintDotSection(boolean[][] dotGrid) {
        int minimumDotX = Integer.MAX_VALUE;
        int minimumDotY = Integer.MAX_VALUE;
        int maximumDotX = 0;
        int maximumDotY = 0;
        for (int y = 0; y < dotGrid.length; y++) {
            for (int x = 0; x < dotGrid[0].length; x++) {
                if (dotGrid[y][x]) {
                    if (y > maximumDotY) {
                        maximumDotY = y;
                    }
                    if (y < minimumDotY) {
                        minimumDotY = y;
                    }
                    if (x > maximumDotX) {
                        maximumDotX = x;
                    }
                    if (x < minimumDotX) {
                        minimumDotX = x;
                    }
                }
            }
        }
        for (int y = minimumDotY; y < maximumDotY + 1; y++) {
            for (int x = minimumDotX; x < maximumDotX + 1; x++) {
                if (dotGrid[y][x]) {
                    System.out.print("█");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.print("\n");
        }
    }

    static void FoldPaper(Fold fold, boolean[][] dotGrid) {
        if (fold.axis == Axis.X) {
            for (int y = 0; y < dotGrid.length; y++) {
                for (int x = fold.foldPos; x < dotGrid[0].length; x++) {
                    if (dotGrid[y][x]) {
                        dotGrid[y][fold.foldPos - (x - fold.foldPos)] = true;
                        dotGrid[y][x] = false;
                    }
                }
            }
        } else {
            for (int y = fold.foldPos; y < dotGrid.length; y++) {
                for (int x = 0; x < dotGrid[0].length; x++) {
                    if (dotGrid[y][x]) {
                        dotGrid[fold.foldPos - (y - fold.foldPos)][x] = true;
                        dotGrid[y][x] = false;
                    }
                }
            }
        }
    }

    static int GetDotCount(boolean[][] dotGrid) {
        int dotCount = 0;
        for (int y = 0; y < dotGrid.length; y++) {
            for (int x = 0; x < dotGrid[0].length; x++) {
                if (dotGrid[y][x]) {
                    dotCount++;
                }
            }
        }
        return dotCount;
    }
}

enum Axis {
    X,
    Y
}
class Fold {
    public Axis axis;
    public int foldPos;

    public Fold(Axis axis, int foldPos) {
        this.axis = axis;
        this.foldPos = foldPos;
    }
}