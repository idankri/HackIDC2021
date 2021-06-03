import json


class UserData:
    def __init__(self, user_id: str, db_path: str):
        self.user_id = user_id
        self.data = {}
        self.db_path = db_path
        self.user_report_path = f"{self.db_path}\\{self.user_id}.json"

    def set(self, item_type: str, price: str):
        self.data[item_type] = {}
        self.data[item_type]["price"] = price

    def set_general(self, **kwargs):
        arg_names = ["name", "city", "house_size", "number_of_family_members", "start_date", "end_date", "house_type",
                     ]
        self.data["general information"] = {}
        for arg_name in arg_names:
            self.data["general information"][arg_name] = kwargs.get(arg_name, None)

    def get(self, item_type) -> dict:
        return self.data[item_type]

    def export_json(self):
        with open(self.user_report_path, "w") as outfile:
            json.dump(self.data, outfile)

    def import_json(self):
        with open(self.user_report_path) as json_file:
            self.data = json.load(json_file)


if __name__ == '__main__':
    myUser = UserData("0548083345", "C:\\Users\\Or\\Desktop\\HackIDC\\HackIDC2021")
    myUser.set_general(name="Or shili", city="Mazkeret batya", house_size="500mr", number_of_family_members="5")
    myUser.set("sofa", "5044")
    myUser.set("tv", "4664000")
    myUser.set("table", "503435400")
    myUser.set("toilet", "5054353400")
    myUser.set("julery", "5034534500")
    myUser.export_json()
