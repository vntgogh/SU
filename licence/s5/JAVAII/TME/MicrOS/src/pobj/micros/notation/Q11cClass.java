package pobj.micros.notation;

import static org.junit.Assert.*;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

import org.junit.Test;

import pobj.micros.fs.DirectoryNode;
import pobj.micros.fs.IDirectoryNode;
import pobj.micros.fs.Node;

public class Q11cClass {
	
	@Test public void testInstance() {
		DirectoryNode n = new DirectoryNode("a");
		assertTrue("Must implement IDirectoryNode", n instanceof IDirectoryNode);
		assertSame("Must extend Node", Node.class, DirectoryNode.class.getSuperclass());
	}

	@Test public void testPrivate() {
		for (Field f : DirectoryNode.class.getDeclaredFields()) {
			assertTrue("Attributes must be private", Modifier.isPrivate(f.getModifiers()));
		}	
	}	
	
}
