import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

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

            Map<String, String> fields = new HashMap<>();
            for (String line : currentPassport) {
                String[] split = line.split(" ");

                for (String keyValue : split) {
                    String[] keyValueSplit = keyValue.split(":");

                    fields.put(keyValueSplit[0], keyValueSplit[1]);
                }
            }

            System.out.println(fields);

            if (!fields.keySet().containsAll(requiredFields)) {
                continue;
            }

            int byrField = Integer.parseInt(fields.get("byr"));
            boolean byrCondition = byrField >= 1920 && byrField <= 2002;

            int iyrField = Integer.parseInt(fields.get("iyr"));
            boolean iyrCondition = iyrField >= 2010 && iyrField <= 2020;

            int eyrField = Integer.parseInt(fields.get("eyr"));
            boolean eyrCondition = eyrField >= 2020 && eyrField <= 2030;

            String hgtField = fields.get("hgt");
            if (!hgtField.endsWith("cm") && !hgtField.endsWith("in")) {
                continue;
            }
            int hgtNum = Integer.parseInt(
                hgtField.substring(0, hgtField.length() - 2)
            );
            String hgtUnit = hgtField.substring(hgtField.length() - 2);
            boolean hgtCondition = hgtUnit.equals("cm")
                ? hgtNum >= 150 && hgtNum <= 193
                : hgtNum >= 59 && hgtNum <= 76;

            String hclField = fields.get("hcl");
            boolean hclCondition =
                hclField.charAt(0) == '#' &&
                hclField.substring(1).matches("^[a-f0-9]+$");

            String eclField = fields.get("ecl");
            Set<String> eclSet = new HashSet<>(
                Set.of("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            );
            boolean eclCondition = eclSet.contains(eclField);

            String pidField = fields.get("pid");
            boolean pidCondition =
                pidField.length() == 9 && pidField.matches("^[0-9]+$");

            System.out.println(
                "byr: " +
                    byrCondition +
                    ", iyr: " +
                    iyrCondition +
                    ", eyr: " +
                    eyrCondition +
                    ", hgt: " +
                    hgtCondition +
                    ", hcl: " +
                    hclCondition +
                    ", ecl: " +
                    eclCondition +
                    ", pid: " +
                    pidCondition
            );

            if (
                byrCondition &&
                iyrCondition &&
                eyrCondition &&
                hgtCondition &&
                hclCondition &&
                eclCondition &&
                pidCondition
            ) {
                validPassportCount++;
            }
        }

        System.out.println("Part Two: " + validPassportCount);
    }
}
