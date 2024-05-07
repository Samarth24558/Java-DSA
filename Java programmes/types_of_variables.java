class Variable
{

    static void print_message(String val)
    {
        System.out.println(val);
    }
}

public class types_of_variables 
{
    static String message="This static variable";
    
    public static void main(String[] args) 
    {
        String value="This is local Variable";
        System.out.println(value);
        System.out.println(message);
        Variable.print_message("This is parameter Variable");
    }
}
