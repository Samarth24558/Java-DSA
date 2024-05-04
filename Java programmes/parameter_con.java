import java.util.Scanner;

class Natural_nums
{
    int num;

    public Natural_nums(int number)
    {
        this.num=number;
        

        for(int i=1;i<=num;i++)
        {
            System.out.println(i);
        }


    }

}
public class parameter_con 
{

    public static void main(String[] args) 
    {
        int number;

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the number:");
        number=input.nextInt();

        Natural_nums obj=new Natural_nums(number);

        




       
    }
}
