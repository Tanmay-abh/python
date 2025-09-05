try:
    # Outer block: file handling
    f = open("File_handling\\flights.txt", "r")

    try:
        # Inner block: booking logic
        lines = f.readlines()
        if not lines:
            raise ValueError("Flight file is empty.")

        flights = []
        for line_number, line in enumerate(lines, start=1):
            parts = line.strip().split()
            if len(parts) != 3:
                print(f"[Warning] Invalid format at line {line_number}: {line.strip()}")
                continue

            flight_no = parts[0].strip().upper()
            try:
                available_seats = int(parts[1])
                price = float(parts[2])

                if available_seats < 0:
                    raise ValueError("Available seats cannot be negative.")
                if price <= 0:
                    raise ValueError("Price must be greater than zero.")

                flights.append([flight_no, available_seats, price])
            except ValueError as ve:
                print(f"[Warning] Skipping line {line_number}: {ve}")
                continue

        if not flights:
            raise ValueError("No valid flights available.")

        # Display all available flights
        print("\nAvailable Flights:")
        print("{:<10} {:<10} {:<10}".format("Flight", "Seats", "Price"))
        for flight in flights:
            print("{:<10} {:<10} ₹{:<10.2f}".format(flight[0], flight[1], flight[2]))

        # Booking section (inner try-except)
        try:
            user_flight = input("\nEnter flight number to book: ").strip().upper()
            tickets_str = input("Enter number of tickets to book: ").strip()

            if not tickets_str.isdigit():
                raise ValueError("Number of tickets must be a positive integer.")

            tickets = int(tickets_str)

            if tickets <= 0:
                raise ZeroDivisionError("Cannot book zero or negative tickets.")

            # Find the flight
            for flight in flights:
                if flight[0] == user_flight:
                    if tickets > flight[1]:
                        raise Exception("SeatsUnavailableError: Not enough seats available.")

                    total = tickets * flight[2]

                    try:
                        discount_per_ticket = total / tickets 
                    except ZeroDivisionError:
                        raise ZeroDivisionError("Division by zero while calculating per-ticket cost.")

                    
                    print("\nBooking successful!")
                    print(f"Flight Number    : {flight[0]}")
                    print(f"Available Seats  : {flight[1]}")
                    print(f"Price per Ticket : ₹{flight[2]:.2f}")
                    print(f"Tickets Booked   : {tickets}")
                    print(f"Total Cost       : ₹{total:.2f}")
                    print(f"Discount per Ticket (Total / Tickets): ₹{discount_per_ticket:.2f}")
                    break
            else:
                raise Exception("FlightNotFoundError: Flight not found.")

        except ValueError as ve:
            print("[ValueError]", ve)
        except ZeroDivisionError as zde:
            print("[ZeroDivisionError]", zde)
        except Exception as e:
            if "FlightNotFoundError" in str(e):
                print("[FlightNotFoundError]", str(e).split(":", 1)[1].strip())
            elif "SeatsUnavailableError" in str(e):
                print("[SeatsUnavailableError]", str(e).split(":", 1)[1].strip())
            else:
                print("[Error] Unexpected booking error:", e)
            raise

    finally:
        f.close()
        print("\n[Info] File closed.")

except FileNotFoundError:
    print("[FileNotFoundError] 'flights.txt' not found. Please check the file path.")

except Exception as outer_exception:
    print("[Critical Error] Booking process failed:", outer_exception)
