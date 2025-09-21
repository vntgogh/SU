package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.FileNode;
import pobj.micros.fs.IFileNode;

public class FileNodeTest {

	@Test public void test() {
		IFileNode n = new FileNode("name", 256);
		assertEquals("name", n.getName());
		assertEquals(256, n.size());
		n.write(10, 100);
		assertEquals(100, n.read(10));
		assertEquals(255, n.read(-1));
	}
}
