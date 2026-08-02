import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main {

    private static final Path INPUT_FILE = Path.of(
        "../../../inputs/2020/2.txt"
    );

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(INPUT_FILE);

        partOne(lines);
        partTwo(lines);
    }

    private static void partOne(List<String> lines) {
        int validPasswords = 0;

        for (String line : lines) {
            String[] parts = line.split(" ");

            String[] range = parts[0].split("-");
            int lowerBound = Integer.parseInt(range[0]);
            int upperBound = Integer.parseInt(range[1]);

            String targetLetter = parts[1].substring(0, 1);

            String password = parts[2];

            int targetLetterCount = 0;
            for (char c : password.toCharArray()) {
                if (c == targetLetter.charAt(0)) {
                    targetLetterCount++;
                }
            }

            if (
                targetLetterCount >= lowerBound &&
                targetLetterCount <= upperBound
            ) {
                validPasswords++;
            }
        }

        System.out.println("Part One: " + validPasswords);
    }

    private static void partTwo(List<String> lines) {
        // TODO
    }
}
