package pobj.micros.notation;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Test;

import pobj.micros.scheduler.IStrategy;
import pobj.micros.scheduler.MostRecentStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.errors.OSError;

public class Q21aMostRecent {
	
	class MockTask implements ITask {
		public void exec(IScheduler sched) throws OSError { }
	}

	@Test public void testClass() {
		assertTrue("MostRecentStragety must implement IStrategy", new MostRecentStrategy() instanceof IStrategy);
		assertSame("MostRecentStrategy must extend Object", Object.class, MostRecentStrategy.class.getSuperclass());
		assertEquals("MostRecentStrategy must not have any attribute", 0, MostRecentStrategy.class.getDeclaredFields().length);
	}
	
	@Test public void testMostRecentOne() {
		MostRecentStrategy p = new MostRecentStrategy();
		ITask t1 = new MockTask();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t1); 
		assertSame("Select one task", t1, p.selectTask(l));
	}

	@Test public void testMostRecentOneRemove() {
		MostRecentStrategy p = new MostRecentStrategy();
		ITask t1 = new MockTask();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t1); 
		p.selectTask(l);
		assertEquals("selectTask removes tasks", 0, l.size());
	}

	@Test public void testMostRecentTwo() {
		MostRecentStrategy p = new MostRecentStrategy();
		ITask t1 = new MockTask();
		ITask t2 = new MockTask();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t2); 
		l.addFirst(t1);
		assertSame("Select two tasks", t1, p.selectTask(l));
		assertEquals("Select two tasks", 1, l.size());
		assertSame("Select two tasks", t2, p.selectTask(l));
		assertEquals("Select two tasks", 0, l.size());
	}

	@Test public void testMostRecentNull() {
		MostRecentStrategy p = new MostRecentStrategy();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(new MockTask()); 
		p.selectTask(l);
		assertSame("Returns null when no more tasks", null, p.selectTask(l));
	}
	
}
