// Back Track Algorithm

class Solution {
    private void print(int[]A, int i) {
        System.out.print("{");
        for (int j = 0; j < i; j++) {
            System.out.print(A[j] + ",");
        }
        System.out.print("}");        
    }

    void solve(int[]A) {
        final int N = A == null? 0: A.legnth;
        for (int i = 0; i <= N; i++) {
            print(A, i);
        }
    }

    void solve2(int[]A, int i) {
        final int N = A == null? 0: A.legnth;
        if (i > N) {
            return;
        }
        print(0, i);
        solve2(A, i+1);
    }

    public static void main(String[] args) {
        func();    
    }
}
