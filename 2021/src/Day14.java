import java.util.*;

public class Day14 {
    public static long Part1() {
        return Solve(true);
    }

    public static long Part2() {
        return Solve(false);
    }

    static int maxDepth;
    static Map<CharTuple, Character> insertionRules;
    static long[] charCount;

    static long Solve(boolean isPartOne) {
        long start = System.currentTimeMillis();

        ArrayList<String> lines = Helper.ReadFile(14, false);
        String original = lines.get(0);
        insertionRules = new HashMap<>();

        for (int i = 2; i < lines.size(); i++) {
            String[] splitStr = lines.get(i).split(" -> ");
            insertionRules.put(new CharTuple(splitStr[0].charAt(0), splitStr[0].charAt(1)), splitStr[1].charAt(0));
        }

        maxDepth = isPartOne ? 10 : 23;
        charCount = new long[(int)'Z' + 1];
        for (int i = 0; i < original.length(); i++) {
            charCount[original.charAt(i)]++;
        }

        for (int i = 0; i < original.length() - 1; i++) {
            System.out.println("Progress: " + (i) + " / " + (original.length() - 1));
            RecursivePolimerize(original.charAt(i), original.charAt(i + 1), 0);
        }

        long maxCount = 0;
        long minCount = Long.MAX_VALUE;
        for (long j : charCount) {
            if (j > maxCount) {
                maxCount = j;
            }
            if (j != 0 && j < minCount) {
                minCount = j;
            }
        }
        long finish = System.currentTimeMillis();
        long timeElapsed = finish - start;
        System.out.println("Took " + ((double) timeElapsed / 1000) + "s");
        return maxCount - minCount;
    }

    static void RecursivePolimerize(char a, char b, int depth) {
        if (depth == maxDepth) {
            return;
        }
        CharTuple sub = new CharTuple(a, b);
        if (insertionRules.containsKey(sub)) {
            char c = insertionRules.get(sub);
            charCount[c]++;
            int depthPlus = depth + 1;
            RecursivePolimerize(a, c, depthPlus);
            RecursivePolimerize(c, b, depthPlus);
        }
    }
}

class CharTuple {
    public char a;
    public char b;

    public CharTuple(char a, char b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public boolean equals(Object o) {
//        if (this == o)
//            return true;
//        if (o == null || getClass() != o.getClass())
//            return false;
        CharTuple other = (CharTuple) o;
        return a == other.a && b == other.b;
    }

    @Override
    public int hashCode() {
        return (int)a * 256 + (int)b;
    }
}