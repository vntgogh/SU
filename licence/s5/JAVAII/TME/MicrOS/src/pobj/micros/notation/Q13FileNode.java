package pobj.micros.notation;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotSame;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import pobj.micros.fs.FileNode;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.INode;

public class Q13FileNode {
	
	@Test public void testClass() {
		FileNode n = new FileNode("aaa", 123);
		INode m = n.copy();
		assertTrue("Must return a FileNode object", m instanceof FileNode);
	}
	
	@Test public void testName() {
		FileNode n = new FileNode("aaa", 123);
		INode m = n.copy();
		assertEquals("Invalid getName()", "aaa", m.getName());
	}
	
	@Test public void testIdentity() {
		FileNode n = new FileNode("aaa", 123);
		INode m = n.copy();
		assertNotSame("Copy must return a new object", m, n);
	}

	@Test public void testSize() {
		FileNode n = new FileNode("aaa", 123);
		IFileNode m = (IFileNode) n.copy();
		assertEquals("Invalid size()", 123, m.size()); 
	}

	@Test public void testCopy() {
		FileNode n = new FileNode("aaa", 1024);
		n.write(100,  100);
		IFileNode m = (IFileNode)n.copy();
		assertEquals("Incorrect read after copy", 100, m.read(100));
	}
	
	@Test public void testNoalias() {
		FileNode n = new FileNode("aaa", 1024);
		n.write(100,  12);
		IFileNode m = (IFileNode)n.copy();
		n.write(100,  13);
		assertEquals("Incorrect read after copy", 12, m.read(100));
	}

}
