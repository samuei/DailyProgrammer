// http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/

/* I'm working under some assumptions. First, that the numerals are actually listed clockwise, because I've had
*  combination locks before, and that's how they're actually arranged. Second, that if the first numeral is 0,
*  that you still have to spin it, but the two spins is enough. You don't have to then spin it again. This makes
*  the math simpler, but an if statement in place of line 25 could change that pretty easily.
*  I'm also assuming that the user isn't going to try anything silly, because I'm the user, here, and I wouldn't
*  do that to me.*/

import java.util.Scanner;

public class ComboLock {
	public static void main(String []args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("How many numbers (including zero) are on the lock?");
		int lockSize = scanner.nextInt();
		System.out.println("Ok. What's the combination? (I won't tell anybody)");
		int combo1 = scanner.nextInt();
		int combo2 = scanner.nextInt();
		int combo3 = scanner.nextInt();
		// This is a step-by-step solution. A more comprehensive solution follows after.
		// initial two spins
		int solution = (2 * lockSize);
		// rolling to the first digit
		solution += combo1;
		// a full spin counterclockwise
		solution += lockSize;
		// then spinning counterclockwise to the second digit
		solution += (lockSize - combo2) + combo1;
		// finally, spinning clockwise from the second to the third
		solution += Math.abs((combo3 - combo2)%lockSize);
		/* Alternately, these could be combined to
		*  int solution = (4*lockSize)+(2*combo1)-combo2+Math.abs((combo3-combo2)%lockSize); */
		System.out.println("You will have to spin past "+solution+" digits to open this lock!");
	}
}

/* Solutions expected:
*  5 1 2 3 = 21
*  5 0 0 0 = 20 */
