import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Helper {
        public static ArrayList<String> ReadFile(int day) {
            return ReadFile(day, false);
        }
        public static ArrayList<String> ReadFile(int day, boolean isTestInput) {
        ArrayList<String> lines = new ArrayList<>();

        String dayNumber = day < 10 ? "0" + day : "" + day;
        File myObj = new File("Input/Day" + dayNumber + (isTestInput ? "Test" : "") + "Input.txt");
        Scanner myReader;
        try {
            myReader = new Scanner(myObj);
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            throw new RuntimeException(e);
        }
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            lines.add(data);
        }
        myReader.close();
        return lines;
    }
}
