import java.util.*;

 class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();
        while (test-- > 0) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            List<List<Integer>> adj = new ArrayList<>(n + 1);
            for (int i = 0; i <= n; i++) {
                adj.add(new ArrayList<>());
            }
            for (int i = 0; i < m; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
            int s = scanner.nextInt();
            int[] dist = new int[n + 1];
            Arrays.fill(dist, -1);
            boolean[] vis = new boolean[n + 1];
            Queue<Integer> q = new LinkedList<>();
            q.add(s);
            vis[s] = true;
            dist[s] = 0;
            while (!q.isEmpty()) {
                int x = q.poll();
                for (int t : adj.get(x)) {
                    if (!vis[t]) {
                        vis[t] = true;
                        q.add(t);
                        dist[t] = dist[x] + 6;
                    }
                }
            }
            for (int i = 1; i <= n; i++) {
                if (i != s) {
                    System.out.print(dist[i] + " ");
                }
            }
            System.out.println();
        }
        scanner.close();
    }
}

