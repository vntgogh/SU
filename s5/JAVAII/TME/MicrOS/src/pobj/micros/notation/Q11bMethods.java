package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.FileNode;

public class Q11bMethods {

	@Test public void testName() {
		FileNode n = new FileNode("a", 1024);
		assertEquals("getName() is incorrect", "a", n.getName());
	}

	@Test public void testSize() {
		FileNode n = new FileNode("a", 1024);
		assertEquals("size() is incorrect", 1024, n.size());
	}

	@Test public void testReadWrite() {
		FileNode n = new FileNode("a", 1024);
		n.write(0, 100);
		n.write(1023,  101);
		assertEquals("Incorrect read after write", 100, n.read(0));
		assertEquals("Incorrect read after write", 101, n.read(1023));
	}

	@Test public void testOutOfBound() {
		FileNode n = new FileNode("a", 1024);
		n.write(0, 10);
		n.write(-1,  102);
		n.write(1024, 103);
		assertEquals("Incorrect read out of bounds", 255, n.read(-1));
		assertEquals("Incorrect read out of bounds", 255, n.read(1024));
		assertEquals("Incorrect write out of bounds", 10, n.read(0));
	}
	
}
