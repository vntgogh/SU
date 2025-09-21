package pobj.micros.test;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.Before;
import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.scheduler.ExampleTask;
import pobj.micros.scheduler.FIFOStrategy;
import pobj.micros.scheduler.IScheduler;
import pobj.micros.scheduler.Scheduler;
import pobj.micros.scheduler.TaskRunner;

public class ExampleTaskTest {

    ByteArrayOutputStream out = new ByteArrayOutputStream();

    @Before public void atBefore() {
            System.setOut(new PrintStream(out));
    }
    
    private String getOut() {
    	System.out.flush();
    	return out.toString().replaceAll("\\s+","");
    }

    @Test public void test() throws OSError {
    	IScheduler sch = new Scheduler(new FIFOStrategy());
 		sch.postTask(new ExampleTask(2));
 		TaskRunner.run(sch);
 		assertEquals("2110000", getOut());
 	}
 	
}
