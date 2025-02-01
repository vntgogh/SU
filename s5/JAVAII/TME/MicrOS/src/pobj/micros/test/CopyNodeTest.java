package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.DirectoryNode;
import pobj.micros.fs.FileNode;
import pobj.micros.fs.IDirectoryNode;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.INode;

public class CopyNodeTest {
	
	@Test public void test() {
		DirectoryNode d = new DirectoryNode("dir");
		FileNode f = new FileNode("file", 256);
		d.addChild(f);
		
		INode copy = d.copy();
		assertTrue(copy instanceof IDirectoryNode);
		assertNotEquals(d, copy);
		assertEquals("dir", copy.getName());
		assertNotEquals(null, ((IDirectoryNode)copy).getChild("file"));
		assertNotEquals(f, ((IDirectoryNode)copy).getChild("file"));
		assertTrue(((IDirectoryNode)copy).getChild("file") instanceof IFileNode);
		assertEquals("file", ((IDirectoryNode)copy).getChild("file").getName());
	}

}
