using System;
using System.IO;

namespace AdventOfCode2023 {
    public static class Helper {
        public static string[] ReadInput(int day, bool isTest = false) {
            string projectRoot = Path.GetFullPath(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "..\\..\\..\\"));
            string filePathRelativeToProject = Path.Combine(projectRoot, day < 10 ? $"Day0{day}Input.txt" : $"Day{day}Input.txt");
            return File.ReadAllLines(filePathRelativeToProject);
        }
    }
}
