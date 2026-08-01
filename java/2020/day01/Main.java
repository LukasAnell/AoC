import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Main {

    private static final Path INPUT_FILE = Path.of(
        "../../../inputs/2020/1.txt"
    );

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(INPUT_FILE);

        partOne(lines);
        partTwo(lines);
    }

    private static void partOne(List<String> lines) {
        for (String line1 : lines) {
            if (Integer.parseInt(line1) >= 2020) {
                continue;
            }

            for (String line2 : lines) {
                int num1 = Integer.parseInt(line1);
                int num2 = Integer.parseInt(line2);

                if (num1 + num2 == 2020) {
                    System.out.println("Part One: " + num1 * num2);

                    return;
                }
            }
        }
    }

    private static void partTwo(List<String> lines) {
        for (String line1 : lines) {
            if (Integer.parseInt(line1) >= 2020) {
                continue;
            }

            for (String line2 : lines) {
                if (Integer.parseInt(line1) + Integer.parseInt(line2) >= 2020) {
                    continue;
                }

                for (String line3 : lines) {
                    int num1 = Integer.parseInt(line1);
                    int num2 = Integer.parseInt(line2);
                    int num3 = Integer.parseInt(line3);

                    if (num1 + num2 + num3 == 2020) {
                        System.out.println("Part Two: " + num1 * num2 * num3);

                        return;
                    }
                }
            }
        }
    }
}
