class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String,Integer> map = new HashMap<>();
        List<String> ans = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        for(int i=0; i<list1.length; i++)
        map.put(list1[i],i);
        
        for(int i=0; i<list2.length; i++)
        {
            if(map.containsKey(list2[i]))
            {
                int ind = i+map.get(list2[i]);
                if(ind<min)
                {
                    min = ind;
                    ans.clear();
                    ans.add(list2[i]);
                }
                else if(ind==min)
                    ans.add(list2[i]);
            }
        }
        return ans.toArray(new String[ans.size()]);
    }
}