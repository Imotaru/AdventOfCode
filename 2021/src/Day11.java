import java.util.ArrayList;

public class Day11 {
    public static long Part1() {
        return Solve(true);
    }


    public static long Part2() {
        return Solve(false);
    }

    final static int[][] DIRECTIONS = {
        {-1, -1},
        {-1, 0},
        {-1, 1},
        {0, -1},
        {0, 1},
        {1, -1},
        {1, 0},
        {1, 1},
    };
    final static int GRID_SIZE = 10;
    static long Solve(boolean isPartOne) {
        int flashCounter = 0;
        ArrayList<int[]> flashedThisRound = new ArrayList<>();
        ArrayList<String> lines = Helper.ReadFile(11, false);
        int[][] octopusGrid = new int[GRID_SIZE][GRID_SIZE];
        for (int y = 0; y < GRID_SIZE; y++) {
            String line = lines.get(y);
            for (int x = 0; x < GRID_SIZE; x++) {
                octopusGrid[y][x] = Integer.parseInt("" + line.charAt(x));
            }
        }
        int counter = 0;
        while (true) {
            for (int y = 0; y < GRID_SIZE; y++) {
                for (int x = 0; x < GRID_SIZE; x++) {
                    octopusGrid[y][x] += 1;
                }
            }
            for (int y = 0; y < GRID_SIZE; y++) {
                for (int x = 0; x < GRID_SIZE; x++) {
                    if (octopusGrid[y][x] > 9) {
                        RecursiveFlash(octopusGrid, x, y, flashedThisRound);
                    }
                }
            }
            flashCounter += flashedThisRound.size();
            flashedThisRound.clear();
            counter++;
            if (isPartOne) {
                if (counter >= 100) {
                    return flashCounter;
                }
            } else {
                boolean allFlashed = true;
                for (int y = 0; y < GRID_SIZE; y++) {
                    for (int x = 0; x < GRID_SIZE; x++) {
                        if (octopusGrid[y][x] != 0) {
                            allFlashed = false;
                            break;
                        }
                    }
                    if (!allFlashed) {
                        break;
                    }
                }
                if (allFlashed) {
                    return counter;
                }
            }
        }
    }

    static void RecursiveFlash(int[][] octopusGrid, int x, int y, ArrayList<int[]> flashedThisRound) {
        for (int[] flashedOctopus : flashedThisRound) {
            if (x == flashedOctopus[0] && y == flashedOctopus[1]) {
                return;
            }
        }
        flashedThisRound.add(new int[] {x, y});
        octopusGrid[y][x] = 0;
        for (int[] dir : DIRECTIONS) {
            int newX = x + dir[0];
            if (newX < 0 || newX >= GRID_SIZE) {
                continue;
            }
            int newY = y + dir[1];
            if (newY < 0 || newY >= GRID_SIZE) {
                continue;
            }
            boolean isAlreadyFlashed = false;
            for (int[] flashedOctopus : flashedThisRound) {
                if (newX == flashedOctopus[0] && newY == flashedOctopus[1]) {
                    isAlreadyFlashed = true;
                    break;
                }
            }
            if (isAlreadyFlashed) {
                continue;
            }
            octopusGrid[newY][newX] += 1;
            if (octopusGrid[newY][newX] > 9) {
                RecursiveFlash(octopusGrid, newX, newY, flashedThisRound);
            }
        }
    }
}