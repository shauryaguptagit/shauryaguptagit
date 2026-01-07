public class ForEach {
    public static void main(String[] args) {
        String[] sampleArray = {"Geeks", "for", "Geeks"};
        System.out.println("Array elements: ");
        printArray(sampleArray);
    }

    public static void printArray(String[] arr) {
        // Code here
        for(String i: arr) {
            System.out.println(i);
        }
    }
}
