package pobj.micros.test;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Test;

import pobj.micros.scheduler.MostRecentStrategy;
import pobj.micros.scheduler.IStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.scheduler.FIFOStrategy;

public class StrategyTest {
	
	class Task implements ITask {
		public void exec(IScheduler sched) { }
	}

	@Test public void testFIFO() {
		IStrategy p = new FIFOStrategy();
		ITask t1 = new Task();
		ITask t2 = new Task();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t1); 
		l.addFirst(t2);
		assertEquals(t1, p.selectTask(l));
		assertEquals(t2, p.selectTask(l));
		assertEquals(null, p.selectTask(l));
	}

	@Test public void testMostRecent() {
		IStrategy p = new MostRecentStrategy();
		ITask t1 = new Task();
		ITask t2 = new Task();
		LinkedList<ITask> l = new LinkedList<>();
		l.addFirst(t1); 
		l.addFirst(t2);
		assertEquals(t2, p.selectTask(l));
		assertEquals(t1, p.selectTask(l));
		assertEquals(null, p.selectTask(l));
	}

}
