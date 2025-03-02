from database.db_handler import DBHandler

class AssetController:
    def __init__(self):
        self.db = DBHandler()

    def add_asset(self, asset):
        try:
            self.db.execute_query('''
                INSERT INTO assets (name, category, serial_number, location, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (asset.name, asset.category, asset.serial_number, asset.location, asset.status))
            print("Asset added successfully.")
        except:
            print("Error: Asset with this serial number already exists.")

    def list_assets(self):
        return self.db.fetch_all("SELECT * FROM assets")

    def update_asset(self, asset_id, **kwargs):
        updates = ", ".join(f"{key} = ?" for key in kwargs.keys())
        params = list(kwargs.values()) + [asset_id]
        self.db.execute_query(f"UPDATE assets SET {updates} WHERE id = ?", params)
        print("Asset updated successfully.")

    def delete_asset(self, asset_id):
        self.db.execute_query("DELETE FROM assets WHERE id = ?", (asset_id,))
        print("Asset deleted successfully.")