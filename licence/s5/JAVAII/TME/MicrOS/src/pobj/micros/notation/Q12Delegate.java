package pobj.micros.notation;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.fs.FileStream;
import pobj.micros.fs.IFileNode;
import pobj.micros.fs.IStream;

public class Q12Delegate {

	class MockFileNode implements IFileNode {
			public int readCalled, writeCalled;

			public int size() { return 99; }
			public String getName() { return "a"; }
			public IFileNode copy() { return null; }
		
			public int read(int pos) { 
				assertEquals("Invalid read delegation", 0, pos);
				readCalled++; 
				return 999; 
			}
		
			public void write(int pos, int c) { 
				assertEquals("Invalid write delegation", 1, pos); 
				assertEquals("Invalid write delegation", 100, c); 
				writeCalled++;
			}
	}
	
	@Test public void testDelegateRead() {
		MockFileNode m = new MockFileNode();
		IStream s = new FileStream(m);
		assertEquals("Invalid read delegation", 999, s.read());
		assertTrue("Invalid read delegation", 1 <= m.readCalled);
	}
	
	@Test public void testDelegateWrite() {
		MockFileNode m = new MockFileNode();
		IStream s = new FileStream(m);
		s.seek(1);
		s.write(100);
		assertTrue("Invalid write delegation", 1 <= m.writeCalled);
	}

}
