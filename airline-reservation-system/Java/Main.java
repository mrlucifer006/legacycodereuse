import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (true) {
            System.out.print("\nAirline Reservation System\n1. Admin\n2. Agent\n3. Customer\n4. Exit\nChoice: ");
            String choice = input.nextLine();
            if (choice.equals("1")) Support.adminMenu(input);
            else if (choice.equals("2")) Support.agentMenu(input);
            else if (choice.equals("3")) Support.customerMenu(input);
            else if (choice.equals("4")) return;
            else System.out.println("Invalid choice.");
        }
    }
}
