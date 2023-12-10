using System;
using System.Collections.Generic;

namespace AdventOfCode2023 {
    public static class Day05 {
        private const int CONVERSION_MAP_AMOUNT = 7;

        private static readonly Dictionary<int, string> fieldNameDict = new Dictionary<int, string>() {
            {0, "soil"},
            {1, "fertilizer"},
            {2, "water"},
            {3, "light"},
            {4, "temperature"},
            {5, "humidity"},
            {6, "location"},
        };

        public static long Solve1() {
            return Solve(true);
        }
        
        public static long Solve2() {
            return -1;
        }

        static long Solve(bool isPartOne) {
            var input = Helper.ReadInput(5, true);
            var rawSeeds = input[0].Substring(input[0].IndexOf(' ') + 1).Split(' ');
            List<long> seeds = new List<long>();
            foreach (var rawSeed in rawSeeds) {
                seeds.Add(long.Parse(rawSeed));
            }

            // build conversion maps
            var conversionMaps = new List<long[]>[CONVERSION_MAP_AMOUNT];
            for (int i = 0; i < CONVERSION_MAP_AMOUNT; i++) {
                conversionMaps[i] = new List<long[]>();
            }

            int currentConversionMap = -1;
            
            foreach (var line in input) {
                if (line.Length == 0) {
                    currentConversionMap++;
                    continue;
                }

                if (currentConversionMap == -1 || line.Contains(':')) {
                    continue;
                }

                var strNumbers = line.Split(' ');
                var numbers = new long[3];
                for (int i = 0; i < 3; i++) {
                    numbers[i] = long.Parse(strNumbers[i]);
                }
                conversionMaps[currentConversionMap].Add(numbers);
            }

            // calculate all the values for the seed
            var seedResults = new Dictionary<long, long[]>();
            for (int i = 0; i < seeds.Count; i++) {
                if (isPartOne) {
                    var results = new long[CONVERSION_MAP_AMOUNT];
                    for (int j = 0; j < CONVERSION_MAP_AMOUNT; j++) {
                        var source = j == 0 ? seeds[i] : results[j - 1];
                        results[j] = Convert(seeds[i], source, conversionMaps[j], j);
                    }
                    seedResults.Add(seeds[i], results);
                } else {
                    if (i % 2 == 1) {
                        List<long> interestingSeeds = new List<long>();
                        long low = seeds[i - 1];
                        long high = seeds[i - 1] + seeds[i] - 1;
                        interestingSeeds.Add(low);
                        interestingSeeds.Add(high);
                        // todo add more interesting seeds inbetween
                        foreach (var interestingSeed in interestingSeeds) {
                            var results = new long[CONVERSION_MAP_AMOUNT];
                            for (int j = 0; j < CONVERSION_MAP_AMOUNT; j++) {
                                var source = j == 0 ? interestingSeed : results[j - 1];
                                results[j] = Convert(interestingSeed, source, conversionMaps[j], j);
                            }
                            seedResults.Add(interestingSeed, results);
                        }
                    }
                }
            }
            
            long lowestLocation = long.MaxValue;
            
            foreach (var results in seedResults) {
                var myLine = $"{results.Key}: ";
                foreach (var numbers in results.Value) {
                    myLine += numbers.ToString() + ", ";
                }
                Console.WriteLine(myLine);
                var location = results.Value[^1];
                if (location < lowestLocation) {
                    lowestLocation = location;
                }
            }
            
            Console.WriteLine($"Lowest location: {lowestLocation}");

            // for (int i = 0; i < CONVERSION_MAP_AMOUNT; i++) {
            //     Console.WriteLine($"DEBUG {fieldNameDict[i]}");
            //     
            //     List<long> numbers = new List<long>();
            //     for (int j = 0; j < 100; j++) {
            //         var result = Convert(j, j, conversionMaps[i], i);
            //         numbers.Add(result);
            //         Console.WriteLine($"{j} {result}");
            //     }
            //     Console.WriteLine("");
            // }

            
            
            // var seedToSoil = new List<long[]>();
            // var soilToFertilizer = new List<long[]>();
            // var fertilizerToWater = new List<long[]>();
            // var waterToLight = new List<long[]>();
            // var lightToTemperature = new List<long[]>();
            // var temperatureToHumidity = new List<long[]>();
            // var humidityToLocation = new List<long[]>();
            

            return lowestLocation;
        }

        static long Convert(long seed, long source, List<long[]> conversionMap, int fieldIndex) {
            foreach (var row in conversionMap) {
                if (row[1] <= source && row[1] + row[2] >= source) {
                    // this row affects the conversion
                    long diff = row[0] - row[1];
                    // Console.WriteLine($"{seed} - {fieldNameDict[fieldIndex]}: line {row[0]}, {row[1]}, {row[2]} is affecting the conversion, diff is {diff} and final result is {source + diff}");
                    return source + diff;
                }
            }

            // Console.WriteLine($"{seed} - {fieldNameDict[fieldIndex]}: no line affected the conversion, source was {source}");
            return source;
        }
    }
}
