import java.util.ArrayList;

public class Day01 {

    public static int Part1() {
        return Solve(true);
    }

    public static int Part2() {
        return Solve(false);
    }

    static int Solve(boolean isPartOne) {
        ArrayList<String> lines = Helper.ReadFile(1);
        int lastDepth = Integer.MAX_VALUE;
        int increaseCount = 0;
        int groupSize = isPartOne ? 1 : 3;

        for (int i = 0; i < lines.size() - (groupSize - 1); i++) {
            int depth = 0;
            for (int j = 0; j < groupSize; j++) {
                depth += Integer.parseInt(lines.get(i + j));
            }
            if (depth > lastDepth) {
                increaseCount++;
            }
            lastDepth = depth;
        }
        return increaseCount;
    }
}
