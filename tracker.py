import datetime

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   Hey there! Welcome to your Calorie Pal.   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Let's log what you ate and see how you did today.\n")

    all_the_meals = []
    calorie_counts = []
    
    try:
        how_many_meals = int(input("So, how many meals are we logging today? "))
    except ValueError:
        print("Whoops, that doesn't look like a number. Please restart and enter a number like 1, 2, or 3.")
        return

    for i in range(how_many_meals):
        print(f"\n--- Okay, on to meal #{i+1} ---")
        what_meal = input("What did you eat? (e.g., a big breakfast): ")
        
        while True:
            try:
                how_many_calories = float(input(f"Got it. And roughly how many calories were in your {what_meal}? "))
                break
            except ValueError:
                print("Hmm, that's not a valid number. Just type the digits, please.")
        
        all_the_meals.append(what_meal)
        calorie_counts.append(how_many_calories)

    total_cals_today = sum(calorie_counts)
    avg_cals_per_meal = total_cals_today / how_many_meals if how_many_meals > 0 else 0
    
    while True:
        try:
            your_calorie_goal = float(input("\nGreat. What's your daily calorie goal? "))
            break
        except ValueError:
            print("Just the number, please! Let's try that again.")
    
    final_verdict = ""
    if total_cals_today > your_calorie_goal:
        difference = total_cals_today - your_calorie_goal
        final_verdict = f"Looks like you went over your goal by about {difference:.0f} calories. That's okay, tomorrow is a new day!"
    else:
        final_verdict = f"Awesome work! You're right on track and within your goal of {your_calorie_goal:.0f} calories."
        
    print("\n" + final_verdict)

    print("\n\n--- Here's the breakdown for today ---")
    print("======================================")
    print(f"{'What you ate':<20}\t{'Calories'}")
    print("--------------------------------------")
    for meal, cals in zip(all_the_meals, calorie_counts):
        print(f"{meal:<20}\t{cals:.0f}")
    print("--------------------------------------")
    print(f"{'Total today:':<20}\t{total_cals_today:.0f}")
    print(f"{'Average per meal:':<20}\t{avg_cals_per_meal:.0f}")
    print("======================================")

    wanna_save = input("\nAll done! Want me to save this to your log file? (yes/no): ").strip().lower()
    if wanna_save == 'yes':
        try:
            with open("my_calorie_log.txt", "a") as file:
                now = datetime.datetime.now()
                file.write(f"--- Log from {now.strftime('%A, %B %d, %Y at %I:%M %p')} ---\n")
                for meal, cals in zip(all_the_meals, calorie_counts):
                    file.write(f"- {meal}: {cals:.0f} calories\n")
                file.write(f"Total: {total_cals_today:.0f} calories\n")
                file.write(f"Goal was: {your_calorie_goal:.0f} calories\n")
                file.write(f"Verdict: {final_verdict}\n\n")
            print("Got it! Saved to my_calorie_log.txt for you.")
        except IOError:
            print("Oh no, something went wrong and I couldn't save the file.")
    else:
        print("No problem! See you next time. 👋")

if __name__ == "__main__":
    main()