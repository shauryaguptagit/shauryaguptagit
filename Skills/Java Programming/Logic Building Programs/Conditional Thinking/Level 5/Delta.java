//Take time (hours and minutes) and print the smaller angle between the hour and minute hands
//Doubt
import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter an hour: ");
        int hour = sc.nextInt();
        System.out.println("Enter the minutes: ");
        int min = sc.nextInt();

        // 1. Calculate the minute hand's angle from the 12 o'clock position.
        // A full circle is 360 degrees, and there are 60 minutes.
        // 360 / 60 = 6 degrees per minute.
        double min_angle = min * 6.0;

        // 2. Calculate the hour hand's angle from the 12 o'clock position.
        // (hour % 12) treats 12 o'clock as 0.
        // A. It moves 30 degrees for each full hour (360 / 12 = 30).
        // B. It also moves 0.5 degrees for every minute (30 degrees / 60 minutes).
        double hour_angle = (hour % 12) * 30.0 + min * 0.5;

        // 3. Find the absolute difference between the two angles.
        double angle_diff = Math.abs(hour_angle - min_angle);

        // 4. Find the smaller angle.
        // If the difference is 300, the smaller angle is 60 (360 - 300).
        double smaller_angle = Math.min(angle_diff, 360.0 - angle_diff);

        System.out.println("The smaller angle is: " + smaller_angle + " degrees");

        sc.close();
    }
}
