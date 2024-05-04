interface Car
{
   String car="Car";
}
interface Bike
{
    String bike="Bike";
    
}
interface Tesla extends Car,Bike
{
    public void print_both();
}
class display implements Tesla
{
    
    public void print_both()
    {
        System.out.println(car+" "+bike);
    }

}



public class multiple_inheritance 
{
    public static void main(String[] args) 
    {
        display display=new display();
        display.print_both();
        
    }

     
}