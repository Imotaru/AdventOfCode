import java.util.ArrayList;
import java.util.HashSet;

public class Day03 {
    public static int Part1() {
        ArrayList<String> lines = Helper.ReadFile(3);
        int totalLines = lines.size();
        int lineLength = lines.get(0).length();
        int[] oneCounts = new int[lineLength];
        for (String line : lines) {
            for (int j = 0; j < lineLength; j++) {
                if (line.charAt(j) == '1') {
                    oneCounts[j] += 1;
                }
            }
        }

        int midPoint = totalLines / 2;
        int gamma = 0;
        int epsilon = 0;
        for (int i = 0; i < oneCounts.length; i++) {
            if (oneCounts[i] > midPoint) {
                gamma += Math.pow(2, oneCounts.length - 1 - i);
            } else {
                epsilon += Math.pow(2, oneCounts.length - 1 - i);
            }
        }

        return gamma * epsilon;
    }

    public static int Part2() {
        ArrayList<String> lines = Helper.ReadFile(3);
        int totalLines = lines.size();
        HashSet<Integer> linesThatStartWithOne = new HashSet<>();

        for (int i = 0; i < totalLines; i++) {
            String line = lines.get(i);
            if (line.charAt(0) == '1') {
                linesThatStartWithOne.add(i);
            }
        }

        int amountOfLinesThatStartWithOne = linesThatStartWithOne.size();
        int oxygenGeneratorRating = CalculateOxygenOrCO2Value(lines, true, amountOfLinesThatStartWithOne);
        int co2ScrubberRating = CalculateOxygenOrCO2Value(lines, false, amountOfLinesThatStartWithOne);

        return oxygenGeneratorRating * co2ScrubberRating;
    }

    /**
     * @param lines the input
     * @param index index position at which to check if it's 1 or 0
     * @param indexesToExclude input index positions which won't be considered
     * @return -1 if '0' is more frequent, 0 if '0' and '1' have the same frequency, 1 if '1' is more frequent
     */
    static int CompareOneCountToZeroCount(ArrayList<String> lines, int index, HashSet<Integer> indexesToExclude) {
        int totalLineCount = lines.size();
        int oneCount = 0;
        int zeroCount = 0;
        for (int i = 0; i < totalLineCount; i++) {
            if (indexesToExclude.contains(i)) {
                continue;
            }
            String line = lines.get(i);
            if (line.charAt(index) == '1') {
                oneCount++;
            } else {
                zeroCount++;
            }
        }
        return Integer.compare(oneCount, zeroCount);
    }

    static void ExcludeLines(ArrayList<String> lines, int index, HashSet<Integer> indexesToExclude, char valueToExclude) {
        for (int i = 0; i < lines.size(); i++) {
            if (lines.get(i).charAt(index) == valueToExclude) {
                indexesToExclude.add(i);
            }
        }
    }

    static int CalculateOxygenOrCO2Value(ArrayList<String> lines, boolean isOxygen, int amountOfLinesThatStartWithOne) {
        HashSet<Integer> linesToExclude = new HashSet<>();
        int totalLines = lines.size();
        int lineLength = lines.get(0).length();
        if (amountOfLinesThatStartWithOne > totalLines / 2) {
            ExcludeLines(lines, 0, linesToExclude, isOxygen ? '0' : '1');
        } else {
            ExcludeLines(lines, 0, linesToExclude, isOxygen ? '1' : '0');
        }
        for (int i = 1; i < lineLength; i++) {
            if (linesToExclude.size() == totalLines - 1) {
                break;
            }
            int comparisonResult = CompareOneCountToZeroCount(lines, i, linesToExclude);
            if (comparisonResult >= 0) {
                ExcludeLines(lines, i, linesToExclude, isOxygen ? '0' : '1');
            } else {
                ExcludeLines(lines, i, linesToExclude, isOxygen ? '1' : '0');
            }
        }
        String valueLine = "";
//        System.out.println("Remaining Line count for " + (isOxygen ? "Oxygen" : "CO2") + " is: " + (totalLines - linesToExclude.size()));
        for (int i = 0; i < totalLines; i++) {
            if (linesToExclude.contains(i)) {
                continue;
            }
            valueLine = lines.get(i);
            break;
        }

        int value = 0;
        for (int i = 0; i < valueLine.length(); i++) {
            if (valueLine.charAt(i) == '1') {
                value += Math.pow(2, valueLine.length() - 1 - i);
            }
        }
//        System.out.println("Value for " + (isOxygen ? "Oxygen" : "CO2") + " is: " + value + ". Binary was " + valueLine);
        return value;
    }
}
