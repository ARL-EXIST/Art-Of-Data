//package com.mkyong.io.csv.opencsv;

import java.io.File;
import java.io.FileNotFoundException;

import java.io.*;

import java.io.FileReader;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
//import com.opencsv.*;

//import com.opencsv.CSVReader;
//import com.opencsv.exceptions.CsvException;

import java.util.Scanner;

public class PokemonCorrector {
    public static void main(String[] args) throws IOException {
        File table = new File("../datasets/PokedexSourceCode.tsv");
        
        for(String[] array : tsvr(table)){
            System.out.println(Arrays.toString(array));
        }

        // need to split at commas

    }

    public static ArrayList<String[]> tsvr(File test2) {
        ArrayList<String[]> Data = new ArrayList<>(); //initializing a new ArrayList out of String[]'s
        try (BufferedReader TSVReader = new BufferedReader(new FileReader(test2))) {
            String line = null;
            while ((line = TSVReader.readLine()) != null) {
                String[] lineItems = line.split("\t"); //splitting the line and adding its items in String[]
                Data.add(lineItems); //adding the splitted line array to the ArrayList
            }
        } catch (Exception e) {
            System.out.println("Something went wrong");
            //System.out.println(e);
        }
        return Data;
    }
}