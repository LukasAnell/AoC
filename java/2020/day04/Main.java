import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Main {

    private static final Path INPUT_FILE = Path.of(
        "../../../inputs/2020/4.txt"
    );

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(INPUT_FILE);

        partOne(lines);
        partTwo(lines);
    }

    private static void partOne(List<String> lines) {
        // TODO
    }

    private static void partTwo(List<String> lines) {
        // TODO
    }
}
