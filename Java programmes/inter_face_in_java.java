interface message
{
    public void print();
}

class Print implements message
{
    
    public void print()
    {
        System.out.println("This is message");
    }

}
public class inter_face_in_java
{
    public static void main(String[] args) 
    {

        Print print=new Print();
        print.print();
    }
    
}
