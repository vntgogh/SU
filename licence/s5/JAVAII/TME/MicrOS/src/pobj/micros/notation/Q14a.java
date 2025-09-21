package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.fs.DirectoryNode;
import pobj.micros.fs.NodeUtils;

public class Q14a {

	DirectoryNode root = new DirectoryNode("/");
	DirectoryNode a = new DirectoryNode("a");
	DirectoryNode b = new DirectoryNode("b");
	
	@Before public void before() {
		root.addChild(a);
		a.addChild( b);
	}
	
	@Test public void testClass() {
		assertSame("Must extend Object", Object.class, NodeUtils.class.getSuperclass());
	}

	@Test public void testRoot() throws OSError {
		assertSame("Cannot find root path", root, NodeUtils.findDirectory(root, "")); 
	}

	@Test public void testLevel1() throws OSError {
		assertSame("Cannot find directory in root", a, NodeUtils.findDirectory(root, "a"));
	}
	
	@Test public void testLevel2() throws OSError {
		assertSame("Cannot find directory in directory", b, NodeUtils.findDirectory(root, "a/b"));
	}
	
	@Test(expected = OSError.class)
	public void testErrorRoot()  throws OSError {
		NodeUtils.findDirectory(root, "aa");
	}

	@Test(expected = OSError.class)
	public void testErrorLevel1()  throws OSError {
		NodeUtils.findDirectory(root, "a/c");
	}

	@Test(expected = OSError.class)
	public void testErrorLevel2()  throws OSError {
		NodeUtils.findDirectory(root, "a/b/c");
	}

	@Test public void testAlias0() throws OSError {
		assertSame("Cannot handle path with extra /", root, NodeUtils.findDirectory(root, "/"));
	}
	
	@Test public void testAlias1() throws OSError {
		assertSame("Cannot handle path with extra /", a, NodeUtils.findDirectory(root, "a/"));
		assertSame("Cannot handle path with extra /", a, NodeUtils.findDirectory(root, "/a"));
		assertSame("Cannot handle path with extra /", a, NodeUtils.findDirectory(root, "/a/"));
	}

	@Test public void testAlias2() throws OSError {
		assertSame("Cannot handle path with extra /", b, NodeUtils.findDirectory(root, "a/b/"));
		assertSame("Cannot handle path with extra /", b, NodeUtils.findDirectory(root, "/a/b"));
		assertSame("Cannot handle path with extra /", b, NodeUtils.findDirectory(root, "/a/b/"));
	}

}
