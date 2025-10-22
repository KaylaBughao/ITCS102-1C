vegetable_list = []

print("Welcome to the Vegetable List Creator!")
print("Enter the name of a vegetable (or type 'exit' to finish).")

while True:
    vegetable = input("Enter the name of a vegetable (or type 'exit' to finish): ").strip()

    if vegetable.lower() == 'exit':
        print("\nYou have exited the vegetable entry program.")
        break

    elif vegetable == "":
        print("You did not enter any name. Please type a vegetable name or 'exit'.")
        continue

    vegetable_list.append(vegetable)
    print(f"'{vegetable}' has been added to your vegetable list.\n")

print("\nYour vegetable list includes:")
if len(vegetable_list) == 0:
    print("No vegetables were added.")
else:
    for item in vegetable_list:
        print(f"- {item}")

print("\nThank you for using the Vegetable List Creator!")
