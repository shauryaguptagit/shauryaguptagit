public class ArrayLargest {
    public static void main(String[] args) {
        int[] sampleArray = {1,2,3,4,5};
        System.out.print("Array elements: ");
        int largestElement = largest(sampleArray);
        System.out.println("Largest element is: " + largestElement);
    }

    
    public static int largest(int[] arr) {
        // code here
        int largest =0;
        for(int i=0; i<arr.length; i++){
            if(arr[i]>largest){
                largest = arr[i];
            }
        }
        return largest;
    }
}
