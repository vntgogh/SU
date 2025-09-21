package pobj.micros.fs;

public class Node implements INode {
	private String name;
	
	public Node(String name){
		this.name= name;	}

	@Override
	public String getName() {
		return name;
	}

	@Override
	public INode copy() {
		return new Node(name);
	}

}
