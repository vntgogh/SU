package pobj.pkgman;

public class Version implements Comparable<IVersion>, IVersion{
	private final int major;
	private final int minor;	
	
	public Version(int maj,int min) {
		this.major=maj;
		this.minor=min;
	}
	
	public int getMajor() { return this.major; }
	public int getMinor() { return this.minor; }
	
	public boolean equals(Object o) {
		if (o instanceof Version) {
			if(((Version) o).getMajor()==this.getMajor()&&((Version) o).getMinor()==this.getMinor()) {
				return true;
			}
		}
		return false;
	}
	
	public String toString() {
		return this.getMajor()+"."+this.getMinor();
	}
	
	@Override
	public int compareTo(IVersion o) {
		if(this.equals(o)==true) {
			return 0;
		}
		if(this.getMajor()<o.getMajor()) {
			return -1;
		}
		if(this.getMajor()>o.getMajor()) {
			return 1;
		}
		if(this.getMinor()<o.getMinor()) {
			return -1;
		}
		return 1;
	}
	
	public static IVersion getDefaultVersion() {
		return (IVersion) new Version(1,0);
	}
}
