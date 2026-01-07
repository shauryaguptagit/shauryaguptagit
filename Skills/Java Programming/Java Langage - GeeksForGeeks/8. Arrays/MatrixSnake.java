import java.util.ArrayList;

public class MatrixSnake {
    public static void main(String[] args) {
        int[][] sampleArray = {{1,2,3},{4,5,6},{7,8,9}};
        ArrayList<Integer> result = snakePattern(sampleArray);
        for(int num : result) {
            System.out.print(num + " ");
        }
    }
    
    static ArrayList<Integer> snakePattern(int matrix[][]) {
        // code here
        int n = matrix.length;
        
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int i =0; i<n; i++){
            if(i%2==0){
                for(int j=0; j<n;j++){
                    result.add(matrix[i][j]);
                }
            } else{
                for(int j = n - 1; j>=0; j--){
                    result.add(matrix[i][j]);
                }
            }
        }
        return result;
        
    }
}
