package pobj.pkgman.test;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import pobj.pkgman.log.ILogger;
import pobj.pkgman.log.LogBuffer;

public class LogBufferTest {
	
	@Test public void test() {
		ILogger log = new LogBuffer();
		log.log("AA");
		log.log("BB");
		assertEquals("AA\nBB\n", log.getLog());
	}
	
}
