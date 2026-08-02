import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Main {

    private static final Path INPUT_FILE = Path.of(
        "../../../inputs/2020/3.txt"
    );

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(INPUT_FILE);

        partOne(lines);
        partTwo(lines);
    }

    private static void partOne(List<String> lines) {
        int width = lines.get(0).length();
        int height = lines.size();

        int treesEncountered = 0;

        int r = 0;
        int c = 0;
        while (r < height) {
            if (lines.get(r).charAt(c) == '#') {
                treesEncountered++;
            }

            r++;
            c = (c + 3) % width;
        }

        System.out.println("Part One: " + treesEncountered);
    }

    private static void partTwo(List<String> lines) {
        // TODO
    }
}
