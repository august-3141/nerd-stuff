// I like the concept of it

import java.util.*;

public class babel_library {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        int charAmount;
        String charList = "abcdefghijklmnopqrstuvwxyz.";

        System.out.println("*** Library of Babel Text Generator ***");

        System.out.print("Input the amount of characters you would like to print: ");
        charAmount = scan.nextInt();

        System.out.println("----------------------------------------------");

        for (int charCurrent = 1; charCurrent <= charAmount; charCurrent++) {

            System.out.print(charList.charAt(rand.nextInt(27)));

        }

        scan.close();

    }

}