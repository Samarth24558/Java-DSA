import java.util.Scanner;

class Evenodd
{
    int num;

    public Evenodd(int number)
    {
        this.num=number;
        int rem=num%2;

       

        if(rem==0)
        {
            System.out.println("Given number is even");
        }
        else
        {
            System.out.println("Given number is odd");
        }

    }

    public Evenodd(Evenodd another)
    {
        num=another.num;


        int rem=num%2;

        System.out.println("Copy Constructur is called");

        if(rem==0)
        {
            System.out.println("Given number is even");
        }
        else
        {
            System.out.println("Given number is odd");
        }

    }

}

public class copy_con {

    public static void main(String[] args) 
    {
        int num;
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the number: ");
        num=input.nextInt();


        Evenodd obj1=new Evenodd(num);

        Evenodd obj2=new Evenodd(obj1);
        
    }
}