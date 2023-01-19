import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class Day10 {
    public static long Part1() {
        return Solve(true);
    }


    public static long Part2() {
        return Solve(false);
    }

    static long Solve(boolean isPartOne) {
        ArrayList<String> lines = Helper.ReadFile(10, false);
        ArrayList<Long> completionScores = new ArrayList<>();

        int errorScore = 0;
        for (String line : lines) {
            Stack<Integer> bracketStack = new Stack<>();
            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                int bracketType = GetBracketType(c);
                if (IsOpenBracket(c)) {
                    bracketStack.add(bracketType);
                } else {
                    int popped = bracketStack.pop();
                    if (bracketType != popped) {
                        errorScore += GetErrorScore(bracketType);
                        break;
                    }
                }
                if (!isPartOne) {
                    if (i == line.length() - 1 && bracketStack.size() > 0) {
                        long completionScore = 0;
                        while (bracketStack.size() > 0) {
                            int nextBracket = bracketStack.pop();
                            completionScore *= 5;
                            completionScore += GetBracketCompletionScore(nextBracket);
                        }
                        completionScores.add(completionScore);
                    }
                }
            }
        }
        if (isPartOne) {
            return errorScore;
        } else {
            Collections.sort(completionScores);
            return completionScores.get(completionScores.size() / 2);
        }
    }

    static boolean IsOpenBracket(char c) {
        return c == '(' || c == '[' || c == '{' || c == '<';
    }

    static int GetBracketType(char c) {
        switch (c) {
            case '(':
            case ')':
                return 0;
            case '[':
            case ']':
                return 1;
            case '{':
            case '}':
                return 2;
            case '<':
            case '>':
                return 3;
            default:
                return -1;
        }
    }

    static int GetBracketCompletionScore(int bracketType) {
        return bracketType + 1;
    }

    static int GetErrorScore(int bracketType) {
        switch (bracketType) {
            case 0:
                return 3;
            case 1:
                return 57;
            case 2:
                return 1197;
            case 3:
                return 25137;
            default:
                return 0;
        }
    }
}