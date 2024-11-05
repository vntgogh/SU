package pobj.pkgman.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

import org.junit.Test;

import pobj.pkgman.updater.Connector;
import pobj.pkgman.updater.IConnector;
import pobj.pkgman.updater.IDatabase;

public class ConnectorTest {

	@Test public void test1() {
		IConnector c = new Connector("src/pobj/pkgman/loader/example.txt");
		IDatabase db = c.getDatabase();
		assertEquals("eclipse", db.getPackage("eclipse").getName());
		assertEquals(4, db.getPackage("eclipse").getVersion().getMajor());
		assertEquals(8, db.getPackage("java").getVersion().getMajor());
		assertNull(db.getPackage("help"));
	}

	@Test public void test2() {
		IConnector c = new Connector("does-not-exist.txt");
		IDatabase db = c.getDatabase();
		assertNull(db);
	}
}
