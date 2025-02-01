package pobj.micros.notation;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.scheduler.FIFOStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.scheduler.Scheduler;
import pobj.micros.scheduler.TaskRunner;

public class Q21c {	
	
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    
    private String getOut() {
            System.out.flush();
            return out.toString().replaceAll("\\s+","");
    }

    class MyTask implements ITask {
		int called;
		public void exec(IScheduler sch) throws OSError { called++; }
	}
	
	@Test public void testOne() {
		Scheduler sch = new Scheduler(new FIFOStrategy());
		MyTask t = new MyTask();
		sch.postTask(t);
		TaskRunner.run(sch);
		assertEquals("task is executed", 1, t.called);
	}

	@Test public void testTwice() {
		Scheduler sch = new Scheduler(new FIFOStrategy());
		MyTask t = new MyTask();
		sch.postTask(t);
		sch.postTask(t);
		TaskRunner.run(sch);
		assertEquals("task is executed", 2, t.called);
	}
	
	class MyTask2 implements ITask {
		int called;
		public void exec(IScheduler sch) throws OSError { called++; if (called < 10) sch.postTask(this); }
	}
	
	@Test public void testPostRec() {
		Scheduler sch = new Scheduler(new FIFOStrategy());
		MyTask2 t = new MyTask2();
		sch.postTask(t);
		TaskRunner.run(sch);
		assertEquals("task is executed", 10, t.called);
	}

	class MyTaskError implements ITask {
		public void exec(IScheduler sch) throws OSError { throw new OSError("error"); }
	}
	
	@Test public void testError() {
		Scheduler sch = new Scheduler(new FIFOStrategy());
		MyTaskError t = new MyTaskError();
		sch.postTask(t);
		TaskRunner.run(sch);	
	}

	@Test public void testErrorMessage() {
        System.setOut(new PrintStream(out));
		Scheduler sch = new Scheduler(new FIFOStrategy());
		MyTaskError t = new MyTaskError();
		sch.postTask(t);
		TaskRunner.run(sch);	
		assertEquals("Error message", "error", getOut());
	}

	@Test public void testErrorContinue() {
		Scheduler sch = new Scheduler(new FIFOStrategy());
		MyTaskError t1 = new MyTaskError();
		MyTask t2 = new MyTask();
		sch.postTask(t2);
		sch.postTask(t1);
		sch.postTask(t2);
		TaskRunner.run(sch);	
		assertEquals("task is executed after an error", 2, t2.called);
	}

}
