import java.util.Scanner;

public class principal_diagonal_matrix 
{
    public static void main(String[] args) 
    {
        int[][] arr=new int[10][10];

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the length of array below 10: ");
        int len=input.nextInt();

        for (int i=0;i<len;i++)
        {
            for(int j=0;j<len;j++)
            { 
                System.out.print("Enter the value("+i+":"+j+"): ");
                int value=input.nextInt();
                arr[i][j]=value;
            }

        }
        int k=len-1;
        int sum=0;
        for (int i=0;i<len;i++)
        {
            for(int j=0;j<len;j++)
            { 
                if (j==k)
                {    System.out.print(arr[i][j]);
                     sum=sum+arr[i][j];
                }

                else
                    System.out.print(" ");
            }
            System.out.println();
            k=k-1;

        }
        System.out.println("Sum is: "+sum);
        
    }

     
}