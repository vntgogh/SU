package pobj.micros.fs;

import java.util.List;

public interface IDirectoryNode extends INode {
	public boolean addChild(INode node);
	public INode getChild(String name);
	public List<String> getChildren();
}
