import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




from controllers.asset_controller import AssetController
from models.asset import Asset

def main():
    controller = AssetController()
    while True:
        print("\nHardware Asset Management System")
        print("1. Add Asset")
        print("2. List Assets")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter asset name: ")
            category = input("Enter category: ")
            serial_number = input("Enter serial number: ")
            location = input("Enter location: ")
            asset = Asset(name, category, serial_number, location)
            controller.add_asset(asset)
        elif choice == "2":
            assets = controller.list_assets()
            for asset in assets:
                print(asset)
        elif choice == "3":
            asset_id = input("Enter asset ID to update: ")
            field = input("Enter field to update (name/category/serial_number/location/status): ")
            value = input(f"Enter new value for {field}: ")
            controller.update_asset(asset_id, **{field: value})
        elif choice == "4":
            asset_id = input("Enter asset ID to delete: ")
            controller.delete_asset(asset_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


