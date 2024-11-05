package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.DirectoryNode;

public class Q11cMethods {

	@Test public void testName() {
		DirectoryNode d = new DirectoryNode("a");
		assertEquals("getName() is incorrect", "a",  d.getName());
	}
	
	@Test public void testEmpty() {
		DirectoryNode d = new DirectoryNode("a");
		assertTrue("isEmpty() is incorrect for empty directory", d.getChildren().isEmpty());
	}
	
	@Test public void testAddEmpty() {
		DirectoryNode d = new DirectoryNode("a");
		assertTrue("addChild must return true", d.addChild(new DirectoryNode("b")));
		assertFalse("isEmpty() is incorrect for non-empty directory", d.getChildren().isEmpty());
	}
	
	@Test public void testAddGet() {
		DirectoryNode d = new DirectoryNode("a");
		DirectoryNode d1 = new DirectoryNode("x");
		DirectoryNode d2 = new DirectoryNode("y");
		d.addChild(d1);
		d.addChild(d2);
		assertSame("getChild after addChild is incorrect", d1, d.getChild("x"));
		assertSame("getChild after addChild is incorrect", d2, d.getChild("y"));
		assertSame("getChild without addChild is incorrect", null, d.getChild("z"));
	}
	
	@Test public void testAddTwice() {
		DirectoryNode d = new DirectoryNode("a");
		DirectoryNode d1 = new DirectoryNode("x");
		DirectoryNode d2 = new DirectoryNode("x");
		d.addChild(d1);
		d.addChild(d2);
		assertSame("getChild after addChild is incorrect", d1, d.getChild("x"));
		assertEquals("getChildren size incorrect", 1, d.getChildren().size());
	}
	
	@Test public void testAddReturn() {
		DirectoryNode d = new DirectoryNode("a");
		DirectoryNode d1 = new DirectoryNode("x");
		DirectoryNode d2 = new DirectoryNode("x");
		assertTrue("addChild must return true", d.addChild(d1));
		assertFalse("addChild must return false", d.addChild(d2));	
	}

		@Test public void testGetChildren() {
		DirectoryNode d = new DirectoryNode("a");
		DirectoryNode d1 = new DirectoryNode("x");
		DirectoryNode d2 = new DirectoryNode("y");
		d.addChild(d1);
		d.addChild(d2);
		assertEquals("getChildren size incorrect", 2, d.getChildren().size());
		assertTrue("getChildren after addChild is incorrect", d.getChildren().contains("x"));
		assertTrue("getChildren after addChild is incorrect", d.getChildren().contains("y"));
		assertFalse("getChildren without addChild is incorrect", d.getChildren().contains("z"));
	}
		
}
