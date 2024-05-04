class Parent
{
    void print_base()
    {
        System.out.println("Parent class called");

    }
}
class FirstDerived extends Parent
{
    void print_fderived()
    {
        System.out.println("Derived class called");
    }
}
class subderived extends FirstDerived
{
    void print_subderived()
    {
        System.out.println("Sub derived class called");
    }
}

public class multi_level_inheritance 
{

    public static void main(String[] args)
    {

        subderived obj=new subderived();
        obj.print_base();
        obj.print_fderived();
        FirstDerived obj2=new FirstDerived();
        obj2.print_base();
    }
}