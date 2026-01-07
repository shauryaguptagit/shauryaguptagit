import java.util.*;
public class ArrayDec {
    public static void main(String[] args) {
        int[] sampleArray = {1,2,3,4,5};
        System.out.print("Decremented Array elements: ");
        int[] finalArray = decrementArrayElements(sampleArray);
        System.out.println(Arrays.toString(finalArray));
    }

    
    public static int[] decrementArrayElements(int[] arr) {
        // Code here
        for(int i =0; i<arr.length; i++){
            arr[i]=arr[i]-1;
        }
        return arr;
    }
}
