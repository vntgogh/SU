package pobj.pkgman;

public interface IVersion extends Comparable<IVersion> {
	
	/** Retourne le numéro de version majeure. */
	public int getMajor();
	
	/** Retourne le numéro de version mineure. */
	public int getMinor();
	
	/** Conversion en chaîne de la forme : majeure.mineure. */
	public String toString();

	/** Retourne true si les numéros de version majeure et mineure correspondent. */
	public boolean equals(Object o);
	
	/** 
	 * Compare this à v et retourne :
	 *  1 si v est antérieur à this,
	 *  0 si v et this sont égaux,
	 * -1 si v est postérieur à this.
	 */
	public int compareTo(IVersion v);
}
