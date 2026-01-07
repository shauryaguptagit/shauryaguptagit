public class PatternMatcher {
    static int follPatt(String s) {
        // Your code here
        int i = 0;
        int n = s.length();
        
        while( i < n){
            int countX = 0;
            
            while (i < n && s.charAt(i) == 'x'){
                countX++;
                i++;
            }
            
            if(countX == 0){
                return 0;
            }
            
            int countY = 0;
            while(countY < countX){
                if(i >= n || s.charAt(i) != 'y'){
                    return 0;
                }
                i++;
                countY++;
            }
        }
        
        return 1;
    }
    public static void main(String[] args) {
        String str = "xxyyxyxyxx";
        System.out.println("Does the string follow the pattern? " + follPatt(str));
    }
}