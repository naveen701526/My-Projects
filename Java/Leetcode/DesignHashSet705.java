class MyHashSet {
    int bucket=15000;
LinkedList<Integer>[]list;
    private int has_function(int key){
        return key%bucket;
    }
    public MyHashSet() {
        list=new LinkedList[bucket];
        
    }
    
    public void add(int key) {
        int i=has_function(key);
        if(list[i]==null)list[i]=new LinkedList<>();
        if(list[i].indexOf(key)==-1){   //-1 means its not present
            list[i].add(key);
        }
    }
    
    public void remove(int key) {
         int i=has_function(key);
    if(list[i]==null)return;
        if(list[i].indexOf(key)!=-1){   //not -1 means its  present
            list[i].remove(list[i].indexOf(key));
        }
    }
    
    public boolean contains(int key) {
         int i=has_function(key);
    if(list[i]==null || list[i].indexOf(key)==-1)return false;  //no contains
       return true;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
