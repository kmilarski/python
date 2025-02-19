''' Create a list representing 20 seats, numbered 1 to 20.

    Display the list of available seats to the customer.

    Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.

    Remove the selected seat from the list of available seats and display the updated list.

    If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.

    Ensure the program gracefully handles all scenarios and is user-friendly.'''

# sets the seat range from 1-20
seats = list(range(1, 21))

# while loop runs forever until break or conditions met
while True:
    print("Available seats:", seats)
    selected_seat = input(
        "\nSelect an available seat number (enter 0 to exit):")
    if selected_seat.isdigit():  # determines if selected seat is a digit. If it is not it will return a message
        selected_seat = int(selected_seat)  # sets selected seat to an integer
        if selected_seat == 0:  # you can enter 0 to force the loop to break
            print("\nHave a nice day!")
            break

        if selected_seat in seats:  # if the seat inputted is in the seats list, will ask to confirm you want the seat or not
            confirm = input(
                f"\nSeat {selected_seat} is available. Would you like to claim it? (yes/no):")

            if confirm == "yes":
                seats.remove(selected_seat)
                print(f"\nSeat {selected_seat} has been booked.")

                if len(seats) == 0:  # when all seats are sold out, will reset the list
                    print("\nAll seats are sold out.")
                    seats = list(range(1, 21))
                    break
            else:
                print(
                    "\nSeat not booked. You can select another seat if you would like.")

        else:
            print("\nNot in selection. Please select a different seat.")
    else:
        print("\nInput an number please.")
