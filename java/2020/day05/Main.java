import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Main {

    private static final Path INPUT_FILE = Path.of(
        "../../../inputs/2020/5.txt"
    );

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(INPUT_FILE);

        partOne(lines);
        partTwo(lines);
    }

    private static void partOne(List<String> lines) {
        int maxSeatId = Integer.MIN_VALUE;

        for (String line : lines) {
            String rowInstructions = line.substring(0, 7);
            String colInstructions = line.substring(7);

            int[] rowRange = { 0, 127 };
            for (char instruction : rowInstructions.toCharArray()) {
                int mid = (rowRange[0] + rowRange[1]) / 2;
                if (instruction == 'F') {
                    rowRange[1] = mid;
                } else if (instruction == 'B') {
                    rowRange[0] = mid + 1;
                }
            }

            int[] colRange = { 0, 7 };
            for (char instruction : colInstructions.toCharArray()) {
                int mid = (colRange[0] + colRange[1]) / 2;
                if (instruction == 'L') {
                    colRange[1] = mid;
                } else if (instruction == 'R') {
                    colRange[0] = mid + 1;
                }
            }

            int currentSeatId = rowRange[0] * 8 + colRange[0];

            maxSeatId = Math.max(maxSeatId, currentSeatId);
        }

        System.out.println("Part One: " + maxSeatId);
    }

    private static void partTwo(List<String> lines) {
        // TODO
    }
}
