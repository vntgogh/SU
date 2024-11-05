package pobj.micros.fs;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DirectoryNode extends Node implements IDirectoryNode {
	private Map<String,INode> dir;
	
	public DirectoryNode(String name) {
		super(name);
		this.dir=new HashMap<String,INode>();	
	}
	
	@Override
	public String getName() {
		return super.getName();
	}

	@Override
	public boolean addChild(INode node) {
		if(dir.containsKey(node.getName())) {
			return false;
		}
		
		dir.put(node.getName(),node);
		return true;
	}

	@Override
	public INode getChild(String name) {
		if (dir.containsKey(name)) {
			return dir.get(name);
		}
		return null;
	}

	@Override
	public List<String> getChildren() {
		List<String> lname = new ArrayList<String>();
		for (Map.Entry<String,INode> e : dir.entrySet()) {
			lname.add(e.getKey());
		}
		return lname;
	}
	
	public INode copy() {
		DirectoryNode d = new DirectoryNode(this.getName());
		for (Map.Entry<String,INode> e : dir.entrySet()) {
			d.addChild(e.getValue());
		}		
		return d;
	}

}
