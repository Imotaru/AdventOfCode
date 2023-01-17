import java.util.ArrayList;
import java.util.Collections;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day07 {
    public static long Part1() {
        return Solve(true);
    }

    public static long Part2() {
        return Solve(false);
    }

    static long Solve(boolean isPartOne) {
        ArrayList<Integer> crabs = new ArrayList<>();
        String line = Helper.ReadFile(7).get(0);
        Pattern numPattern = Pattern.compile("\\d+");
        Matcher m = numPattern.matcher(line);
        while (m.find()) {
            crabs.add(Integer.parseInt(m.group()));
        }
        Collections.sort(crabs);
        int median;
        if (crabs.size() % 2 == 0) {
            median = (crabs.get((crabs.size() / 2) - 1) + crabs.get(crabs.size() / 2)) / 2;
        } else {
            median = crabs.get(crabs.size() / 2);
        }
        int sum = 0;
        for (int crab : crabs) {
            sum += crab;
        }
        int average = sum / crabs.size();
        int minFuelCost = Integer.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            int fuelCost = 0;
            for (int crab : crabs) {
                if (isPartOne) {
                    fuelCost += Math.abs(crab - (median + 1 - i));
                } else {
                    int diff = Math.abs(crab - (average + 1 - i));
                    fuelCost += diff * (diff + 1) / 2;
                }
            }
            if (fuelCost < minFuelCost) {
                minFuelCost = fuelCost;
            }
        }
        return minFuelCost;
    }
}