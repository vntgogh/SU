package pobj.micros.fs;

public class FileStream implements IStream {
	private int pos;
	private IFileNode node;
	
	public FileStream(IFileNode node) {
		this.pos = 0;
		this.node = node;
	}
	
	@Override
	public int read() {
		int tmp = this.pos;
		if(pos<this.node.size()) {
			pos++;
		}
		return this.node.read(tmp);
	}

	@Override
	public void write(int c) {
		this.node.write(this.pos,c);
		if(pos<this.node.size()) {
			pos++;
		}
	}

	@Override
	public void seek(int pos) {
		if(0<=pos) {
			this.pos = pos;
		}
	}

	@Override
	public int tell() {
		return this.pos;
	}
}
