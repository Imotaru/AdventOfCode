using System;

namespace AdventOfCode2023 {
    enum DiceColor {
        Red = 0,
        Green = 1,
        Blue = 2,
    }
    public static class Day02 {
        static readonly int[] MAX_DICE_COLORS = new[] { 12, 13, 14 };
        public static int Solve1() {
            return Solve(true);
        }
        
        public static int Solve2() {
            return Solve(false);
        }

        static int Solve(bool isPartOne) {
            int sum = 0;
            var input = Helper.ReadInput(2);
            for (int i = 0; i < input.Length; i++) {
                var game = input[i].Substring(input[i].IndexOf(':') + 2);
                var rounds = game.Split("; ");
                bool isGameValidPart1 = true;
                int[] part2MaxDiceOccurances = new[] { 0, 0, 0 };
                foreach (var round in rounds) {
                    int[] diceColors = new[] { 0, 0, 0 };
                    var colors = round.Split(", ");
                    foreach (var color in colors) {
                        DiceColor dc;
                        if (color.Contains("red")) {
                            dc = DiceColor.Red;
                        } else if (color.Contains("green")) {
                            dc = DiceColor.Green;
                        } else if (color.Contains("blue")) {
                            dc = DiceColor.Blue;
                        } else {
                            throw new ArgumentException("Invalid color");
                        }
                        diceColors[(int)dc] = int.Parse(color.Split(" ")[0]);
                    }
                    if (isPartOne) {
                        if (diceColors[0] > MAX_DICE_COLORS[0] || diceColors[1] > MAX_DICE_COLORS[1] || diceColors[2] > MAX_DICE_COLORS[2]) {
                            isGameValidPart1 = false;
                            break;
                        }
                    } else {
                        for (int j = 0; j < 3; j++) {
                            if (diceColors[j] > part2MaxDiceOccurances[j]) {
                                part2MaxDiceOccurances[j] = diceColors[j];
                            }
                        }
                    }
                }
                if (isPartOne) {
                    if (isGameValidPart1) sum += i + 1;
                } else {
                    sum += part2MaxDiceOccurances[0] * part2MaxDiceOccurances[1] * part2MaxDiceOccurances[2];
                }
            }
            return sum;
        }
    }
}
