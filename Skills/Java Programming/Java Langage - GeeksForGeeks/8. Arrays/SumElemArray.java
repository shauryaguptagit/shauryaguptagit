public class SumElemArray {
    public static void main(String[] args) {
        int[] sampleArray = {1,2,3,4,5};
        //System.out.print("Array elements: ");
        int sumOfArray = arraySum(sampleArray);
        System.out.println("Sum of Array elements: " + sumOfArray);
    }

    
    public static int arraySum(int[] arr) {
        // code here
        int count = 0;
        for(int i =0; i<arr.length; i++){
            count+=arr[i];
        }
        return count;
    }
}
