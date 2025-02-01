package pobj.micros.notation;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.Before;
import org.junit.Test;

import pobj.micros.errors.OSError;
import pobj.micros.scheduler.ExampleMain;

public class Q22Main {

    ByteArrayOutputStream out = new ByteArrayOutputStream();

    @Before public void atBefore() {
            System.setOut(new PrintStream(out));
    }
    
    private String getOut() {
            System.out.flush();
            return out.toString().replaceAll("\\s+","");
    }

    @Test public void test() throws OSError {
    	ExampleMain.main(new String[] {});
		assertEquals("322111100000000", getOut());
    }
}
