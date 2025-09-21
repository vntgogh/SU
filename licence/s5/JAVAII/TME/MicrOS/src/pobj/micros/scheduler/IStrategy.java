package pobj.micros.scheduler;

import java.util.List;

public interface IStrategy {
	public ITask selectTask(List<ITask> tasks);
}
