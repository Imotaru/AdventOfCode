import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day08 {
    public static long Part1() {
        ArrayList<String> lines = Helper.ReadFile(8, false);
        int count1478 = 0;
        Pattern[] output1478Patterns = new Pattern[4];
        output1478Patterns[0] = BuildOutputPattern(2); // one
        output1478Patterns[1] = BuildOutputPattern(4); // four
        output1478Patterns[2] = BuildOutputPattern(3); // seven
        output1478Patterns[3] = BuildOutputPattern(7); // eight
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            String output = line.substring(line.indexOf('|')).replace(" ", "  ");
            for (Pattern outputPattern : output1478Patterns) {
                Matcher m = outputPattern.matcher(output);
                while (m.find()) {
                    count1478++;
                }
            }
        }

        return count1478;
    }

    public static long Part2() {
        int sum = 0;
        ArrayList<String> lines = Helper.ReadFile(8, false);
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            String[] inputOutput = line.split("\\|");
            String[] outputs = inputOutput[1].split(" ");
            String[] decoded = DecodeInput(inputOutput[0].split(" "));

            StringBuilder finalNumber = new StringBuilder();
            for (String output : outputs) {
                if (output.length() < 2) {
                    continue;
                }
                for (int j = 0; j < 10; j++) {
                    if (output.length() == decoded[j].length() && ContainsAllChars(output, decoded[j])) {
                        finalNumber.append(j);
                        break;
                    }
                }
            }

            sum += Integer.parseInt(finalNumber.toString());
        }

        return sum;
    }

    static Pattern BuildOutputPattern(int segmentAmount) {
        StringBuilder sb = new StringBuilder();
        sb.append("\\W");
        for (int i = 0; i < segmentAmount; i++) {
            sb.append("\\w");
        }
        sb.append("((\\W)|$)");
        return Pattern.compile(sb.toString());
    }

    static boolean ContainsChar(String str, char c) {
        return str.indexOf(c) >= 0;
    }

    static boolean ContainsAllChars(String str, String str2) {
        for (int i = 0; i < str2.length(); i++) {
            if (!ContainsChar(str, str2.charAt(i))) {
                return false;
            }
        }
        return true;
    }

    static String[] DecodeInput(String[] inputDigits) {
        String[] decoded = new String[10];
        int decodedAmount = 0;
        while (decodedAmount < 10) {
            for (String input : inputDigits) {
                int len = input.length();
                if (len == 2) {
                    if (decoded[1] != null) {
                        continue;
                    }
                    decoded[1] = input;
                    decodedAmount++;
                } else if (len == 3) {
                    if (decoded[7] != null) {
                        continue;
                    }
                    decoded[7] = input;
                    decodedAmount++;
                } else if (len == 4) {
                    if (decoded[4] != null) {
                        continue;
                    }
                    decoded[4] = input;
                    decodedAmount++;
                } else if (len == 7) {
                    if (decoded[8] != null) {
                        continue;
                    }
                    decoded[8] = input;
                    decodedAmount++;
                } else if (len == 5) {
                    // 2, 3, 5
                    if (decoded[3] == null && decoded[1] != null) {
                        if (ContainsAllChars(input, decoded[1])) {
                            decoded[3] = input;
                            decodedAmount++;
                        }
                    } else if (decoded[5] == null && decoded[6] != null) {
                        if (ContainsAllChars(decoded[6], input)) {
                            decoded[5] = input;
                            decodedAmount++;
                        }
                    } else if (decoded[2] == null && decoded[3] != null && decoded[5] != null && !input.equals(decoded[3]) && !input.equals(decoded[5])) {
                        decoded[2] = input;
                        decodedAmount++;
                    }
                } else if (len == 6) {
                    // 0, 6, 9
                    if (decoded[6] == null && decoded[1] != null) {
                        if (!ContainsAllChars(input, decoded[1])) {
                            decoded[6] = input;
                            decodedAmount++;
                        }
                    } else if (decoded[9] == null && decoded[4] != null) {
                        if (ContainsAllChars(input, decoded[4])) {
                            decoded[9] = input;
                            decodedAmount++;
                        }
                    } else if (decoded[0] == null && decoded[6] != null && decoded[9] != null && !input.equals(decoded[6]) && !input.equals(decoded[9])) {
                        decoded[0] = input;
                        decodedAmount++;
                    }
                }
            }
        }
        return decoded;
    }
}