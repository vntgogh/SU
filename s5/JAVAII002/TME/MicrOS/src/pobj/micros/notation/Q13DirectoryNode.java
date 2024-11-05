package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.DirectoryNode;
import pobj.micros.fs.IDirectoryNode;
import pobj.micros.fs.INode;
import pobj.micros.fs.Node;

public class Q13DirectoryNode {
	
	@Test public void testClass() {
		DirectoryNode n = new DirectoryNode("aaa");
		INode m = n.copy();
		assertTrue("Must return a DirectoryNode object", m instanceof DirectoryNode);
	}
	
	@Test public void testName() {
		DirectoryNode n = new DirectoryNode("aaa");
		INode m = n.copy();
		assertEquals("Invalid getName()", "aaa", m.getName());
	}
	
	@Test public void testIdentity() {
		DirectoryNode n = new DirectoryNode("aaa");
		INode m = n.copy();
		assertNotSame("Copy must return a new object", m, n);
	}

	@Test public void testCopy() {
		DirectoryNode d = new DirectoryNode("a");
		DirectoryNode x = new DirectoryNode("x");
		d.addChild(x);
		IDirectoryNode dd = (IDirectoryNode)d.copy();
		assertEquals("Incorrect directory copy", 1, dd.getChildren().size());
		assertTrue("Incorrect directory copy", dd.getChildren().contains("x"));
		assertFalse("Incorrect directory copy", dd.getChildren().contains("y"));
	}
	
	@Test public void testAddAfterCopy() {
		DirectoryNode d = new DirectoryNode("a");
		DirectoryNode x = new DirectoryNode("x");
		IDirectoryNode y = (IDirectoryNode)d.copy();
		d.addChild(x);
		assertEquals("Incorrect add after copy", 1, d.getChildren().size());
		assertTrue("Incorrect add after copy", d.getChildren().contains("x"));
		assertEquals("Incorrect add after copy", 0, y.getChildren().size());
		assertFalse("Incorrect add after copy", y.getChildren().contains("x"));
	}
		
	@Test public void testCopyRec() {
		DirectoryNode d = new DirectoryNode("a");
		DirectoryNode x = new DirectoryNode("x");
		DirectoryNode y = new DirectoryNode("y");
		d.addChild(x);
		x.addChild(y);
		IDirectoryNode dd = (IDirectoryNode)d.copy();
		assertEquals("Incorrect directory copy", 1, dd.getChildren().size());
		assertTrue("Incorrect directory copy", dd.getChildren().contains("x"));
		assertNotSame("Incorrect directory copy", null, dd.getChild("x"));
		assertTrue("Incorrect recursive directory copy", dd.getChild("x") instanceof IDirectoryNode);
		IDirectoryNode xx = (IDirectoryNode)dd.getChild("x");
		assertNotSame("Incorrect recursive directory copy", x, xx);
		assertEquals("Incorrect recursive directory copy", 1, xx.getChildren().size());
		assertTrue("Incorrect recursive directory copy", xx.getChildren().contains("y"));
		assertNotSame("Incorrect recursive directory copy", null, xx.getChild("y"));
		assertTrue("Incorrect recursive directory copy", xx.getChild("y") instanceof IDirectoryNode);
		IDirectoryNode yy = (IDirectoryNode)xx.getChild("y");
		assertNotSame("Incorrect recursive directory copy", y, yy);
	}
	

	class MyNode extends Node {
		public int called;
		public MyNode(String name) { super(name); }
		public INode copy() { called++; return new MyNode(getName()); }
	}
	
	@Test public void testDelegate() {
		DirectoryNode d = new DirectoryNode("a");
		MyNode n = new MyNode("u");
		d.addChild(n);
		d.copy();
		assertEquals("Incorrect delegation to copy()", 1, n.called);
	}

}
