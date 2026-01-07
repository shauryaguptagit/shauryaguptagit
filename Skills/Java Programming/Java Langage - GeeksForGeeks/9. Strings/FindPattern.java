public class FindPattern {
    public static int findPattern(String s, String p) {
        // code here
        int n = s.length();
        int m = p.length();
        
        if(m>n) return -1;
        
        for(int i = 0; i <= n-m; i++){
            int j;
            for(j = 0; j < m; j++){
                if(s.charAt(i+j) != p.charAt(j)){
                    break;
                }
            }
            
            if(j == m){
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        String s = "GeeksForGeeks";
        String p = "For";
        int result = findPattern(s, p);
        if(result != -1){
            System.out.println("Pattern found at index: " + result);
        } else {
            System.out.println("Pattern not found.");
        }
    }
}