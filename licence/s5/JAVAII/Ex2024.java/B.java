public class B extends A{
    public void f(A x){
        System.out.println("2");
    }
    public void f(B x){
        super.f(x);
        System.out.println("3");
    }
}
