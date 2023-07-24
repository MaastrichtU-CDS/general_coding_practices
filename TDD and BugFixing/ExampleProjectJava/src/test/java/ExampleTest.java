import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;


public class ExampleTest {

    //This is an exampleclass showing the basics of unittests in java
    //Use assertions to check if the results were correct
    //If the assertion fails, the entire unit-test fails
    @Test
    public void testExample() {
        //use assertTrue to determine if a statement is true
        assertTrue(true);
        //Use assertEquals to determine if two objects are equal
        assertEquals(1, 1);
        //Use assertEquals with a delta to determine if two values are equal for a given level of precision
        assertEquals(1, 0.99, 0.1);
    }

}
