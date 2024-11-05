package pobj.micros.notation;

import static org.junit.Assert.*;

import java.util.List;

import org.junit.Test;
import pobj.micros.errors.OSError;
import pobj.micros.scheduler.IStrategy;
import pobj.micros.scheduler.FIFOStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.scheduler.MostRecentStrategy;
import pobj.micros.scheduler.Scheduler;

public class Q21bMethods {

	class MyTask implements ITask {
		int called;
		public void exec(IScheduler sch) { called++; }
	}
	
	@Test public void testPostExec() throws OSError {
		Scheduler s = new Scheduler(new FIFOStrategy());
		MyTask t = new MyTask();
		s.postTask(t);
		assertEquals("postTask does not execute task", 0, t.called);
		s.execNext();
		assertEquals("nextTask executes a task", 1, t.called);
	}

	@Test public void testPostReturn() throws OSError {
		Scheduler s = new Scheduler(new FIFOStrategy());
		MyTask t = new MyTask();
		s.postTask(t);
		assertTrue("execNext returns true when a task is executed", s.execNext());
		assertFalse("execNext returns false when no task is executed", s.execNext());
	}

	@Test public void testPostTwiceExec() throws OSError {
		Scheduler s = new Scheduler(new FIFOStrategy());
		MyTask t = new MyTask();
		s.postTask(t);
		s.postTask(t);
		s.execNext();
		s.execNext();
		assertEquals("nextTask executes a task", 2, t.called);
	}

	@Test public void testPostTwoExec() throws OSError {
		Scheduler s = new Scheduler(new FIFOStrategy());
		MyTask t1 = new MyTask();
		MyTask t2 = new MyTask();
		s.postTask(t1);
		s.postTask(t2);
		s.execNext();
		assertEquals("nextTask executes tasks in order", 1, t1.called);
		assertEquals("nextTask executes tasks in order", 0, t2.called);
		s.execNext();
		assertEquals("nextTask executes tasks in order", 1, t1.called);
		assertEquals("nextTask executes tasks in order", 1, t2.called);
	}

	@Test public void testSetStrategy() throws OSError {
		Scheduler s = new Scheduler(new FIFOStrategy());
		MyTask t1 = new MyTask();
		MyTask t2 = new MyTask();
		s.postTask(t1);
		s.postTask(t2);
		s.setStrategy(new MostRecentStrategy());
		s.execNext();
		assertEquals("nextTask executes tasks in order", 0, t1.called);
		assertEquals("nextTask executes tasks in order", 1, t2.called);
		s.execNext();
		assertEquals("nextTask executes tasks in order", 1, t1.called);
		assertEquals("nextTask executes tasks in order", 1, t2.called);
	}

	
	class MyTask2  implements ITask {
		Scheduler sch;
		int called = 0;
		public MyTask2(Scheduler sch) { this.sch = sch; }
		public void exec(IScheduler ctx) throws OSError {
			called = 1;
			assertSame("argument of exec", ctx, sch);
		}
	}
	
	@Test public void testExecArg() throws OSError {
		Scheduler s = new Scheduler(new FIFOStrategy());
		MyTask2 t = new MyTask2(s);
		s.postTask(t);
		s.execNext();
		assertEquals("nextTask executes a task", 1, t.called);
	}
	
	class MyStrategy implements IStrategy {
		int called;
		public ITask selectTask(List<ITask> tasks) { 
			called++; 
			return tasks==null || tasks.size() == 0 ? null : tasks.remove(0); 
			}
	}
	
	@Test public void testDelegateStrategy() throws OSError {
		MyStrategy strat = new MyStrategy();
		Scheduler s = new Scheduler(strat);
		MyTask t = new MyTask();
		s.postTask(t);
		s.execNext();
		assertEquals("execNext delegates to strategy", 1, strat.called);
	}
}
