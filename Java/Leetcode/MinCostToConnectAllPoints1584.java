class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n=points.length;
        //the elements of int[] are distance and index
        PriorityQueue<int[]> pq=new PriorityQueue<>((arr1,arr2)->{
            return arr1[0]-arr2[0];
        });
		//record if a point has connected and calculated distance
        boolean[] visited=new boolean[n];
        //from first point, connect to the rest one by one
        int index=0;
        visited[0]=true;
        int res=0;
        for(int count=1;count<n;++count){
            int x=points[index][0];
            int y=points[index][1];
            for(int i=1;i<n;++i){
                if(!visited[i]){
                    int[] p=points[i];
                    //try to find the minimun distance to the connected points
                    //one point may appear many times and the peek one is with minimun distance
                    pq.add(new int[]{Math.abs(x-p[0])+Math.abs(y-p[1]),i});
                }
            }
            while(visited[pq.peek()[1]]){
                //this point has already visited, poll it
                pq.poll();
            } 
            //this is the point to connect to one of the visited points
            int[] connect=pq.poll();
            //its manhattan distance is connect[0]
            res+=connect[0];
            index=connect[1];
            visited[index]=true;
        }
        return res;
    }
}
