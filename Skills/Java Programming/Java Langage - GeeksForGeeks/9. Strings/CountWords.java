public class CountWords {
    // Complete the function
    // str: input string
    public static int countWords(String str) {
        // find and return the number of words
        // present in the string
        if(str== null || str.isEmpty()){
            return 0;
        }
        String[] words = str.trim().split("\\s+");
        return words.length;
    }
    public static void main(String[] args) {
        String str = "Geeks For Geeks";
        System.out.println("Number of words in the string: " + countWords(str));
    }
}