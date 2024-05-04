import java.util.Scanner;
public class inchtocenti {
    public static void main(String[] args) {

        float inch;
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the inch: ");
        inch=input.nextFloat();
        System.out.println("Centimeter is: "+inch*2.54);

        
        input.close();
    }
    
}
