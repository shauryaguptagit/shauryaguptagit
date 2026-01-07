/*Function to count number of characters
 * to make s1 and s2 equal
 * s1 : first string
 * s2 : second string
 */
public class AlmostEqual {

    static int coutChars(String s1, String s2) {

        // Your code here
        int[] count = new int[26];
        
        for (int i = 0; i < s1.length(); i++){
            count[s1.charAt(i) - 'a']++;
        }
        
        for (int i = 0; i < s2.length(); i++){
            count[s2.charAt(i) - 'a']--;
        }
        
        int deletions = 0;
        
        for(int val : count){
            deletions += Math.abs(val);
        }
        
        return deletions;
    }

    public static void main(String[] args) {
        String s1 = "abcde";
        String s2 = "bcdfg";
        System.out.println("Number of characters to delete to make strings equal: " + coutChars(s1, s2));
    }
}