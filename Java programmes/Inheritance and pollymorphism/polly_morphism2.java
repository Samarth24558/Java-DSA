class Addition
{

    void add(int a,int b,int c)
    {
        System.out.print("all are integer parameters: ");
        System.out.println(a+b+c);
    }
    void add (float a,float b,int c)
    {
        System.out.print("2 float and 1 integer parameters: ");
        System.out.println(a+b+c);
    }
    void add (int a, int b,float c)
    {
        System.out.print("2 interger and 1 float parameters: ");        
        System.out.println(a+b+c);

    }
    void add(float a, float b, float c)
    {
        System.out.print("all are float parameters: ");
        System.out.println(a+b+c);
    }
}


public class polly_morphism2 {
    public static void main(String[] args) 
    {
        Addition add=new Addition();

        add.add(120, 12, 20);
        add.add(23.0f, 78.6f, 68.9f);
        add.add(23.5f, 10.2f, 89);
        add.add(24, 60, 80.5f);
        
    }
}
