
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class c {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        List<List<Integer>> a = new ArrayList<>();
        List<Integer> c = new ArrayList<>();
        List<Integer> l = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            l.add(sc.nextInt());
            List<Integer> a_tmp = new ArrayList<>();
            for (int j = 0; j < l.get(i); j++) {
                a_tmp.add(sc.nextInt());
            }
            a.add(a_tmp);
        }
        for (int j = 0; j < n; j++) {
            c.add(sc.nextInt());
        }
        int sore=0;
        int gare=0;//migi
        for(int i=0;i<n;i++){
            sore=gare;
            gare+=c.get(i)*l.get(i);
            if(k<=gare){
                int tmp=(k-sore-1+l.get(i))%l.get(i);
                System.out.println((a.get(i)).get(tmp));
                break;
            }
        }

    }
}
