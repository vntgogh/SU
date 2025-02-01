package pobj.micros.test;

import static org.junit.Assert.*;

import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.scheduler.FIFOStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.scheduler.Scheduler;
import pobj.micros.scheduler.TaskRunner;

public class TaskRunnerTest {
	
	private int counter = 0;
	
	class Task implements ITask {
		public void exec(IScheduler ctx) throws OSError { counter++; }
	}

	@Test public void test() {
		IScheduler sch = new Scheduler(new FIFOStrategy());
		Task t = new Task();
		sch.postTask(t);
		sch.postTask(t);
		sch.postTask(t);
		assertEquals(0, counter);
		TaskRunner.run(sch);
		assertEquals(3, counter);
	}
	
}
