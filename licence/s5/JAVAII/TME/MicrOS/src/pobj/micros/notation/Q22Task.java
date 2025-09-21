package pobj.micros.notation;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

import org.junit.Before;
import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.scheduler.ExampleTask;
import pobj.micros.scheduler.FIFOStrategy;
import pobj.micros.scheduler.ITask;
import pobj.micros.scheduler.Scheduler;

public class Q22Task {

    ByteArrayOutputStream out = new ByteArrayOutputStream();

    @Before public void atBefore() {
            System.setOut(new PrintStream(out));
    }
    
    private String getOut() {
            System.out.flush();
            return out.toString().replaceAll("\\s+","");
    }


	@Test public void testClass() {
		ExampleTask t = new ExampleTask(2);
		assertTrue("Must implement ITask", t instanceof ITask);
		assertSame("Must extend Object", Object.class, ExampleTask.class.getSuperclass());
		for (Field f : ExampleTask.class.getDeclaredFields()) {
			assertTrue("Attributes must be private", Modifier.isPrivate(f.getModifiers()));
		}	
	}

	@Test public void testOnce() throws OSError {
    	ExampleTask t = new ExampleTask(2);
		Scheduler sch = new Scheduler(new FIFOStrategy());
		t.exec(sch);
		assertEquals("2", getOut());
    }
    
    @Test public void testTwice() throws OSError {
    	ExampleTask t = new ExampleTask(2);
		Scheduler sch = new Scheduler(new FIFOStrategy());
		t.exec(sch);
		assertTrue(sch.execNext());
		assertEquals("21", getOut());
	}

    @Test public void testThird() throws OSError {
    	ExampleTask t = new ExampleTask(2);
 		Scheduler sch = new Scheduler(new FIFOStrategy());
 		t.exec(sch);
 		assertTrue(sch.execNext());
 		assertTrue(sch.execNext());
 		assertEquals("211", getOut());
 	}
	
    @Test public void testAll() throws OSError {
    	ExampleTask t = new ExampleTask(2);
 		Scheduler sch = new Scheduler(new FIFOStrategy());
 		t.exec(sch);
 		assertTrue(sch.execNext());
 		assertTrue(sch.execNext());
 		assertTrue(sch.execNext());
 		assertTrue(sch.execNext());
 		assertTrue(sch.execNext());
 		assertTrue(sch.execNext());
 		assertEquals("2110000", getOut());
 	}
	
    @Test public void testEnd() throws OSError {
  		ExampleTask t = new ExampleTask(0);
  		Scheduler sch = new Scheduler(new FIFOStrategy());
  		t.exec(sch);
  		assertEquals("0", getOut());
  		assertFalse(sch.execNext());
  	}
 	
}
