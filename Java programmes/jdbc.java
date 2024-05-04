// java programme to connect JDBC
import java.sql.*;
import java.sql.SQLException;

public class jdbc 
{

    public static void main(String[] args) 
    {
        try{

            Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/car_details", "root", "mysql");

            System.out.println("Connected successfully");
            Statement st=con.createStatement();
            ResultSet res=st.executeQuery("select * from car");

            while (res.next()) 
            {
                String name;
                name=res.getString("car_name");
                System.out.println(name);
                
            }
            res.close();
            st.close();
            con.close();


        }
        catch(SQLException e)
        {
            e.printStackTrace();
        }
    
}
}