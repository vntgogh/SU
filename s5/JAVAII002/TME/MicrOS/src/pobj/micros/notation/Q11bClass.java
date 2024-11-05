package pobj.micros.notation;

import static org.junit.Assert.*;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

import org.junit.Test;

import pobj.micros.fs.FileNode;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.Node;

public class Q11bClass {

	@Test public void testInstance() {
		FileNode n = new FileNode("a", 1024);
		assertTrue("Must implement IFileNode", n instanceof IFileNode);
		assertSame("Must extend Node", Node.class, FileNode.class.getSuperclass());
	}
	
	@Test public void testPrivate() {
		for (Field f : FileNode.class.getDeclaredFields()) {
			assertTrue("Attributes must be private", Modifier.isPrivate(f.getModifiers()));
		}	
	}
}
