import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day05 {
    static int MAX_VALUE = 1000;
    public static int Part1() {
        return Solve(true);
    }

    public static int Part2() {
        return Solve(false);
    }

    static int Solve(boolean isPartOne) {
        ArrayList<String> lines = Helper.ReadFile(5);
        ArrayList<int[]> coordList = new ArrayList<>();

        Pattern numPattern = Pattern.compile("\\d+");

        for (int i = 0; i < lines.size(); i++) {
            Matcher m = numPattern.matcher(lines.get(i));
            coordList.add(new int[4]);
            for (int j = 0; j < 4; j++) {
                if (m.find()) {
                    coordList.get(i)[j] = Integer.parseInt(m.group());
                }
            }
        }

        int[][] grid = new int[MAX_VALUE][MAX_VALUE];

        for (int[] coords : coordList) {
            if (coords[0] == coords[2]) {
                int min_y = Math.min(coords[1], coords[3]);
                for (int i = 0; i <= Math.abs(coords[1] - coords[3]); i++) {
                    grid[coords[0]][min_y + i] += 1;
                }
            } else if (coords[1] == coords[3]) {
                int min_x = Math.min(coords[0], coords[2]);
                for (int i = 0; i <= Math.abs(coords[0] - coords[2]); i++) {
                    grid[min_x + i][coords[1]] += 1;
                }
            } else if (!isPartOne) {
                boolean x_first_larger = coords[0] > coords[2];
                boolean y_first_larger = coords[1] > coords[3];
                for (int i = 0; i <= Math.abs(coords[0] - coords[2]); i++) {
                    grid[coords[0] + (x_first_larger ? -i : i)][coords[1] + (y_first_larger ? -i : i)] += 1;
                }
            }
        }

        int count = 0;
        for (int[] gridLine : grid) {
            for (int cell : gridLine) {
                if (cell > 1) {
                    count++;
                }
            }
        }
        return count;
    }
}