package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.FileNode;
import pobj.micros.fs.FileStream;

public class Q12Methods {

	@Test public void testRead() {
		FileNode data = new FileNode("a", 1024);
		data.write(0,  100);
		FileStream s = new FileStream(data);
		assertEquals("Incorrect stream read", 100, s.read());
	}

	@Test public void testWrite() {
		FileNode data = new FileNode("a", 1024);
		FileStream s = new FileStream(data);
		s.write(101);
		assertEquals("Incorrect stream write", 101, data.read(0));
	}
	
	@Test public void testMultiRead() {
		FileNode data = new FileNode("a", 1024);
		data.write(0,  100);
		data.write(1,  101);
		data.write(2,  102);
		FileStream s = new FileStream(data);
		assertEquals("Incorrect stream read", 100, s.read());
		assertEquals("Incorrect stream read", 101, s.read());
		assertEquals("Incorrect stream read", 102, s.read());
	}

	@Test public void testMultiWrite() {
		FileNode data = new FileNode("a", 1024);
		FileStream s = new FileStream(data);
		s.write(101);
		s.write(102);
		s.write(103);
		assertEquals("Incorrect stream write", 101, data.read(0));
		assertEquals("Incorrect stream write", 102, data.read(1));
		assertEquals("Incorrect stream write", 103, data.read(2));
	}

	@Test public void testMultiReadWrite() {
		FileNode data = new FileNode("a", 1024);
		data.write(1,  100);
		FileStream s = new FileStream(data);
		s.write(99);
		assertEquals("Incorrect stream read", 100, s.read());
		assertEquals("Incorrect stream write", 99, data.read(0));
		assertEquals("Incorrect stream write", 100, data.read(1));
	}
	
	@Test public void testReadTell() {
		FileNode data = new FileNode("a", 1024);
		FileStream s = new FileStream(data);
		assertEquals("Incorrect tell()", 0, s.tell());
		s.read();
		assertEquals("Incorrect tell() after read", 1, s.tell());
	}
	
	@Test public void testWriteTell() {
		FileNode data = new FileNode("a", 1024);
		FileStream s = new FileStream(data);
		assertEquals("Incorrect  tell()", 0, s.tell());
		s.write(12);
		assertEquals("Incorrect tell() after read", 1, s.tell());
	}

	@Test public void testSeekTell() {
		FileNode data = new FileNode("a", 1024);
		FileStream s = new FileStream(data);
		s.seek(40);
		assertEquals("Incorrect tell after seek", 40, s.tell());
	}
	@Test public void testSeekRead() {
		FileNode data = new FileNode("a", 1024);
		data.write(50,  100);
		FileStream s = new FileStream(data);
		s.seek(50);
		assertEquals("Incorrect read after seek", 100, s.read());
	}

	@Test public void testSeekWrite() {
		FileNode data = new FileNode("a", 1024);
		FileStream s = new FileStream(data);
		s.seek(60);
		s.write(101);
		assertEquals("Incorrect write after seek", 101, data.read(60));
	}

	@Test public void testOutOfBound() {
		FileNode data = new FileNode("a", 2);
		FileStream s = new FileStream(data);
		s.write(0);
		s.write(0);
		s.write(0);
		assertEquals("Incorrect  out of bound read",255, s.read());
		assertEquals("Incorrect  out of bound read / write", 2, s.tell());
	}

}
