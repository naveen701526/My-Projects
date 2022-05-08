/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */


    

    public class NestedIterator implements Iterator<Integer> {

    
    ArrayList<Integer> lst = null;
    int curr = 0;
    
    public NestedIterator(List<NestedInteger> nestedList) {
        lst = new ArrayList<>();
        addList(nestedList);
    }
    
    private void addList(List<NestedInteger> nestedList){
        for (NestedInteger list: nestedList){
            if (list.isInteger()) lst.add(list.getInteger());
            else{
                addList(list.getList());
            }
        }
    }

    @Override
    public Integer next() {
        return lst.get(curr++);
    }

    @Override
    public boolean hasNext() {
        return curr<lst.size();
    }
}


/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
