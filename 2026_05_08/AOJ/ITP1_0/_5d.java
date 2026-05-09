
import java.util.Scanner;

public class _5d {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0) {
                System.out.println(i);
            } else {
                int tmp = i;
                Boolean flag = true;
                while (flag) {
                    if (tmp % 10 == 3) {
                        System.out.println(i);
                        flag = false;
                    } else {
                        tmp = tmp / 10;
                        if (tmp == 0) {
                            flag = false;
                        }
                    }
                }
            }
        }
    }
}
