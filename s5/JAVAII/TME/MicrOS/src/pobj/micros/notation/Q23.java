package pobj.micros.notation;

import static org.junit.Assert.*;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

import org.junit.Test;

import pobj.micros.scheduler.IService;
import pobj.micros.scheduler.Service;

public class Q23 {

	@Test public void testPrivateFinal() {
		Service s = new Service("a",1);
		assertTrue(s instanceof IService);
		for (Field f : Service.class.getDeclaredFields()) {
			assertTrue("Attributes must be private", Modifier.isPrivate(f.getModifiers()));
			assertTrue("Attributes must be final", Modifier.isFinal(f.getModifiers()));
		}
	}
	
	@Test public void testGetters() {
		Service l1 = new Service("a",1);
		assertEquals("Incorrect getName()", "a", l1.getName());
		assertEquals("Incorrect getVersion()", 1, l1.getVersion());
	}

	@Test public void testToString() {
		Service l1 = new Service("a",1);
		assertEquals("Incorect toString()", "a/1",l1.toString());
	}

	@Test public void testEquals() {
		Service l1 = new Service("a",1);
		Service l2 = new Service("a",1);
		Service l3 = new Service("a",2);
		Service l4 = new Service("b",1);
		assertEquals("Incorrect equals", l1, l2);
		assertNotEquals("Incorrect equals",l1,l3);
		assertNotEquals("Incorrect equals",l1,l4);
		assertNotEquals("Incorrect equals",l3,l4);
	}

}
