package pobj.micros.fs;

import java.util.List;

import pobj.micros.errors.OSError;

public class FileSystem  implements IFileSystem{
	private IDirectoryNode racine;
	
	public FileSystem() {
		this.racine = new DirectoryNode("root");
	}

	@Override
	public List<String> listDirectory(String path) throws OSError {
		IDirectoryNode id = NodeUtils.findDirectory(this.racine,path);
		return id.getChildren();
	}

	@Override
	public void createDirectory(String path, String name) throws OSError {
		DirectoryNode dp = new DirectoryNode(path);
		dp.addChild(new Node(name));
	}

	@Override
	public IFileNode openFile(String path, String name, int createSize) throws OSError {
		for( String d : this.listDirectory(path)) {
			if(d == name) {
				IDirectoryNode id = NodeUtils.findDirectory(this.racine,path);
				id.getChild(name);
			}
		}
		return new FileNode(name,createSize);
	}
	
}
