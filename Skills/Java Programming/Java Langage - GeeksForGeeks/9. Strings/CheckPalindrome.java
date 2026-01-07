public class CheckPalindrome {
    public static boolean isPalindrome(String s) {
        // code here
        int left = 0;
        int right = s.length() - 1;
        
        while(left < right){
            char l = s.charAt(left);
            char r = s.charAt(right);
            
            if (Character.toLowerCase(l) != Character.toLowerCase(r)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    public static void main(String[] args) {
        String s = "Madam";
        if(isPalindrome(s)){
            System.out.println("The string is a palindrome.");
        } else {
            System.out.println("The string is not a palindrome.");  
        }
    }
}