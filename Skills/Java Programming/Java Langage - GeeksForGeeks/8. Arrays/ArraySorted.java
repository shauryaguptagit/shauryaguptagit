public class ArraySorted {
    public static void main(String[] args) {
        int[] sampleArray = {1,2,3,4,5};
        System.out.print("Array elements: ");
        boolean result = isSorted(sampleArray);
        System.out.println("Is array sorted? " + result);
    }

    
    public static boolean isSorted(int[] arr) {
        // code here
        for(int i=0; i<(arr.length-1); i++){
            if(arr[i+1] < arr[i]){
                return false;
            }
        }
        return true;
    }
}
