class MyHashMap {
    int[] map;
    int size = 1;
    public MyHashMap() {
        map = new int[size];
        Arrays.fill(map, -1);
    }
    
    public void put(int key, int value) {
        if (key >= size) {
            int[] newMap = new int[key + size + 1];
            Arrays.fill(newMap, -1);
            System.arraycopy(map, 0, newMap, 0, size);
            size = newMap.length;
            map = newMap;
        }
        map[key] = value;
    }
    
    public int get(int key) {
        if (key >= size) return -1;
        return map[key];
    }
    
    public void remove(int key) {
        if (key >= size) return;
        map[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
