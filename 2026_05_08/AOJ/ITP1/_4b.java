import java.util.Scanner;

public class _4b {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int r=sc.nextInt();
        double s=r*r*Math.PI;
        double l=2*r*Math.PI;
        System.out.println(String.format("%.6f", s)+" "+String.format("%.6f", l));
    }
}
