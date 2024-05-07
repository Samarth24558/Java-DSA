import java.util.Scanner;
public class saparete_even_odd_in_2d_array 
{
    public static void main(String[] args) 
    {
        int[][] arr=new int[10][10];
        int[][] even=new int[10][10];
        int[][] odd=new int[10][10];

        Scanner input=new Scanner(System.in);
        System.out.println("Enter the length of array below 10: ");
        int length=input.nextInt();

        for (int i=0;i<length;i++)
        {
            for (int j=0;j<length;j++)
            {
                System.out.println("Enter the value"+i+":"+j);
                int value=input.nextInt();
                arr[i][j]=value;
            }
        }
        System.out.println("Your Array: ");
        for (int i=0;i<length;i++)
        {
            for (int j=0;j<length;j++)
            {
                System.out.print(arr[i][j]+" ");
                if (arr[i][j]%2==0)
                {
                    even[i][j]=arr[i][j];
                    
                }
                else
                {
                    odd[i][j]=arr[i][j];
                    
                }            
            }
            System.out.println();
        }
        System.out.println("Even array:");
        for (int i=0; i<length;i++)
        {
            for (int j=0;j<length;j++)
            {
                System.out.print(even[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("Odd array:");
        for (int i=0; i<length;i++)
        {
            for (int j=0;j<length;j++)
            {
                System.out.print(odd[i][j]+" ");
            }
            System.out.println();
        }
        


    }


    
}
