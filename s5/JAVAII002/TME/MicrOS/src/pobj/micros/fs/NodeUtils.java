package pobj.micros.fs;

import pobj.micros.errors.OSError;

public class NodeUtils {
	public static IDirectoryNode findDirectory(IDirectoryNode root, String path) throws OSError{
		if(path=="") {
			return root;
		}
		IDirectoryNode d;
		String[] x = path.split("/");
		d = (IDirectoryNode) root.getChild(x[0]);
		if(x.length == 1) {
			if(d==null) {
				throw new OSError("Invalid path");
			}
			return d;
		}
		for(int i = 1; i<x.length; i++) {
			d.addChild(new DirectoryNode(x[i]));
			if(d.getChild(x[i]) == null) {
				throw new OSError("Invalid path");
			}

			d = (IDirectoryNode) d.getChild(x[i]);
		}
		return d;
	}
}
