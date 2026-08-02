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
        int validPassportCount = 0;

        for (int i = 0; i < lines.size(); i++) {
            List<String> currentPassport = new ArrayList<>();

            while (i < lines.size() && !lines.get(i).isBlank()) {
                currentPassport.add(lines.get(i));

                i++;
            }

            Set<String> requiredFields = new HashSet<>(
                Set.of("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
            );

            Set<String> fieldSet = new HashSet<>();
            for (String line : currentPassport) {
                String[] split = line.split(" ");

                for (String keyValue : split) {
                    fieldSet.add(keyValue.split(":")[0]);
                }
            }

            if (fieldSet.containsAll(requiredFields)) {
                validPassportCount++;
            }
        }

        System.out.println("Part One: " + validPassportCount);
    }

    private static void partTwo(List<String> lines) {
        // TODO
    }
}
