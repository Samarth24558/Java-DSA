import java.util.Scanner;

public class do_while
{
    public static void main(String[] args) 
    {
        //java programme to perform do while

        int i,n;

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the limit: ");
        n=input.nextInt();

        i=1;

        do {
            System.out.println(i*i);
            i++;
        } while (i<=n);
        input.close();
    }
    
}
