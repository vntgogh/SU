package pobj.micros.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertSame;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import pobj.micros.fs.DirectoryNode;
import pobj.micros.fs.IDirectoryNode;

public class DirectoryNodeTest {
	
	@Test public void test() {
		IDirectoryNode d1 = new DirectoryNode("root");
		IDirectoryNode d2 = new DirectoryNode("one");
		d1.addChild(d2);

		assertTrue(d2.getChildren().isEmpty());
		assertEquals(1, d1.getChildren().size());
		assertSame(d2, d1.getChild("one"));
		assertSame(null, d1.getChild("two"));
		assertTrue(d1.getChildren().contains("one"));
	}	
	
}
