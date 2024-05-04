import java.util.Scanner;
public class generate_num 
{
    public static void main(String[] args) {
        int num,i=0;

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the number: ");
        num=input.nextInt();

        if(num%2==0)
        {
            while (i<=num) 
            {
                System.out.println(i);
                i=i+2;
            }
        }
        else
        {
            i=1;
            while (i<=num) 
            {
                System.out.println(i);
                i=i+2;
                
            }
        }
    }
}
