using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace AdventOfCode2023 {
    public static class Day06 {

       
        public static long Solve1() {
            return Solve(true);
        }
        
        public static long Solve2() {
            return -1;
        }
        

        static long Solve(bool isPartOne) {
            var input = Helper.ReadInput(6, true);
            var values = new List<List<int>>();
            
            foreach (var line in input) {
                values.Add(ExtractNumbers(line));
            }

            var times = values[0];
            var distances = values[1];
            for (int i = 0; i < times.Count; i++) {
                Console.WriteLine($"{times[i]} - {distances[i]}");
            }
            
            return -1;
        }
        
        static List<int> ExtractNumbers(string input)
        {
            List<int> numbers = new List<int>();
            Regex regex = new Regex(@"\d+");

            MatchCollection matches = regex.Matches(input);
            foreach (Match match in matches)
            {
                numbers.Add(int.Parse(match.Value));
            }

            return numbers;
        }
    }
}
