using System;
using System.Collections.Generic;

namespace AdventOfCode2023 {
    public static class Day03 {
        public static int Solve1() {
            int sum = 0;
            var input = Helper.ReadInput(3, false);
            
            for (int i = 0; i < input.Length; i++) {
                string number = "";
                int startX = -1;
                for (int j = 0; j < input[i].Length; j++) {
                    if (char.IsDigit(input[i][j])) {
                        number += input[i][j];
                        if (startX == -1) {
                            startX = j;
                        }
                    } else if (startX != -1) {
                        if (IsTouchingSpecialChar(input, i, startX, number.Length)) {
                            sum += int.Parse(number);
                        }
                        number = "";
                        startX = -1;
                    }
                }

                if (startX != -1) {
                    if (IsTouchingSpecialChar(input, i, startX, number.Length)) {
                        sum += int.Parse(number);
                    }
                }
            }
            
            return sum;
        }
        
        public static int Solve2() {
            int sum = 0;
            var input = Helper.ReadInput(3, false);
            
            for (int i = 0; i < input.Length; i++) {
                for (int j = 0; j < input[i].Length; j++) {
                    if (input[i][j] != '*') {
                        continue;
                    }
                    int numbersAmount = 0;
                    
                    // checking in line
                    if (j >= 1 && char.IsDigit(input[i][j - 1])) {
                        numbersAmount++;
                    }
                    if (j + 1 < input[i].Length && char.IsDigit(input[i][j + 1])) {
                        numbersAmount++;
                    }

                    // checking line above
                    if (i > 0) {
                        if (j >= 1 && char.IsDigit(input[i - 1][j - 1])) {
                            numbersAmount++;
                            if (j + 1 < input[i].Length && char.IsDigit(input[i - 1][j + 1]) && !char.IsDigit(input[i - 1][j])) {
                                numbersAmount++;
                            }
                        } else if (j + 1 < input[i].Length && char.IsDigit(input[i - 1][j + 1]) ||
                                   char.IsDigit(input[i - 1][j])) {
                            numbersAmount++;
                        }
                    }
                    
                    // checking line below
                    if (i - 1 < input.Length) {
                        if (j >= 1 && char.IsDigit(input[i + 1][j - 1])) {
                            numbersAmount++;
                            if (j + 1 < input[i].Length && char.IsDigit(input[i + 1][j + 1]) && !char.IsDigit(input[i + 1][j])) {
                                numbersAmount++;
                            }
                        } else if (j + 1 < input[i].Length && char.IsDigit(input[i + 1][j + 1]) ||
                                   char.IsDigit(input[i + 1][j])) {
                            numbersAmount++;
                        }
                    }

                    // continue if not touching exactly 2 numbers
                    if (numbersAmount != 2) {
                        continue;
                    }
                    
                    Console.Out.WriteLine($"{j + 1}, {i + 1} is touching 2 numbers");

                    List<int> numbers = new List<int>();
                    
                    // parse in same line
                    if (j >= 1 && char.IsDigit(input[i][j - 1])) {
                        numbers.Add(ParseNumberFromGrid(input, i, j - 1));
                    }
                    if (j + 1 < input[i].Length && char.IsDigit(input[i][j + 1])) {
                        numbers.Add(ParseNumberFromGrid(input, i, j + 1));
                    }
                    
                    // parse in line above
                    if (i > 0) {
                        if (j >= 1 && char.IsDigit(input[i - 1][j - 1])) {
                            numbers.Add(ParseNumberFromGrid(input, i - 1, j - 1));
                            if (j + 1 < input[i].Length && char.IsDigit(input[i - 1][j + 1]) && !char.IsDigit(input[i - 1][j])) {
                                numbers.Add(ParseNumberFromGrid(input, i - 1, j + 1));
                            }
                        } else if (j + 1 < input[i].Length && char.IsDigit(input[i - 1][j + 1])) {
                            numbers.Add(ParseNumberFromGrid(input, i - 1, j + 1));
                        } else if (char.IsDigit(input[i - 1][j])) {
                            numbers.Add(ParseNumberFromGrid(input, i - 1, j));
                        }
                    }
                    
                    // parse in line below
                    if (i - 1 < input.Length) {
                        if (j >= 1 && char.IsDigit(input[i + 1][j - 1])) {
                            numbers.Add(ParseNumberFromGrid(input, i + 1, j - 1));
                            if (j + 1 < input[i].Length && char.IsDigit(input[i + 1][j + 1]) && !char.IsDigit(input[i + 1][j])) {
                                numbers.Add(ParseNumberFromGrid(input, i + 1, j + 1));
                            }
                        } else if (j + 1 < input[i].Length && char.IsDigit(input[i + 1][j + 1])) {
                            numbers.Add(ParseNumberFromGrid(input, i + 1, j + 1));
                        } else if (char.IsDigit(input[i + 1][j])) {
                            numbers.Add(ParseNumberFromGrid(input, i + 1, j));
                        }
                    }

                    if (numbers.Count == 2) {
                        sum += numbers[0] * numbers[1];
                    } else {
                        throw new Exception(
                            $"Somehow parsed {numbers.Count} numbers when there should have been only 2 at {j + 1}, {i + 1}");
                    }
                }
            }
            
            return sum;
        }

        static bool IsTouchingSpecialChar(string[] input, int line, int startX, int length) {
            int endIndex = startX + length;
            for (int i = startX - 1; i < endIndex + 1; i++) {
                if (i < 0 || i > input[line].Length - 1) {
                    continue;
                }

                for (int j = line - 1; j < line + 2; j++) {
                    if (j < 0 || j > input.Length - 1) {
                        continue;
                    }

                    if (input[j][i] != '.' && !char.IsDigit(input[j][i])) {
                        return true;
                    }
                }
            }

            return false;
        }

        static int ParseNumberFromGrid(string[] input, int i, int j) {
            if (!char.IsDigit(input[i][j])) {
                throw new Exception($"input[{i}][{j}] is not a digit");
            }
            
            string number = "";
            int startIndex = j;
            
            for (int k = j; k >= 0; k--) {
                if (char.IsDigit(input[i][k])) {
                    startIndex = k;
                } else {
                    break;
                }
            }

            int index = startIndex;
            while (index < input[i].Length && char.IsDigit(input[i][index])) {
                number += input[i][index];
                index++;
            }

            return int.Parse(number);
        }
    }
}
