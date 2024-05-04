class A 
{
    String display()
    {
        System.out.println("Class A");
        return null;

    }
}
class B extends A
{
    
}
class C extends A
{
   
}
class D extends A
{
    
}
public class hirarchical_inheritance
{
    public static void main(String[] args) {
        B b=new B();
        C c=new C();
        D d=new D();       

        System.out.println(b.display());
    }
}