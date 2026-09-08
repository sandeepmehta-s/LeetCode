class Solution {
    public static void nQueenUtility(int j, int n, boolean[] row, boolean[] d1, boolean[] d2, List<Integer>board, List<List<String>>res){
        if(j>=n)
        {
            List<String> sol=new ArrayList<>();
            for(int i=0; i<n; i++)
            {
                StringBuilder sb=new StringBuilder();
                for(int col=1; col<=n; col++)
                {
                    if(board.get(col-1)==i+1) 
                    {
                        sb.append('Q');
                    } 
                    else 
                    {
                        sb.append('.');
                    }
                }
                sol.add(sb.toString());
            }
            res.add(sol);
            return;
        }
        for(int i=1; i<=n; i++)
        {
            if(!row[i] && !d1[i+j] && !d2[i-j+n])
            {
                row[i]=d1[i+j]=d2[i-j+n]=true;
                board.add(i);
                nQueenUtility(j+1, n, row, d1, d2, board, res);
                board.remove(board.size()-1);
                row[i]=d1[i+j]=d2[i-j+n]=false;
            }
        }
    }

    public List<List<String>> solveNQueens(int n) {
        List<List<String>>res=new ArrayList<>();
        List<Integer> board=new ArrayList<>();
        boolean[] row=new boolean[n+1];
        boolean[] d1=new boolean[2*n+1];
        boolean[] d2=new boolean[2*n+1];
        nQueenUtility(0, n, row, d1, d2, board, res);
        return res;
    }
}