class Solution {

int findMinIndex(int dist[],HashSet<Integer> set){
    
    int min=2147483647,minIndex=-1;
    
    
    for(int i=0;i<dist.length;i++){
        if(!set.contains(i)){
            if(min>dist[i]){
                min=dist[i];
                minIndex=i;
            }
        }
    }
    
    
    return minIndex;
    
}
public int networkDelayTime(int[][] times, int n, int k) {
    
    HashSet<Integer> set=new HashSet<>();
    
    int dist[]=new int[n];
    
    Arrays.fill(dist,2147483647);
    
    dist[k-1]=0;
    
    
    int x=0;
    
    
    while(x<n){
        
        
        int y=findMinIndex(dist,set);
        
        if(y==-1)
            return -1;
        
        set.add(y);
        
        
        for(int e[]: times){
            if(e[0]==(y+1)){
                dist[e[1]-1]=Math.min(dist[e[1]-1],dist[y]+e[2]);
            }
        }
        
        x++;
        
    }
    
    int max=0;
    
    for(int r : dist){
        max=Math.max(max,r);
    }
    
    return max==2147483647?-1:max;
}
}
