class UndergroundSystem {

    public class Pair {
        
        int id;
        String station;
        int t;
        
        public Pair(int id,String station,int t)
        {
            this.id = id;
            this.station = station;
            this.t = t;
        }
        
    }
    
    public class Node {
        int duration;
        int count;
        
        public Node(int duration)
        {
            this.duration = duration;
            count = 1;
        }
    }
    
    
    HashMap<Integer,Pair> hm ;
    HashMap<String,HashMap<String,Node>> map;
    public UndergroundSystem() {
        
        hm = new HashMap<>();
        map = new HashMap<>();
    }
    
    public void checkIn(int id, String stationName, int t) {
        
        hm.put(id,new Pair(id,stationName,t));
        
        if(!map.containsKey(stationName)) map.put(stationName, new HashMap<>());
        
    }
    
    public void checkOut(int id, String stationName, int t) {
        
        Pair p = hm.remove(id);
                
        HashMap<String,Node> h = map.get(p.station);
        
        if(!h.containsKey(stationName)) h.put(stationName, new Node(t-p.t));
        else
        {
            Node n = h.get(stationName);
            n.duration += t-p.t;
            n.count += 1;
            
        }
    }
    
    public double getAverageTime(String startStation, String endStation) 
    {
        Node n = map.get(startStation).get(endStation);
        
        return (n.duration * 1.0) / n.count;
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */
