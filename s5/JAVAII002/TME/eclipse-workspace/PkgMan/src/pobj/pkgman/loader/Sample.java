package pobj.pkgman.loader;

import java.io.IOException;
import java.util.List;

import org.junit.Test;

import pobj.pkgman.IPkg;

public class Sample {			
		public void printPkgs(List<IPkg> packages){
			for (IPkg p : packages) {
				System.out.print(p.toString()+": ");
				for(IPkg d : p.getDependencies()) {
					System.out.println(d.toString()+" ");
				}
			}				
		}
		
		@Test public void test() throws IOException{
			PkgLoader fic = new PkgLoader("src/pobj/pkgman/loader/example.txt");
			printPkgs(fic.getPackages());
		}
}
