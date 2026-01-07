public class ArrayTrav {
    public static void main(String[] args) {
        int[] sampleArray = {1,2,3,4,5};
        System.out.print("Array elements: ");
        arrayTraversal(sampleArray);
    }

    
    public static void arrayTraversal(int[] arr) {
        // Code here
        for(int i=0; i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }
    }
}
