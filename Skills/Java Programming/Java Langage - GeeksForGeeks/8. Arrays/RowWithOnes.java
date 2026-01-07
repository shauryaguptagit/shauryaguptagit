public class RowWithOnes {
    public static void main(String[] args) {
        int[][] sampleMatrix = {
            {0, 0, 1, 1},
            {1, 1, 1, 1},
            {0, 0, 0, 0},
            {1, 0, 1, 1}
        };
        int rowIndex = minRow(sampleMatrix);
        System.out.println("Row with minimum number of 1s is: " + rowIndex);
    }


    
    static int minRow(int mat[][]) {
        // code here
        int rows = mat.length;
        int cols = mat[0].length;
        
        int minCount = Integer.MAX_VALUE;
        int resultIndex = 1;
        
        for(int i = 0; i < rows; i++){
            int currentCount = 0;
            
            for(int j =0; j<cols; j++){
                if(mat[i][j] == 1){
                    currentCount++;
                }
            }
            
            if(currentCount < minCount){
                minCount = currentCount;
                resultIndex = i + 1 ;
            }
        }
        return resultIndex;
    }
}
