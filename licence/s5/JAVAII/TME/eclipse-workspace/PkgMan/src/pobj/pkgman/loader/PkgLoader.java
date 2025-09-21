package pobj.pkgman.loader;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import pobj.pkgman.IPkg;
import pobj.pkgman.IVersion;
import pobj.pkgman.LimitPkg;
import pobj.pkgman.Version;

public class PkgLoader {

	private List<IPkg> pkgs;
	
	/**
	 * Ouvre le fichier 'file' et charge les paquets contenus.
	 * Voir 'example.txt' pour un exemple de fichier de paquets.
	 * Signale IOException en cas d'erreur de lecture.
	 * 
	 * Les classes Version et LimitPkg sont utilisées pour créer les paquets.
	 */
	public PkgLoader(String file) throws IOException {
		pkgs = new ArrayList<>();
		
		// Ouverture du fichier
		BufferedReader r = new BufferedReader(new FileReader(file));
		while (true) {
			// Lecture d'une ligne
			String line = r.readLine();
			if (line==null) break;
			line = line.trim();
			if (line.equals("")) continue;
			
			// Découpage au niveau du caractère :
			// entre le paquet déclaré et ses dépendances
			String [] l = line.split(":");

			// Découpage du premier paquet au niveau du caractère -
			// entre un nom et un numéro de version
			String [] f = l[0].trim().split("-");
			if (f.length != 2) continue;
			
			// Extraction du nom
			String name = f[0];
			
			// Découpage du numéro de version au niveau du caractère .
			// entre le numéro majeur et le numéro mineur
			String [] v = f[1]. trim().split("\\.");
			if (v.length != 2) continue;
			
			// Création de l'objet IVersion
			IVersion ver = new Version(Integer.valueOf(v[0]), Integer.valueOf(v[1]));

			// Découpage de la liste de dépendances au niveau du caractère espace 
			String [] ps =l.length > 1 ?  l[1].trim().split("\\s+") : new String[0];
			
			// Récupération de l'objet IPkg correspondant à chaque dépendance
			// la dépendance doit exister dans la liste pkgs, donc être définie
			// dans le fichier avant les paquets qui en dépendent
			List<IPkg> deps = new ArrayList<>();
			for (String s : ps) {
				for (IPkg p : pkgs) {
					if (p.toString().equals(s)) {
						deps.add(p);
						break;
					}
				}
			}
			
			// Création de l'objet IPkg
			IPkg pkg = new LimitPkg(name, ver, deps);

			// Ajout dans la liste des paquets
			pkgs.add(pkg);
		}
		r.close();
	}

	/** Retourne la liste des paquets chargés par le contructeur. */
	public List<IPkg> getPackages() {
		return pkgs;
	}

}
