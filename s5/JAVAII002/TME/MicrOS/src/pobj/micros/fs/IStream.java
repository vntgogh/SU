package pobj.micros.fs;

public interface IStream {
	public int read();
	public void write(int c);
	public void seek(int pos);
	public int tell();
}
