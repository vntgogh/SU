package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.Node;
import pobj.micros.fs.INode;

public class NodeTest {

	@Test public void test1() {
		Node n = new Node("name");
		assertTrue(n instanceof INode);
	}
	
	@Test public void test2() {
		Node a = new Node("name");
		assertEquals("name", a.getName());
	}
}
