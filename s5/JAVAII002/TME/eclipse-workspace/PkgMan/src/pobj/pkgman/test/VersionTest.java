package pobj.pkgman.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import pobj.pkgman.IVersion;
import pobj.pkgman.Version;

public class VersionTest {

	@Test public void test1() {
		IVersion v = new Version(5,6);
		assertEquals(5, v.getMajor());
		assertEquals(6, v.getMinor());
		assertEquals("5.6", v.toString());
	}
	
	@Test public void test2() {
		IVersion v1 = new Version(5,6);
		IVersion v2 = new Version(5,6);
		assertEquals(v1,v2);
	}
	
	@Test public void test3() {
		IVersion v1 = new Version(1,9);
		IVersion v2 = new Version(2,3);
		assertTrue(v1.compareTo(v2) == -1);
		assertTrue(v2.compareTo(v1) == 1);
	}
}
