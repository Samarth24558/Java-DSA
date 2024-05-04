import java.util.Scanner;

public class array_in_java {

    public static void main(String[] args) {
        
        int e=0,o=0;

        int[] arr=new int[10];

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the lenth of array below ten: ");
        int l=input.nextInt();

        for(int i=0;i<l;i++)
        {
            System.out.print("Enter the element: ");
            int val=input.nextInt();
            arr[i]=val;
        }

        for(int i=0;i<l;i++)
        {
            if(arr[i]%2==0)
            {
                e++;
            }
            else
            {
                o++;
            }
        }
        System.out.println("Even numbers in array: "+e);
        System.out.println("Odd numbers in array: "+o);
        

    }
}