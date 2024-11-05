package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.fs.DirectoryNode;
import pobj.micros.fs.IDirectoryNode;
import pobj.micros.fs.NodeUtils;

public class NodeUtilsTest {

	@Test public void test() throws OSError {
		IDirectoryNode root = new DirectoryNode("root");
		IDirectoryNode dir1 = new DirectoryNode("dir1");
		IDirectoryNode dir2= new DirectoryNode("dir2");
		root.addChild(dir1);
		dir1.addChild(dir2);
		assertEquals(root, NodeUtils.findDirectory(root, ""));
		assertEquals(dir1, NodeUtils.findDirectory(root, "dir1"));
		assertEquals(dir2, NodeUtils.findDirectory(root, "dir1/dir2"));
	}
}
