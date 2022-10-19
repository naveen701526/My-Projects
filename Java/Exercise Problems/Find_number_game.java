import java.util.*;

public class Find_Number {
	public static void main(String[] args) {
		int randNo, inputNo, userAttempt = 1;
		Scanner scan = new Scanner(System.in);
		Random rand = new Random();
		randNo = rand.nextInt(101);
		System.out.println("Guess the number between 1 to 100\n");
		do {
			inputNo = scan.nextInt();
			if (inputNo > randNo) 
				System.out.println("Lower number!!");
			else if (inputNo < randNo) 
				System.out.println("Higher number!!");
			else
				System.out.println("Correct!! \nYou guessed in " + userAttempt + "  attempts.");
			userAttempt++;
		} while (inputNo != randNo);
	}
}
