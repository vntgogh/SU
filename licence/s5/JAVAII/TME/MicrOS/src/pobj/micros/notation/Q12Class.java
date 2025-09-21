package pobj.micros.notation;

import static org.junit.Assert.*;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

import org.junit.Test;

import pobj.micros.fs.FileNode;
import pobj.micros.fs.FileStream;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.IStream;

public class Q12Class {

	@Test public void testInstance() {
		FileNode f = new FileNode("aa" ,1024);
		FileStream e = new FileStream(f);
		assertTrue("Must implement IStream", e instanceof IStream);
		assertSame("Must extend Object", Object.class, FileStream.class.getSuperclass());
	}

	@Test public void testPrivate() {
		for (Field f : FileStream.class.getDeclaredFields()) {
			assertTrue("Attributes must be private", Modifier.isPrivate(f.getModifiers()));
		}	
	}
	
	@Test public void testAttr() {
		for (Field f : FileStream.class.getDeclaredFields()) {
			if (f.getType() == IFileNode.class) return;
		}
		fail("Must have a IFileNode attribute");
	}


}
