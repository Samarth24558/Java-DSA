import java.util.Scanner;
public class generatetable {

    public static void main(String[] args) {
        
        int num;
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the number: ");
        num=input.nextInt();

        for(int i=1;i<=10;i++)
        {
            System.out.println(num*i);
        }


        input.close();

    }
}