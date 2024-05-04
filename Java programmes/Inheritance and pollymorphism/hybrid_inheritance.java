class Vychicle
{
    String company="Tesla";

}
class car extends Vychicle
{
    String model="Tesla";
    int wheels=4;

}
class bike extends Vychicle
{
    int wheels=2;
    String model="Activa";
}
class Cycle extends bike
{

}
public class hybrid_inheritance
{
    public static void main(String[] args) 
    {
        Cycle cycle=new Cycle();
        System.out.println(cycle.company+" "+cycle.wheels);
    }
}
