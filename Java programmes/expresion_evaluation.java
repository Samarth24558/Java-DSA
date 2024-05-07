import java.util.Scanner;
public class expresion_evaluation 
{
    public static void main(String[] args) 
    {

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the radius of semi-circle: ");
        float radius=input.nextFloat();
        float area=(3.14f*radius*radius)/2;
        System.out.println("Area of semi-circle is: "+area);

        
        
    }

    
}