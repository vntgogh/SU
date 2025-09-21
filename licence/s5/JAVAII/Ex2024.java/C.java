public class C extends B{
    public void f(A x){
        System.out.println("4");
    }
    public void f(B x){
        System.out.println("5");
    }
    public void f(C x){
        super.f(x);
        System.out.println("6");
    }
}
