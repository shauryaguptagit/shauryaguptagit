public class ArrayTravRev {
    public static void main(String[] args) {
        int[] sampleArray = {1,2,3,4,5};
        System.out.print("Array elements: ");
        arrayTraversalReversal(sampleArray);
    }

    
    public static void arrayTraversalReversal(int[] arr) {
        // Code here
        for(int i= (arr.length - 1); i>=0 ;i--){
            System.out.print(arr[i] + " ");
        }
    }
}
