import java.util.Scanner;

public class _1d {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s=n%60;
        int m=(int)(n/60)%60;
        int h=(int)(n/60)/60;
        System.out.println(h+" "+m+" "+s);
    }
}
