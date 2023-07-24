package util;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;
import data.Attribute;
import data.Individual;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static data.Attribute.checkType;

public class Parser {
    public static List<Individual> parseCsv(String path) {
        List<List<String>> data = readCsv(path);
        List<String> attributeNames = data.get(0);
        List<Individual> individuals = new ArrayList<>();
        for (int i = 1; i < data.size(); i++) {
            Individual in = new Individual();
            for (int j = 0; j < data.get(i).size(); j++) {
                String value = data.get(i).get(j);
                in.addAttribute(new Attribute(attributeNames.get(j), value, checkType(value)));
            }
            individuals.add(in);
        }
        return individuals;
    }

    private static List<List<String>> readCsv(String path) {
        List<List<String>> records = new ArrayList<List<String>>();
        try (CSVReader csvReader = new CSVReader(new FileReader(path))) {
            String[] values = null;
            while ((values = csvReader.readNext()) != null) {
                records.add(Arrays.asList(values));
            }
        } catch (IOException | CsvValidationException e) {
            e.printStackTrace();
        }
        return records;
    }
}
