import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day06 {
    public static long Part1() {
        return Solve(true);
    }

    public static long Part2() {
        return Solve(false);
    }

    static long Solve(boolean isPartOne) {
        int MAX_AGE = 8;
        long[] allFish = new long[MAX_AGE + 1];
        String line = Helper.ReadFile(6).get(0);
        Pattern numPattern = Pattern.compile("\\d+");
        Matcher m = numPattern.matcher(line);
        while (m.find()) {
            allFish[Integer.parseInt(m.group())] += 1;
        }

        int DAYS = isPartOne ? 80 : 256;

        for (int i = 0; i < DAYS; i++) {
            long birthingFishAmount = allFish[0];
            for (int j = 0; j < MAX_AGE; j++) {
                allFish[j] = allFish[j + 1];
            }
            allFish[MAX_AGE] = birthingFishAmount;
            allFish[6] += birthingFishAmount;
        }

        long fishCount = 0;
        for (long fish : allFish) {
            fishCount += fish;
        }
        return fishCount;
    }
}