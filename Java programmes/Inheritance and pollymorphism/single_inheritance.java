class Base
{

    public void print_Base()
    {
        System.out.println("Base class");
    }
}
class Derived extends Base
{
    public void print_message()
    {
        System.out.println("inherited class");
    }
}    
public class single_inheritance 
{
    public static void main(String[] args) {
        Derived obj=new Derived();
        obj.print_Base();
        obj.print_message();
    }
}
