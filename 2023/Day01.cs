using System;
using System.IO;

namespace AdventOfCode2023 {
    public static class Day01 {
        public static int Solve1() {
            int sum = 0;
            char[] digits = new[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
            var input = Helper.ReadInput(1);
            foreach (string line in input) {
                int firstIndex = line.IndexOfAny(digits);
                int lastIndex = line.LastIndexOfAny(digits);
                sum += int.Parse((line[firstIndex].ToString())) * 10 + int.Parse((line[lastIndex].ToString()));
            }
            return sum;
        }
        
        public static int Solve2() {
            int sum = 0;
            char[] digits = new[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
            string[] strDigits = new[] { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
            var input = Helper.ReadInput(1);
            foreach (string line in input) {
                int firstIndex = line.IndexOfAny(digits);
                int firstDigit = firstIndex != -1 ? int.Parse(line[firstIndex].ToString()) : -1;
                int lastIndex = line.LastIndexOfAny(digits);
                int lastDigit = firstIndex != -1 ? int.Parse(line[lastIndex].ToString()) : -1;
                for (int i = 0; i < strDigits.Length; i++) {
                    int index = line.IndexOf(strDigits[i]);
                    if (firstIndex == -1 || (index < firstIndex && index != -1)) {
                        firstIndex = index;
                        firstDigit = i + 1;
                    }
                    int index2 = line.LastIndexOf(strDigits[i]);
                    if (index2 > lastIndex) {
                        lastIndex = index2;
                        lastDigit = i + 1;
                    }
                }
                sum += firstDigit * 10 + lastDigit;
            }
            return sum;
        }
    }
}
