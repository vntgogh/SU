import java.util.InputMismatchException;
import java.util.Scanner;

public class TestSleep {
    public static void main(String[] args) {
        Scanner s= new Scanner(System.in);
        try{
            System.out.println("Entrez un entier:");
            int x= s.nextInt();
            if(x>0){
                System.out.println("Attente de "+x+" secondes");
                Thread.sleep(x*1000); 
                System.out.println("Fin de l'attente");
            }else{
                System.out.println("Le nombre est mal formé");
            }
        }catch(InputMismatchException e){
            System.out.println("Le nombre est mal formé");
        }catch(Exception e){    
            System.out.println("Interruption");
        }finally{
            s.close(); 
        }
    }
}
