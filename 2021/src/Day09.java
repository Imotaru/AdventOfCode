import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day09 {
    public static long Part1() {
        ArrayList<String> lines = Helper.ReadFile(9, false);
        int width = lines.get(0).length();
        int height = lines.size();
        int[][] grid = new int[height][width];

        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                grid[y][x] = Integer.parseInt("" + lines.get(y).charAt(x));
            }
        }

        int riskLevelSum = 0;
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                int currentPoint = grid[y][x];
                if (x > 0 && currentPoint >= grid[y][x - 1]) {
                    continue;
                }
                if (y > 0 && currentPoint >= grid[y - 1][x]) {
                    continue;
                }
                if (x < width - 1 && currentPoint >= grid[y][x + 1]) {
                    continue;
                }
                if (y < height - 1 && currentPoint >= grid[y + 1][x]) {
                    continue;
                }
                riskLevelSum += currentPoint + 1;
            }
        }

        return riskLevelSum;
    }

    public static long Part2() {
        return -1;
    }
}