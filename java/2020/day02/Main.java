import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

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

            char targetLetter = parts[1].charAt(0);

            String password = parts[2];

            int targetLetterCount = 0;
            for (char c : password.toCharArray()) {
                if (c == targetLetter) {
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
        int validPasswords = 0;

        for (String line : lines) {
            String[] parts = line.split(" ");

            String[] positions = parts[0].split("-");
            int pos1 = Integer.parseInt(positions[0]);
            int pos2 = Integer.parseInt(positions[1]);

            char targetLetter = parts[1].charAt(0);

            String password = parts[2];

            boolean pos1Matches = password.charAt(pos1 - 1) == targetLetter;
            boolean pos2Matches = password.charAt(pos2 - 1) == targetLetter;

            if (pos1Matches ^ pos2Matches) {
                validPasswords++;
            }
        }

        System.out.println("Part Two: " + validPasswords);
    }
}
