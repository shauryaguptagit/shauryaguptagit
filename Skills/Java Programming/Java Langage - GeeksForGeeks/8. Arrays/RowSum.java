public class RowSum {
    public static void main(String[] args) {
        int[][] sampleArray = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        //System.out.print("Array elements: ");
        int[] answer = rowSum(sampleArray);
        for(int i = 0; i < answer.length; i++) {
            System.out.print(answer[i] + " ");
        }
    }

    
    public static int[] rowSum(int mat[][]) {
        // Code here
        int[] ans = new int[mat.length];
        for(int i = 0; i<mat.length; i++) {
            int sum = 0;
            for(int j =0; j<mat[i].length; j++) {
                sum += mat[i][j];
            }
            ans[i] = sum;
        }
        return ans;
    }
}
