
import java.util.Scanner;

public class _3b {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, i = 1;
        while (true) {

            x = sc.nextInt();
            if (x == 0) {
                break;
            }
            System.out.println("case" + i + "," + x);
            i++;
        }
    }
}
