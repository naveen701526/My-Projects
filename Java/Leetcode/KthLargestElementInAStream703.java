class KthLargest {
    //minHeap 
    PriorityQueue < Integer > pq;
    int k;
    public KthLargest(int k, int[] nums) {
        ///initialise k and priorityQueue
        this.k = k;
        //size of PQ is k+1 so that it can hold k+1 element and whenever the size 
        //reaches k+1 we will poll() the smallest element to make the size as k
        pq = new PriorityQueue < > (k + 1);
        for (int i = 0; i < nums.length; i++) {
            pq.add(nums[i]);
            if (pq.size() > k)
                pq.poll();
        }
    }

    public int add(int val) {
        pq.add(val);

        if (pq.size() > k)
            //if the size reached k+1 remove the minimum element
            pq.poll();

        return pq.peek();
    }
}
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
