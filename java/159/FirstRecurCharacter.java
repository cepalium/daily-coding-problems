import java.util.HashMap;

/**
 * @author Tuan Nguyen
 * @since 20191026
 * @description
Given a string, return the first recurring character in it, or null if there is no recurring chracter.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
 */
public class FirstRecurCharacter {
    /** return the first recurring character in string; otherwise null */
    public Character firstRecurringCharacter(String str) {
        HashMap<Character,Integer> map = new HashMap<>();   // frequency map declared
        int n = str.length();
        for (int i = 0; i < n; i++)     // initialize frequency map: each character has 0 frequeny
            map.put(str.charAt(i), 0);
        for (int i = 0; i < n; i++) {   // find the 1st recurring character by frequency
            Integer freq = map.get(str.charAt(i));
            freq++;                     // increment frequency of the current character
            if (freq == 2) {            // the 1st character to reach 2 
                return str.charAt(i);   // is the 1st recurring character
            } else
                map.put(str.charAt(i), freq);
        }
        return null;                    // reach this ~> no recurring character found
    }

    public static void main(String[] args) {
        FirstRecurCharacter frc = new FirstRecurCharacter();
        String str;
        // test 1
        str = "acbbac";
        assert(frc.firstRecurringCharacter(str) == 'b');
        // test 2
        str = "abcdef";
        assert(frc.firstRecurringCharacter(str) == null);
    }
}