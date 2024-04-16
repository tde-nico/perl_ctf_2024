import java.util.Scanner;

// 
// Decompiled by Procyon v0.6.0
// 

public class input_validator
{
    private static final int FLAG_LEN = 34;
    
    private static boolean validate(final String s, final String s2) {
        final int[] array = new int[34];
        final int[] array2 = { 1102, 1067, 1032, 1562, 1612, 1257, 1562, 1067, 1012, 902, 882, 1397, 1472, 1312, 1442, 1582, 1067, 1263, 1363, 1413, 1379, 1311, 1187, 1285, 1217, 1313, 1297, 1431, 1137, 1273, 1161, 1339, 1267, 1427 };
        for (int i = 0; i < 34; ++i) {
            array[i] = (s.charAt(i) ^ s2.charAt(i));
        }
        for (int j = 0; j < 34; ++j) {
            array[j] -= s2.charAt(33 - j);
        }
        final int[] array3 = new int[34];
        for (int k = 0; k < 17; ++k) {
            array3[k] = array[1 + k * 2] * 5;
            array3[k + 17] = array[k * 2] * 2;
        }
        for (int l = 0; l < 34; ++l) {
            final int[] array4 = array3;
            final int n = l;
            array4[n] += 1337;
        }
        for (int n2 = 0; n2 < 34; ++n2) {
            if (array3[n2] != array2[n2]) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(final String[] array) {
        final Scanner scanner = new Scanner(System.in);
        final String s = "oF/M5BK_U<rqxCf8zWCPC(RK,/B'v3uARD";
        System.out.print("Enter input: ");
        final String nextLine = scanner.nextLine();
        if (nextLine.length() != 34) {
            System.out.println("Input length does not match!");
            return;
        }
        if (validate(new String(nextLine), s)) {
            System.out.println("Correct");
        }
        else {
            System.out.println("Wrong");
        }
    }
}
