public class ColumnSum {
    public static void main(String[] args) {
        int[][] sampleArray = {{1,2,3},{4,5,6},{7,8,9}};
        int[] answer = colSum(sampleArray);
        for(int i = 0; i < answer.length; i++) {
            System.out.print(answer[i] + " ");
        }
    }
    
    public static int[] colSum(int mat[][]) {
        int ans[] = new int[mat[0].length];
        int n = mat.length;
        int m = mat[0].length;
        for (int i = 0; i < m; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += mat[j][i];
            }
            ans[i] = sum;
        }
        return ans;
    }
}
