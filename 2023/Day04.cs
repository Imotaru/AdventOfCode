using System;
using System.Collections.Generic;

namespace AdventOfCode2023 {
    public static class Day04 {
        public static int Solve1() {
            return Solve(true);
        }
        
        public static int Solve2() {
            return Solve(false);
        }

        static int Solve(bool isPartOne) {
            int sum = 0;
            var input = Helper.ReadInput(4, false);

            int[] cardAmounts = new int[input.Length];

            for (int i = 0; i < input.Length; i++) {
                cardAmounts[i] = 1;
            }

            for (int i = 0; i < input.Length; i++) {
                var line = input[i].Substring(input[i].IndexOf(':') + 2);
                List<int> winningNumbers = new List<int>();
                List<int> drawnNumbers = new List<int>();
                var splits = line.Split(' ');
                bool doneWithWinning = false;
                foreach (var split in splits) {
                    if (split.Length == 0) {
                        continue;
                    }

                    if (split == "|") {
                        doneWithWinning = true;
                        continue;
                    }

                    if (doneWithWinning) {
                        drawnNumbers.Add(int.Parse(split));
                    } else {
                        winningNumbers.Add(int.Parse(split));
                    }
                }

                int wins = 0;
                foreach (var drawnNumber in drawnNumbers) {
                    if (winningNumbers.Contains(drawnNumber)) {
                        wins++;
                    }
                }
                
                if (isPartOne) {
                    int score = 0;
                    if (wins > 0) {
                        score = 1;
                    }

                    for (int j = 0; j < wins - 1; j++) {
                        score *= 2;
                    }

                    sum += score;
                } else {
                    for (int j = i + 1; j < i + wins + 1; j++) {
                        cardAmounts[j] += cardAmounts[i];
                    }
                    sum += cardAmounts[i];
                }
            }
            
            return sum;
        }
    }
}
