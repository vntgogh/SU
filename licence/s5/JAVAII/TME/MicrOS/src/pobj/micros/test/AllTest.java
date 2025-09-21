package pobj.micros.test;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
	NodeTest.class, FileNodeTest.class, DirectoryNodeTest.class,
	FileStreamTest.class,
	CopyNodeTest.class,
	NodeUtilsTest.class, FileSystemTest.class,
	StrategyTest.class, SchedulerTest.class, TaskRunnerTest.class,
	ExampleTaskTest.class,
	ServiceTest.class,
})
public class AllTest {
}
