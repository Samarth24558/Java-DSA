import java.io.*;

public class exceptions {

    // Checked exception - FileNotFoundException
    public static void checked() {
        try {
            File file = new File("nonexistentfile.txt");
            FileReader fr = new FileReader(file);
        } catch (FileNotFoundException e) {
            System.out.println("Checked Exception Caught: " + e.getMessage());
        }
    }

    // Unchecked exception - ArithmeticException
    public static void unchecked() {
        try {
            int result = 10 / 0; 
        } catch (ArithmeticException e) {
            System.out.println("Unchecked Exception Caught: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        checked();
        unchecked();
    }
}
