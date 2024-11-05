package pobj.pkgman.log;

public class LogBuffer implements ILogger{
	private String sb;
	
	public LogBuffer() {
		this.sb = "";
	}

	@Override
	public void log(String msg) {
		this.sb+=msg+'\n';
		
	}

	@Override
	public String getLog() {
		return this.sb;
	}

}
