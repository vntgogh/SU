package pobj.micros.fs;

import pobj.micros.errors.OSError;

public class NodeUtils {
	public static IDirectoryNode findDirectory(IDirectoryNode root, String path) throws OSError{
		if(path=="") {
			return root;
		}
		IDirectoryNode d = new DirectoryNode("root");
		String[] tpath = path.split("/");
		if(tpath==null) {
			return root;
		}
		IDirectoryNode rnode= new DirectoryNode(tpath[0]);
		root.addChild(rnode);
		for(int i = 1; i<tpath.length-1;i++) {
			if(i==1) {
				rnode.addChild(new Node(tpath[i-1]));
			}
			IDirectoryNode nnode = new DirectoryNode(tpath[i-1]);			
			nnode.addChild(new Node(tpath[i]));
		}
		

		return d;
	}
}
