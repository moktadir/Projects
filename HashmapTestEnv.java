//Moktadir Shourav GM Capstone Big Data Analytics Project
//School: Wayne State University	StID: fa9444
//Contact: moktadir@live.com

package test;
import java.util.*;

public class Test {

	public class linkedListNode {
		int ID;
		String name;
		double inWeight;
		double outWeight;
		int depth;
		int position;
		ArrayList<linkedListNode> outputs = new ArrayList<linkedListNode>();//connections to deeper nodes
	}

	public static void makeMap(ArrayList<String[]> connections, HashMap<Integer, Integer[]> map){
		int to, from;
		//ArrayList<Integer[]> map = new ArrayList<Integer[]>();
		//System.out.println("ConnectionSize: " + connections.size());
		
		
		for (int i = 0; i < connections.size(); i++){
			to = new Integer(connections.get(i)[0]).intValue();
			from = new Integer(connections.get(i)[1]).intValue();
			//System.out.println("\ni: " + i + "\nto: " + to + "  from: " + from + "  weight: " + weight);
			
			if (!map.containsKey(from)){
				Integer[] initial = new Integer[connections.size()];
				for (int j = 0; j < connections.size(); j++){
					initial[j] = 0;
				}
				initial[0] = 1;
				initial[1] = to; //lol
				map.put(from, initial);
				//System.out.println("Wot. From: " + from + " i = " + i);
			}
			
			else if (map.containsKey(from)){
				map.get(from)[0] += 1;
				//System.out.println("\n+1 i = \n" + i);
				map.get(from)[map.get(from)[0]] = to;
			}
			
			/*System.out.println("\nnode: " + from);
			for (int j = 0; j < map.get(from)[0] + 1; j++){
				System.out.println("Ind: " + j + " Val: " + map.get(from)[j]);
			}*/
		}
	}
	
	public static void hashConnections(ArrayList<String[]> connections, HashMap<Integer, Integer[]> connectionList){
		
	}
	
	public static void makeNetwork(ArrayList<String[]> nodes, ArrayList<String[]> connections, HashMap<Integer, Integer[]> map,
			ArrayList<linkedListNode> graph){
		double weight;
		for (int i = 0; i < map.size(); i++){
			linkedListNode node = new linkedListNode();
			node.ID = i;
			node.name = nodes.get(i)[1];
			node.inWeight = 
			
		}
	}

	public static void main(String[] args)throws Exception{
		ArrayList<String[]> nodes = new ArrayList<String[]>();
		ArrayList<String[]> connections = new ArrayList<String[]>();
		HashMap<Integer, Integer[]> connectionList = new HashMap<Integer, Integer[]>();

		HashMap<Integer, Integer[]> map = new HashMap<Integer, Integer[]>();
		ArrayList<linkedListNode> graph = new ArrayList<linkedListNode>();
		
		nodes.add(new String[]{"0", "fracking","-1"});
		nodes.add(new String[]{"1", "tarsands","-1"});
		nodes.add(new String[]{"2", "opec","-1"});
		connections.add(new String[]{"2", "0", "0.3"});
		connections.add(new String[]{"1", "0", "0.1"});
		connections.add(new String[]{"0", "1", "0.5"});
		
		hashConnections(connections, connectionList);
		makeMap(connections, map);
		makeNetwork(nodes, connections, map, graph);
		/*for (int i = 0; i < map.size(); i++){
			System.out.println("Node: " + i);
			for (int j = 0; j < map.get(i)[0] + 1; j++){
				System.out.println("Ind: " + j + " Val: " + map.get(i)[j]);
			}
		}*/
	}
}