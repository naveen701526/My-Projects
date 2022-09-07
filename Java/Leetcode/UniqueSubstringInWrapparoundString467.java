class Solution {
    public int findSubstringInWraproundString(String p) {
        int t[] = new int[p.length()];
        t[0] = 1;
        Set < String > st = new HashSet < > ();
        st.add(p.charAt(0) + "");
        for (int i = 1; i < p.length(); i++) {
            int x = (p.charAt(i - 1) - 'a' + 1), y = (p.charAt(i) - 'a' + 1);
            if ((p.charAt(i) == 'a' && p.charAt(i - 1) == 'z') || x + 1 == y) {
                t[i] = t[i - 1] + 1;
            } else {
                t[i] = 1;
            }
        }
        Map < Character, Integer > mp = new HashMap < > ();
        int ans = 0;
        for (int i = 0; i < p.length(); i++) {
            if (!mp.containsKey(p.charAt(i))) {
                ans += t[i];
                mp.put(p.charAt(i), t[i]);
            } else if (mp.get(p.charAt(i)) <= t[i]) {
                ans += t[i] - mp.get(p.charAt(i));
                mp.put(p.charAt(i), t[i]);

            }

        }
        return ans;
    }
}
