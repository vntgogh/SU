public class TrianglePascal{
    private int[][] x;

    public TrianglePascal(int n){
        this.x= new int[n][];

        for(int i=0; i<n;i++){
            x[i]=new int[i];
        }
    }

    public void remplirTriangle(){
        for (int i=0; i<x.length;i++){
            x[i][0]=1;
            x[i][i]=1;
            if(i>1){
                for (int j=0; j<i; j++){
                    x[i][j]= x[i-1][j-1] + x[i-1][j];
                }
            }
        }
    } 

    public String toString(){
        StringBuilder strBuild= new StringBuilder(x[0][0]);
        for (int i=1; i<x.length; x++){
            for (int j=0; j<i; j++){
                strBuild.append(x[i][j]);
            }
            strBuild.append("\n");
        }
        return strBuild.toString();
    }
}