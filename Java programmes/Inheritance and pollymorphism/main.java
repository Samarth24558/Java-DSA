import java.io.IOException;
import java.io.FileReader;;

public class main
{
    public static void main(String[] args) 
    {
        try
        {
            FileReader reader=new FileReader("First.txt");
            int end=reader.read();
            while (end!=-1)
            {
                System.out.print((char)end);
                end=reader.read();

            }
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }
}
