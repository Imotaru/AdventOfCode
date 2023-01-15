import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Day02 {
    static String FORWARD = "forward";
    static String DOWN = "down";
    static String UP = "up";
    public static int Part1() {
        return Solve(true);
    }

    public static int Part2() {
        return Solve(false);
    }

    static int Solve(boolean isPartOne) {
        ArrayList<String> lines = Helper.ReadFile(2);
        Pattern pattern = Pattern.compile("\\d+");

        int horizontal = 0;
        int depth = 0;
        int aim = 0;

        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            Matcher m = pattern.matcher(line);
            if (m.find()) {
                int value = Integer.parseInt(m.group());
                if (isPartOne) {
                    if (line.startsWith(FORWARD)) {
                        horizontal += value;
                    } else if (line.startsWith(DOWN)) {
                        depth += value;
                    } else if (line.startsWith(UP)) {
                        depth -= value;
                    }
                } else {
                    if (line.startsWith(FORWARD)) {
                        horizontal += value;
                        depth += aim * value;
                    } else if (line.startsWith(DOWN)) {
                        aim += value;
                    } else if (line.startsWith(UP)) {
                        aim -= value;
                    }
                }
            }
        }
        return horizontal * depth;
    }
}
