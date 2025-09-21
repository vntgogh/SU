package pobj.micros.scheduler;

import pobj.micros.errors.OSError;

public interface ITask {
	public void exec(IScheduler ctx) throws OSError;
}
