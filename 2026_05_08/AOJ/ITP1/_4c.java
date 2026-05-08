import java.util.Scanner;

public class _4c {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        while(true){
            int a=sc.nextInt();
            char op=sc.next().charAt(0);
            int y=sc.nextInt();
            if(op=='+'){
                System.out.println(a+y);
            }
            else if(op=='-'){
                System.out.println(a-y);
            }
            else if(op=='*'){
                System.out.println(a*y);
            }
            else if(op=='/'){
                System.out.println(a/y);
            }
            else if(op=='?'){
                break;
            }
        }
    }
}
