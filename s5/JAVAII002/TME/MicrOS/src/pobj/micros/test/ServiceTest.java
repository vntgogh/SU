package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.scheduler.IService;
import pobj.micros.scheduler.Service;

public class ServiceTest {

	@Test public void testGetters() {
		IService s1 = new Service("service",1);
		assertEquals("service", s1.getName());
		assertEquals(1, s1.getVersion());
		assertEquals("service/1", s1.toString());

		IService s2 = new Service("service",1);
		assertEquals(s1, s2);
		assertEquals(s1.hashCode(), s2.hashCode());
	}
}
