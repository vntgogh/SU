package pobj.micros.fs;

import java.util.List;

import pobj.micros.errors.OSError;

public interface IFileSystem {
	public List<String> listDirectory(String path) throws OSError;	
	public void createDirectory(String path, String name) throws OSError;
	public IFileNode openFile(String path, String name, int createSize) throws OSError;
}
