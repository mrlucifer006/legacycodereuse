import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char ch = 'y';
        Support support = new Support(scanner);

        while (ch == 'y' || ch == 'Y') {
            clearScreen();
            System.out.println("An automated billing software");
            System.out.println("1.Admin\n2.Employee\n3.Customer\n4.Exit");
            System.out.print("Enter user type(1/2/3/4): ");

            if (!scanner.hasNextInt()) {
                System.out.println("Invalid input.");
                scanner.nextLine();
                continue;
            }
            int userType = scanner.nextInt();
            scanner.nextLine();

            switch (userType) {

                case 1:
                    clearScreen();
                    support.employee();
                    break;
                case 2:
                    clearScreen();
                    support.employee();
                    break;
                case 3:
                    clearScreen();
                    support.admin();
                    System.out.println("Thank you for using our service. Visit us again!");
                    break;
                case 4:
                    clearScreen();
                    System.out.println("Exited. Thank you for using our service.");
                    return;
                default:
                    System.out.println("Invalid input. Enter a valid choice.");
            }

            System.out.print("Do you want to continue (y/n)? ");
            String res = scanner.nextLine();
            if (res.length() > 0) {
                ch = res.charAt(0);
            } else {
                ch = 'n';
            }
        }
    }

    public static void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
}
