import java.util.Scanner;
public class string_palindrome
{
    public static void main(String[] args) 
    {
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the String: ");
        String value=input.nextLine();
        String reverse="";
        int charl=value.length()-1;
        while (charl!=-1) 
        {
            reverse=reverse+((char)value.charAt(charl));
            charl--;
            
        }
        if (reverse.equals(value))
        {
            System.out.println("Given String palindrome");

        }
        else
        {
            System.out.println("Given string is not palindrome");
        }


    }
}