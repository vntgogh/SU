package pobj.micros.notation;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Test;

import pobj.micros.scheduler.IStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.errors.OSError;
import pobj.micros.scheduler.FIFOStrategy;

public class Q21aFIFO {
	
	class MockTask implements ITask {
		public void exec(IScheduler sched) throws OSError { }
	}

	@Test public void testClass() {
		assertTrue("FIFOStragety must implement IStrategy", new FIFOStrategy() instanceof IStrategy);
		assertSame("FIFOStrategy must extend Object", Object.class, FIFOStrategy.class.getSuperclass());
		assertEquals("FIFOStrategy must not have any attribute", 0, FIFOStrategy.class.getDeclaredFields().length);
	}
	
	@Test public void testFIFOOne() {
		FIFOStrategy p = new FIFOStrategy();
		ITask t1 = new MockTask();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t1); 
		assertSame("Select one task", t1, p.selectTask(l));
	}

	@Test public void testFIFOOneRemove() {
		FIFOStrategy p = new FIFOStrategy();
		ITask t1 = new MockTask();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t1); 
		p.selectTask(l);
		assertEquals("selectTask removes tasks", 0, l.size());
	}

	@Test public void testFIFOTwo() {
		FIFOStrategy p = new FIFOStrategy();
		ITask t1 = new MockTask();
		ITask t2 = new MockTask();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t1); 
		l.addFirst(t2);
		assertSame("Select two tasks", t1, p.selectTask(l));
		assertEquals("Select two tasks", 1, l.size());
		assertSame("Select two tasks", t2, p.selectTask(l));
		assertEquals("Select two tasks", 0, l.size());
	}

	@Test public void testFIFONull() {
		FIFOStrategy p = new FIFOStrategy();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(new MockTask()); 
		p.selectTask(l);
		assertSame("Returns null when no more tasks", null, p.selectTask(l));
	}
	
}
