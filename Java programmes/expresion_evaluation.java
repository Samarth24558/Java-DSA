import java.util.Scanner;
public class expresion_evaluation 
{
    public static void main(String[] args) 
    {

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the radius of semi-circle: ");
        double radius=input.nextDouble();
        double area=1/2*(3.14*radius*radius);
        System.out.println("Area of semi-circle is: "+area);

        
        
    }

    
}