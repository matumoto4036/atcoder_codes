
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class b {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        List<List<Integer>> list=new ArrayList<>();
        for(int i=0;i<n;i++){
            int l=sc.nextInt();
            List<Integer> list_tmp=new ArrayList<>();
            for(int j=0;j<l;j++){
                list_tmp.add(sc.nextInt());
            }
            list.add(list_tmp);
        }
        int x=sc.nextInt();
        int y=sc.nextInt();
        System.out.println((list.get(x-1)).get(y-1));


    }
}
