package pobj.micros.notation;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
	Q11aClass.class, Q11aMethods.class,
	Q11bClass.class, Q11bMethods.class,
	Q11cClass.class, Q11cMethods.class,
	Q12Class.class, Q12Methods.class, Q12Delegate.class,
	Q13Node.class, Q13FileNode.class, Q13DirectoryNode.class,
	Q14a.class, Q14b.class,
	Q21aFIFO.class, Q21aMostRecent.class,
	Q21bClass.class,  Q21bMethods.class,
	Q21c.class,
	Q22Main.class, Q22Task.class,
	Q23.class
})
public class AllTest {
}
