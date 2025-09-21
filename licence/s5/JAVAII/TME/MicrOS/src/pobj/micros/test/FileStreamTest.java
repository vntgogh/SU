package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.FileNode;
import pobj.micros.fs.FileStream;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.IStream;

public class FileStreamTest {

	@Test public void test() {
		IFileNode f = new FileNode("name", 256);
		f.write(0, 25);
		
		IStream s = new FileStream(f);
		assertEquals(0, s.tell());
		assertEquals(25, s.read());
		assertEquals(1, s.tell());
		s.seek(0);
		assertEquals(0, s.tell());
	}

}
