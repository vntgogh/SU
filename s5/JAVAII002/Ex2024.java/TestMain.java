public class TestMain {
    public static void main(String[] args){
        //A x = new A(); B y = new C(); x.f(y);
        //C x = new C(); A y = new C(); x.f(y);
        C x = new C(); C y = new C(); x.f(y);

    }
}
