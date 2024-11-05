package pobj.pkgman.log;

public interface ILogger {
	
	/** Ajoute la chaîne 'msg' suivie de '\n' au buffer. */
	public void log(String msg);
	
	/** Retourne le buffer sous forme de chaîne. */
	public String getLog();
}
