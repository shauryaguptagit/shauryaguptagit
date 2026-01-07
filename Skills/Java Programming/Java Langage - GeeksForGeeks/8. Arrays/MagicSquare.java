public class MagicSquare {
    public static void main(String[] args) {
        int[][] sampleMatrix = {
            {0, 0, 1, 1},
            {1, 1, 1, 1},
            {0, 0, 0, 0},
            {1, 0, 1, 1}
        };
        String result = magicSquare(sampleMatrix);
        System.out.println(result);
    }

    
    public static String magicSquare(int mat[][]) {
        // Code here
        int n = mat.length;
        
        boolean[] visited = new boolean[n * n + 1];
        
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                int val = mat[i][j];
                if(val<1 || val>n*n || visited[val]){
                    return "Not a Magic Square";
                }
                visited[val] = true;
            }
        }
        
        int targetSum = 0;
        for (int j = 0; j<n; j++){
            targetSum += mat[0][j];
        }
        
        for(int i =0; i<n; i++){
            int rowSum = 0;
            int colSum = 0;
            
            for(int j =0; j <n; j++){
                rowSum += mat[i][j];
                colSum += mat[j][i];
            }
            if(rowSum != targetSum || colSum != targetSum){
                return "Not a Magic Square";
            }
        }
        
        int diag1Sum =0;
        int diag2Sum =0;
        
        for(int i =0; i<n; i++){
            diag1Sum += mat[i][i];
            diag2Sum += mat[i][n - 1 - i];
        }
        if(diag1Sum != targetSum || diag2Sum != targetSum){
            return "Not a Magic Square";
        }
        return "Magic Square";
    }
}
