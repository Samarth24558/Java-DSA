import java.util.Scanner;
public class num_type 
{
    public static void main(String[] args) 
    {
        int num;
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the number: ");
        num=input.nextInt();
        if(num==0)
        {
            System.out.println("Given number is zero");
        }
        else
        if(num>0)
        {
            System.out.println("Given number positive");
        }
        else
        {
            System.out.println("Given number is nagetive");
        }
    }
}
