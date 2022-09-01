class Solution {
    public boolean hasAlternatingBits(int n) {
        
    
        int lastdigit;
        ArrayList<Integer> arrayList= new ArrayList<>();
        while (n>0){

            lastdigit=n&1;
            arrayList.add(lastdigit);
            n= n>>1;
        }
        
        return(answer(arrayList));

       }
    
    boolean answer(ArrayList<Integer> arrayList){
        boolean b=true;

        for (int i = 0; i < arrayList.size()-1; i++) {
            if(Objects.equals(arrayList.get(i), arrayList.get(i + 1))){
                b=false;
                break;
            }

        }
        return b;
    }
}
