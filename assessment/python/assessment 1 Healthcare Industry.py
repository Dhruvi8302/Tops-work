class ClinicAppointment:
    def __init__(self):
        self.appointments = []

    def bookApprointment(self, dict1):
        self.dr_dict = dict1

        name = input("Enter patient Name: ")
        try:
            age = int(input("Enter Age: "))
            mobile_num = int(input("Enter Mobile number: "))
        except ValueError:
            print("Age and Mobile number must be numbers!")
            return

        print("\nAvailable Doctors:")
        for key, value in dict1.items():
            for dr_name in value:
                print(f"{key}) {dr_name}")

        try:
            doc_choice = int(input("Enter preferred Doctor Number: "))
        except ValueError:
            print("Enter a valid doctor number!")
            return

        if doc_choice in dict1:
            doctor_info = dict1[doc_choice]
            doctor_name = list(doctor_info.keys())[0]
            print(f"\nSelected Doctor: {doctor_name}")

            slot_list = list(doctor_info[doctor_name].keys())

            print("\nAvailable Slots:")
            for i, slot in enumerate(slot_list, 1):
                count = doctor_info[doctor_name][slot]
                print(f"{i}) {slot} ({count}/3 booked)")

            try:
                slot_choice = int(input("\nEnter Slot Number: "))
                if slot_choice < 1 or slot_choice > len(slot_list):
                    print("Invalid slot number!")
                    return
            except ValueError:
                print("Enter a valid number!")
                return

            time_slot = slot_list[slot_choice - 1]

            # ✅ Check availability before booking
            if self.checkAvaibility(doc_choice, doctor_name, time_slot):
                self.appointments.append({
                    "name": name,
                    "age": age,
                    "mobile": mobile_num,
                    "doctor": doctor_name,
                    "slot": time_slot
                })

                print("\n Appointment Booked Successfully!")
                print(f"Patient: {name} | Age: {age} | Mobile: {mobile_num}")
                print(f"Doctor: {doctor_name} | Slot: {time_slot}")
            else:
                print("\n Slot Full! Cannot book appointment. Try another slot.")
        else:
            print("\nInvalid doctor choice!")

        print("\nUpdated Doctor Slots:")
        print(self.dr_dict)

    def checkAvaibility(self, doctor_choice, doctor_name, time_slot):
        no_of_slots = self.dr_dict[doctor_choice][doctor_name][time_slot]
        print(f"Current bookings in this slot: {no_of_slots}")

        if no_of_slots < 3:
            self.dr_dict[doctor_choice][doctor_name][time_slot] = no_of_slots + 1
            return True
        else:
            return False

    def viewAppointment(self):
        try:
            mob = int(input("\nEnter Mobile Number to view Appointment: "))
        except ValueError:
            print("Enter valid number!")
            return

        found = False
        for app in self.appointments:
            if app["mobile"] == mob:
                found = True
                print("\nAppointment Details:")
                print(f"Name: {app['name']}")
                print(f"Age: {app['age']}")
                print(f"Mobile: {app['mobile']}")
                print(f"Doctor: {app['doctor']}")
                print(f"Slot: {app['slot']}")

        if not found:
            print("No appointment found for this number!")

    def cancelAppointment(self):
        try:
            mob = int(input("\nEnter Mobile Number to cancel Appointment: "))
        except ValueError:
            print("Enter valid number!")
            return

        for app in self.appointments:
            if app["mobile"] == mob:
                # Reduce count back in doctor dict
                for key, doc in self.dr_dict.items():
                    if app["doctor"] in doc:
                        self.dr_dict[key][app["doctor"]][app["slot"]] -= 1

                self.appointments.remove(app)
                print("\nAppointment Cancelled Successfully!")
                return

        print("No appointment found with this number!")


# -------- Main Code --------
dict1 = {
    1: {'Mr. Patel': {'10 am': 0, '11 am': 0, '2 pm': 0}},
    2: {'Mr. Shah': {'11 am': 0, '12 am': 0, '2 pm': 0}},
    3: {'Mr. Modi': {'10 am': 0, '11 am': 0}}
}

obj = ClinicAppointment()

while True:
    print("\n1. Book Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number!")
        continue

    match ch:
        case 1: obj.bookApprointment(dict1)
        case 2: obj.viewAppointment()
        case 3: obj.cancelAppointment()
        case 4:
            print("Exiting...")
            break
        case _: print("Invalid Choice!")
