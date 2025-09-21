package pobj.micros.fs;

public class FileNode extends Node implements IFileNode{
	private byte[] data;
	
	public FileNode(String name, int size) {
		super(name);
		this.data = new byte[size];
	}
	
	public int size() {
		return this.data.length;
	}
	
	public void write(int pos, int c) {
		if(0<=pos && pos<this.data.length) {
			data[pos] = (byte) c;
		}
	}
	
	public int read(int pos) {
		if(0<=pos && pos<this.data.length) {
			return data[pos];
		}
		return 255;
	}
	
	public INode copy() {
		FileNode f = new FileNode(this.getName(),this.data.length);
		byte[] n = new byte[this.data.length];
		for(int i = 0; i<this.data.length; i++) {
			n[i] = this.data[i];
		}
		return f;
	}
	
}
