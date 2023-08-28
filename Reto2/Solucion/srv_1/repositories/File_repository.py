import csv

class File_repository():
    # __file_path = ""
    # __file_open = None

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__file_open = None

    def __open_file(self)->None:
        if(self.__file_open == None):
            self.__file_open = open(self.__file_path)

    def __close_file(self)->None:
        if(self.__file_open):
            self.__file_open.close()

    def __read_data(self):
        try:
            data_read = []

            self.__open_file()
            csv_reader = csv.reader(self.__file_open)

            next(csv_reader)#Omite el encabezado
            for row in csv_reader:
                data_read.append(row)

            return data_read
        
        except Exception as exception:
            raise Exception('Error while reading data: ', str(exception))
        finally:
            self.__close_file


    def get_data(self):
        return self.__read_data()




    