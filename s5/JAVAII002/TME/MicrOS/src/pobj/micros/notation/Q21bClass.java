package pobj.micros.notation;

import static org.junit.Assert.*;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.List;

import org.junit.Test;
import pobj.micros.scheduler.IStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.ITask;
import pobj.micros.scheduler.Scheduler;

public class Q21bClass {

	class MockStrategy implements IStrategy {
		@Override public ITask selectTask(List<ITask> tasks) { return null; }
	}
	
	@Test public void testInstance() {
		Scheduler n = new Scheduler(new MockStrategy());
		assertTrue("Must implement IScheduler", n instanceof IScheduler);
		assertSame("Must extend Object", Object.class, Scheduler.class.getSuperclass());
	}

	@Test public void testPrivate() {
		for (Field f : Scheduler.class.getDeclaredFields()) {
			assertTrue("Attributes must be private", Modifier.isPrivate(f.getModifiers()));
		}	
	}

}
