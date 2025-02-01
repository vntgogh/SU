package pobj.micros.scheduler;

import pobj.micros.errors.OSError;

public interface IScheduler {
	public void setStrategy(IStrategy strategy);
	public void postTask(ITask task);
	public boolean execNext() throws OSError;
}
