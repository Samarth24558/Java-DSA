import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class file_handaling 
{
    public static void main(String[] args) 
    {
        try{
        FileReader file=new FileReader("First.txt");

        int b=file.read();

        while(b!=-1)
        {
            System.out.print((char)b);
            b=file.read();
        }

        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        
        
        try
        {
            FileWriter file=new FileWriter("First.txt");
            file.write("Hello world");
            file.append("\nSamarth");
            file.close();
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }


    }
    
}
