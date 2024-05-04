class Add
{
    static int add(int num1,int num2)
    {
        return num1+num2;
    }
    static double add(double num1,double num2)
    {
        return num1+num2;
    }

}
public class polly_morphism {

    public static void main(String[] args)
    {
        System.out.println(Add.add(10, 10));
        System.out.println(Add.add(10.9, 10.0));
    }
}