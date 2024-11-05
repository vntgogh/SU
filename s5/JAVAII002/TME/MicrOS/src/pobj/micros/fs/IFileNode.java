package pobj.micros.fs;

public interface IFileNode extends INode {
	public int size();
	public int read(int pos);
	public void write(int pos, int c);
}
