class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        
        int[] rel = new int[s.length()];
        char[] res= s.toCharArray();
        
        for(int i=0;i<rel.length;i++){
            rel[i]=i;
        }
        Union union = new Union();
        for(List<Integer> pair:pairs){
            union.union(rel,pair.get(0),pair.get(1));
        }
        
        Map<Integer,List<Integer>> map = new HashMap<>();
        for(int i=0;i<rel.length;i++){
            int parent = union.find(rel,i);
            List<Integer> l = map.getOrDefault(parent,new ArrayList<>());
            l.add(i);
            map.put(parent,l);
        }
        for(int key:map.keySet()){
            if(key>-1){
            List<Integer> index = map.get(key);
            List<Character> characters = new ArrayList<>();
            
            for(int k:index){
                characters.add(res[k]);
            }
            Collections.sort(characters);
            
            for(int i=0;i<index.size();i++){
                res[index.get(i)] = characters.get(i);
            }
                      }
        }
        return new String(res);
    }
    
    
    class Union{
        
        public void union(int[] rel,int a,int b){
            int roota = find(rel,a);
            int rootb = find(rel,b);
            if(roota!=rootb){
                rel[rootb] = roota;
            }
        }
        
        public int find(int[] rel,int a){
            while(rel[a]!=a){
                rel[a] = rel[rel[a]];
                a = rel[a];
            }
            return a;
        }
    }
}
