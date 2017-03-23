//Moktadir Shourav GM Capstone Big Data Analytics Project
//School: Wayne State University	StID: fa9444
//Contact: moktadir@live.com

import java.io.*;
import java.util.*;
import static PoSTagger;

public class test{
	public static String[] test(String inFile)throws Exception{
		File file = new File(inFile);
		RandomAccessFile in = new RandomAccessFile(file,"r");
		int lineC;
		String tagged[] = new String[10000];
		for (lineC = 0; lineC < 10000; lineC++){
			tagged[lineC] = PoSTagger.PoSTagger(in.readline());
		}
		return tagged;
	}
	
	public static void main(String args[])throws Exception{		//main
		test(args[0]);
//		System.out.println(args[0]);
	}
}