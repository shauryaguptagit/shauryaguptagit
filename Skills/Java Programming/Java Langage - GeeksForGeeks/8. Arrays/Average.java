public class Average {
    public static void main(String[] args) {
        int[] sampleArray = {1,2,3,4,5};
        //System.out.print("Array elements: ");
        double averageResult = posAverage(sampleArray);
        System.out.println("Positive Average: " + averageResult);
    }

    
    public static double posAverage(int[] arr) {
        // Code here
        int count = 0;
        double sum=0;        
        
        for(int i = 0; i<arr.length; i++){
            if(arr[i]>=0){
                sum += arr[i];
                count++;
            }
        }
        if(count==0){
            return 0.0;
        }
        
        double average = sum/count;
        return average;
    }
}
