import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (true) {
            System.out.print("\nQuizWiz\n1 Admin\n2 QuizMaster\n3 Player\n4 Exit\nChoose: ");
            String choice = input.nextLine();
            if (choice.equals("1")) { if (Support.login("admin.csv", input)) Support.adminMenu(input); else System.out.println("Invalid credentials."); }
            else if (choice.equals("2")) { if (Support.login("quizmaster.csv", input)) Support.staffMenu(input); else System.out.println("Invalid credentials."); }
            else if (choice.equals("3")) Support.playerMenu(input);
            else if (choice.equals("4")) return;
            else System.out.println("Invalid option.");
        }
    }
}
