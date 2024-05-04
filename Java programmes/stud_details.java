import java.util.Scanner;

import java.util.Scanner;

public class stud_details 
{
    public static void main(String[] args) 
    {
        //java programme to display student data using all data types

        Scanner input=new Scanner(System.in);

        String reg_no;
        String name;
        int age;
        char gender;
        double height;
        long colage_code;
        short district_code;
        byte marks;
        float percentage;
        boolean destiction;
        
        System.out.print("Enter the register no: ");
        reg_no=input.next();
        System.out.print("Enter the name: ");
        name=input.next();
        System.out.print("Enter the age: ");
        age=input.nextInt();
        System.out.print("Enter the gender: ");
        gender=input.next().charAt(0);
        System.out.print("Enter the height: ");
        height=input.nextDouble();
        System.out.print("Enter the collage code: ");
        colage_code=input.nextLong();
        System.out.print("Enter thet district code: ");
        district_code=input.nextShort();
        System.out.print("Enter the marks: ");
        marks=input.nextByte();
        System.out.print("Enter the percentage: ");
        percentage=input.nextFloat();
        if (percentage>=85) 
        {
            destiction=true;
            
        }
        else
        {
            destiction=false;
        }
        System.out.println("reg no: "+reg_no);
        System.out.println("name: "+name);
        System.out.println("age: "+age);
        System.out.println("gender :"+gender);
        System.out.println("height: "+height);
        System.out.println("collage code: "+colage_code);
        System.out.println("district code: "+district_code);
        System.out.println("marks: "+marks);
        System.out.println("percentage: "+percentage);
        System.out.println("Destiction: "+destiction);
        


        



    }
    
}
