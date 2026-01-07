public class PanagramCheck {

    public static boolean isPanagram(String str) {
        // Your code here
        if (str.length() < 26) return false;
        boolean[] visited = new boolean[26];
        int count = 0;
        
        for(int i = 0; i< str.length(); i++){
            char ch = str.charAt(i);
            int index = -1;
            
            if( ch >= 'A' && ch <= 'Z' ){
                index = ch - 'A';
            }
            else if( ch >= 'a' && ch <= 'z' ){
                index = ch - 'a';
            }
            if (index != -1 && !visited[index]){
                visited[index] = true;
                count++;
            }
            if(count == 26) return true;
        }
        return false;
    }
    public static void main(String[] args) {
        String str = "The quick brown fox jumps over a lazy dog";
        if(isPanagram(str)){
            System.out.println("The string is a panagram.");
        } else {
            System.out.println("The string is not a panagram.");
        }
    }
}