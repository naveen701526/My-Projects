class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a,b)-> b[1]-a[1]);
        int count=0,ans=0;
        
        for(int i=0;i<boxTypes.length;i++)
        {
            ans +=boxTypes[i][0];
            count+=boxTypes[i][0]*boxTypes[i][1];
            if(ans>truckSize)
            {
                ans-=boxTypes[i][0];
                count-=boxTypes[i][0]*boxTypes[i][1];
                int rem=truckSize-ans;
                count+=rem*boxTypes[i][1];
                break;
            }
        }
        return count;
    }
}
