class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> hash = new HashMap<>();
        for(char c : s.toCharArray()) {
            if(hash.containsKey(c)) {
                int count = hash.get(c);
                count++;
                hash.put(c,count);
            } else {
                hash.put(c,1);
            }
        }

        for(Character c : t.toCharArray()) {
            if(hash.containsKey(c)) {
                int count = hash.get(c);
                if(count==0) {
                    return false;
                } else {
                    count--;
                    hash.put(c,count);
                }
            } else {
                return false;
            }
        }

        for(Integer i : hash.values()) {
            if(i != 0) {
                return false;
            }
        }

        return true;
    }
}
