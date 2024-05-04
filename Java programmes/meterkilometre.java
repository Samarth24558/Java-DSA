//Java programme to convert meter to kilometer

import java.util.Scanner;
public class meterkilometre {

    public static void main(String[] args) 
    {
        float m,km;

        Scanner input=new Scanner(System.in);
        System.out.print("Enter the meter: ");
        m=input.nextFloat();
        km=m/1000;
        System.out.println("Kilometer is: "+km);
        input.close();
        

        
    }
}