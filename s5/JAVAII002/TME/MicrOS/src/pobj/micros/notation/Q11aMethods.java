package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.Node;

public class Q11aMethods {

	@Test public void testName() {
		Node a = new Node("a");
		Node b = new Node("b");
		assertEquals("getName() is incorrect", "a", a.getName());
		assertEquals("getName() is incorrect", "b", b.getName());
	}
	
}
