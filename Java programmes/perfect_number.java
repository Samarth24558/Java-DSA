 //java programme generate perfect number

 import java.util.Scanner;

 public class perfect_number 
 {
 
    public static void main(String[] args) 
    {
        int limit;

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the limit");
        limit=input.nextInt();

        int sum=0;

        for(int i=1;i<limit;i++)
        {
            for(int j=1;j<i;j++)
            {
                if(i%j==0)
                {
                    sum=sum+j;

                }

            }
            if(sum==i)
            {
                System.out.println(i);
                sum=0;
            }
            sum=0;
        }

        
        
    }
 }