//Moktadir Shourav GM Capstone Big Data Analytics Project
//School: Wayne State University	StID: fa9444
//Contact: moktadir@live.com

import java.*;
import java.util.*;
import java.lang.Object.*;

class linkedListNode
{
	int ID;
	String name;
	double inWeight;
	double outWeight;
	int depth;
	int position;
	ArrayList<linkedListNode> outputs = new ArrayList<linkedListNode>();//connections to deeper nodes
}

public static int makeStruct(ArrayList<String[]> nodes, ArrayList<String[]> connections, ArrayList<linkedListNode> graph){
	int to, from; 
	double weight;
	HashMap<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
	for (int i = 0; i < connections.size()-1; i++){
		to = new Integer(connections.get(i)[0]).intValue();
		from = new Integer(connections.get(i)[1]).intValue();
		weight = new Double(connections.get(i)[2]).doubleValue();
		graph.get(to).inWeight = weight;
		graph.get(from).outWeight = weight;
		if !(map.containsKey(from){
			map.put(from,[0,to]);
		}
		else if (map.containsKey(from)){
			map.get(from)[0] += 1;
			map.get(from).add(to);
		}
	}
	return 0;
}

public static void main(String[] args)throws Exception{
	ArrayList<String[]> nodes = new ArrayList<String[]>();
	ArrayList<String[]> connections = new ArrayList<String[]>();
	ArrayList<linkedListNode> graph = new ArrayList<linkedListNode>();
	nodes.add(new String[]{"0", "fracking","-1"});
	nodes.add(new String[]{"1", "tarsands","-1"});
	nodes.add(new String[]{"2", "opec","-1"});
	connections.add("2", "0", "0.3");
	connections.add("1", "0", "0.1");
	makeStruct(nodes, connections, graph);
}