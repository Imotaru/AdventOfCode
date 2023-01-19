import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day09 {
    static int currentBasinSize = 0;
    public static long Part1() {
        return Solve(true);
    }


    public static long Part2() {
        return Solve(false);
    }

    static int Solve(boolean isPartOne) {
        ArrayList<String> lines = Helper.ReadFile(9);
        int width = lines.get(0).length();
        int height = lines.size();
        int[][] grid = new int[height][width];

        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                grid[y][x] = Integer.parseInt("" + lines.get(y).charAt(x));
            }
        }
        if (isPartOne) {
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
        } else {
            HashSet<Integer> seen = new HashSet<>();
            ArrayList<Integer> basinSizes = new ArrayList<>();
            for (int x = 0; x < width; x++) {
                for (int y = 0; y < height; y++) {
                    int currentPoint = grid[y][x];
                    if (currentPoint == 9) {
                        continue;
                    }
                    int currentPointHash = ToHash(x, y, width);
                    if (seen.contains(currentPointHash)) {
                        continue;
                    }
                    RecursiveCheckNeighbors(x, y, grid, seen, width, height);
                    basinSizes.add(currentBasinSize);
                    currentBasinSize = 0;
                }
            }
            Collections.sort(basinSizes);
            return basinSizes.get(basinSizes.size() - 1) * basinSizes.get(basinSizes.size() - 2) * basinSizes.get(basinSizes.size() - 3);
        }
    }

    static int ToHash(int x, int y, int width) {
        return y * width + x;
    }

    static void RecursiveCheckNeighbors(int x, int y, int[][] grid, HashSet<Integer> seen, int width, int height) {
        if (grid[y][x] == 9) {
            return;
        }
        currentBasinSize++;
        seen.add(ToHash(x, y, width));
        if (x > 0 && !seen.contains(ToHash(x - 1, y, width))) {
            RecursiveCheckNeighbors(x - 1, y, grid, seen, width, height);
        }
        if (y > 0 && !seen.contains(ToHash(x, y - 1, width))) {
            RecursiveCheckNeighbors(x, y - 1, grid, seen, width, height);
        }
        if (x < width - 1 && !seen.contains(ToHash(x + 1, y, width))) {
            RecursiveCheckNeighbors(x + 1, y, grid, seen, width, height);
        }
        if (y < height - 1 && !seen.contains(ToHash(x, y + 1, width))) {
            RecursiveCheckNeighbors(x, y + 1, grid, seen, width, height);
        }
    }
}