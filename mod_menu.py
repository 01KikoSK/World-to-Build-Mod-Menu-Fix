class ModMenu:
    def __init__(self):
        self.mod_enabled = False

    def toggle_mod(self):
        self.mod_enabled = not self.mod_enabled
        print(f"Mod is {'enabled' if self.mod_enabled else 'disabled'}")

    def display_menu(self):
        while True:
            print("\nMod Menu")
            print("1. Toggle mod")
            print("2. Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if choice == 1:
                self.toggle_mod()
            elif choice == 2:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    mod_menu = ModMenu()
    mod_menu.display_menu()