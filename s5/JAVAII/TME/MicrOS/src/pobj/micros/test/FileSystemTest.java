package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.fs.FileSystem;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.IFileSystem;

public class FileSystemTest {

	@Test public void test() throws OSError {
		IFileSystem fs = new FileSystem();
		fs.createDirectory("", "A");
		assertTrue(fs.listDirectory("").contains("A"));

		fs.createDirectory("A", "B");
		assertTrue(fs.listDirectory("A").contains("B"));
		
		IFileNode s = fs.openFile("A/B", "file", 1024);
		assertTrue(fs.listDirectory("A/B").contains("file"));

		s.write(0, 100);
		assertEquals(100, s.read(0));		
	}
	
}
