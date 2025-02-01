package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;
import pobj.micros.errors.OSError;
import pobj.micros.scheduler.FIFOStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.scheduler.Scheduler;

public class SchedulerTest {

	private int called = 0;
	
	class Task implements ITask {
		public void exec(IScheduler sch) { called = 1; }
	}

	@Test public void test() throws OSError  {
		IScheduler sch  = new Scheduler(new FIFOStrategy());
		sch.postTask(new Task());
		assertEquals(0, called);
		assertTrue(sch.execNext());
		assertEquals(1, called);
		assertFalse(sch.execNext());
	}

}
