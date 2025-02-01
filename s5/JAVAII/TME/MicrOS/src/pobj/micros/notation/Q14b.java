package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.fs.FileNode;
import pobj.micros.fs.FileSystem;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.IFileSystem;

public class Q14b {

	@Test public void testClass() {
		FileSystem fs = new FileSystem();
		assertSame("Must extend Object", Object.class, FileSystem.class.getSuperclass());
		assertTrue("Must implement IFileSystem", fs instanceof IFileSystem);
	}

	@Test public void testEmptyRoot() throws OSError {
		FileSystem fs = new FileSystem();
		assertTrue("Empty root", fs.listDirectory("").isEmpty());
	}
	
	@Test public void testDirectoryLevel1() throws OSError {
		FileSystem fs = new FileSystem();
		fs.createDirectory("", "a");
		assertEquals("List non-empty root directory", 1, fs.listDirectory("").size());
		assertTrue("List non-empty root directory", fs.listDirectory("").contains("a"));
	}
	
	@Test public void testDirectoryLevel2() throws OSError {
		FileSystem fs = new FileSystem();
		fs.createDirectory("", "a");
		fs.createDirectory("a", "b");
		assertEquals("List non-empty directory", 1, fs.listDirectory("a").size());
		assertTrue("List non-empty directory", fs.listDirectory("a").contains("b"));
	}
	
	@Test public void testDirectoryLevel3() throws OSError {
		FileSystem fs = new FileSystem();
		fs.createDirectory("", "a");
		fs.createDirectory("a", "b");
		fs.createDirectory("a/b", "c");
		assertEquals("List non-empty subdirectory", 1, fs.listDirectory("a/b").size());
		assertTrue("List non-empty subdirectory", fs.listDirectory("a/b").contains("c"));
	}

	@Test public void testFileLevel1() throws OSError {
		FileSystem fs = new FileSystem();
		IFileNode f = fs.openFile("", "ddd", 1024);
		assertEquals("List non-empty root directory", 1, fs.listDirectory("").size());
		assertTrue("List non-empty root directory", fs.listDirectory("").contains("ddd"));
		assertNotSame("Created file", null, f);
		assertTrue("Created file", f instanceof FileNode);
		assertEquals("Created file name", "ddd", f.getName());
		assertEquals("Created file size", 1024, f.size());
	}
	
	@Test public void testFileLevel2() throws OSError {
		FileSystem fs = new FileSystem();
		fs.createDirectory("", "a");
		IFileNode f = fs.openFile("a", "ddd", 1024);
		assertEquals("List non-empty root directory", 1, fs.listDirectory("a").size());
		assertTrue("List non-empty root directory", fs.listDirectory("a").contains("ddd"));
		assertNotSame("Created file", null, f);
		assertTrue("Created file", f instanceof FileNode);
		assertEquals("Created file name", "ddd", f.getName());
		assertEquals("Created file size", 1024, f.size());
	}
	
	@Test public void testFileReopen() throws OSError {
		FileSystem fs = new FileSystem();
		IFileNode f = fs.openFile("", "ddd", 1024);
		IFileNode g = fs.openFile("", "ddd", 1024);
		assertNotSame("Open file", null, g);
		assertSame("Open file", f, g);
	}
	
	@Test public void testFileReadWrite() throws OSError {
		FileSystem fs = new FileSystem();
		IFileNode f = fs.openFile("", "ddd", 1024);
		f.write(12, 100);
		assertEquals("File read and write", 100, f.read(12));
	}

	@Test(expected = OSError.class)  
	public void testErrorList() throws OSError {
		FileSystem fs = new FileSystem();
		fs.listDirectory("a");
	}

	@Test(expected = OSError.class)  
	public void testErrorCreateDirectory1() throws OSError {
		FileSystem fs = new FileSystem();
		fs.createDirectory("a", "b");
	}

	@Test(expected = OSError.class)  
	public void testErrorCreateDirectory2() throws OSError {
		FileSystem fs = new FileSystem();
		fs.createDirectory("", "a");
		fs.createDirectory("", "a");
	}

	@Test(expected = OSError.class)  
	public void testErrorCreateDirectory3() throws OSError {
		FileSystem fs = new FileSystem();
		fs.openFile("", "a", 1024);
		fs.createDirectory("", "a");
	}

	@Test(expected = OSError.class)  
	public void testErrorOpen() throws OSError {
		FileSystem fs = new FileSystem();
		fs.openFile("x", "ddd", 1024);
	}

	
}
