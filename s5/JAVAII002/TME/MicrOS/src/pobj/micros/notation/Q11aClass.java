package pobj.micros.notation;

import static org.junit.Assert.*;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

import org.junit.Test;

import pobj.micros.fs.Node;
import pobj.micros.fs.INode;

public class Q11aClass {

	@Test public void testInstance() {
		Node n = new Node("a");
		assertTrue("Must implement INode", n instanceof INode);
		assertSame("Must extend Object", Object.class, Node.class.getSuperclass());
	}

	@Test public void testPrivate() {
		for (Field f : Node.class.getDeclaredFields()) {
			assertTrue("Attributes must be private", Modifier.isPrivate(f.getModifiers()));
		}	
	}
	
}
