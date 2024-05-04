import java.util.Scanner;

public class string_manipulation 
{
    public static void main(String[] args) 
    {
        // java program to perform various string manipulations

        Scanner input=new Scanner(System.in);
        System.out.print("Enter any word:");
        String value=input.nextLine();
        StringBuilder sb=new StringBuilder(value);
        System.out.println("Length of string is: "+sb.length());
        System.out.println("Append: "+sb.append(" Hello world"));
        System.out.println("Insert: "+sb.insert(0,"S"));
        System.out.println("Delete: "+sb.delete(1, 3));

        
    }
}