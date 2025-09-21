package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.INode;
import pobj.micros.fs.Node;

public class Q13Node {
	
	@Test public void testClass() {
		Node n = new Node("aaa");
		INode m = n.copy();
		assertTrue("Must return a Node object", m instanceof Node);
	}
	
	@Test public void testName() {
		Node n = new Node("aaa");
		INode m = n.copy();
		assertEquals("Invalid getName()", "aaa", m.getName());
	}
	
	@Test public void testIdentity() {
		Node n = new Node("aaa");
		INode m = n.copy();
		assertNotSame("Copy must return a new object", m, n);
	}
}
