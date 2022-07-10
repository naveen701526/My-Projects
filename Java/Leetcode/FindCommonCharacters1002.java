class Solution {
    public List<String> commonChars(String[] words) {
        String[] val=words[0].split("");
       
    List<String> res=new ArrayList<>();
    if(words.length==1){
        return Arrays.asList(val);
    }
       
    for(int i=0;i<val.length;i++){
            String temp=val[i];
        for(int j=1;j<words.length;j++){
            
            if(words[j].contains(temp)){
                words[j]=words[j].replaceFirst(temp,"");
            }
            
            else if(!words[j].contains(temp))
                break;
            
            if(j==words.length-1)
                res.add(temp);
        }
    }
    return res;
    }
}
