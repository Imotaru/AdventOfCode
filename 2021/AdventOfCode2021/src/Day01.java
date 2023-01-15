import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day01 {

    public static int Part1() {
        ArrayList<String> lines = Helper.ReadFile(1);
        int lastDepth = Integer.MAX_VALUE;
        int increaseCount = 0;
        for (String line : lines) {
            int depth = Integer.parseInt(line);
            if (depth > lastDepth) {
                increaseCount++;
            }
            lastDepth = depth;
        }
        return increaseCount;
    }

    public static int Part2() {
        ArrayList<String> lines = Helper.ReadFile(1);
        int lastDepth = Integer.MAX_VALUE;
        int increaseCount = 0;
        for (int i = 0; i < lines.size() - 2; i++) {
            int depth = 0;
            depth += Integer.parseInt(lines.get(i));
            depth += Integer.parseInt(lines.get(i + 1));
            depth += Integer.parseInt(lines.get(i + 2));
            if (depth > lastDepth) {
                increaseCount++;
            }
            lastDepth = depth;
        }
        return increaseCount;
    }
}
