def yield_calculator():
    print("Reaction Yield Calculator\n")

    theoretical = float(input("Enter theoretical yield (g): "))
    actual = float(input("Enter actual yield (g): "))

    if theoretical <= 0:
        print("Theoretical yield must be greater than zero.")
        return

    if actual > theoretical:
        print("Actual yield cannot exceed theoretical yield.")
        return

    percentage_yield = (actual / theoretical) * 100

    print(f"\nTheoretical Yield = {theoretical} g")
    print(f"Actual Yield = {actual} g")
    print(f"Percentage Yield = {round(percentage_yield, 2)}%")

    if percentage_yield >= 90:
        print("Excellent yield!")
    elif percentage_yield >= 70:
        print("Good yield.")
    elif percentage_yield >= 50:
        print("Average yield.")
    else:
        print("Poor yield. Review your reaction conditions.")

yield_calculator()
