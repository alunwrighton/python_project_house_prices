from openpyxl import load_workbook

class DataFileReader:

    def __init__(self, file_name):
        self.workbook = load_workbook(file_name, read_only=True)
        self.worksheet = self.workbook.active

    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)

    def print_all_cell_data(self):
        for i in self.worksheet.values:
            print(i)
    #BELOW
    def convert_to_list(self):
        data_list = []
        for i in self.worksheet.values:
            data_list.append(i)
        return data_list

    def print_all_data_cells_coordinates(self):
        for i in self.worksheet.rows:
            for p in i:
                print(p.coordinate)