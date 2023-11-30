package util;

import data.Individual;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static util.Parser.parseCsv;

class ParserTest {
    @Test
    public void testParseRecords() {
        List<Individual> individuals = parseCsv("resources/iris.csv");
        for (Individual i : individuals) {
            assertEquals(i.getAttributes().size(), 5);
        }

    }

}