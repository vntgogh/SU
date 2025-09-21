public class Complexe{
    private double reelle, imag;
    public Complexe(double reelle, double imag){
        this.reelle=reelle;
        this.imag=imag;
    }
    public Complexe(){
        this(Math.random()*2, Math.random()*2);
    }
    public String toString(){
        return "( "+this.reelle+" + "+this.imag+"i )";
    }
    public void estReel(){
        if (this.imag == 0){
            System.out.println(this.reelle+" est un reel.");
        }else{
            System.out.println(this.reelle+" n'est pas un reel.");
        }
    }
    public Complexe addition(Complexe c){
        Complexe ac= new Complexe(this.reelle+c.reelle, this.imag+c.imag);
        return ac;
    }
    public Complexe multiplication(Complexe c){
        Complexe mc= new Complexe((this.reelle*c.reelle -this.imag*c.imag), (this.reelle*c.imag + this.imag*c.reelle));
        return mc;
    }
}