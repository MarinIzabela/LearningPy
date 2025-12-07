import os


file = open("example.txt","w")
file.write("Hello World")
file.close()

file = open("example.txt","r")
content = file.read()
print(content)
file.close()


#we add the import os to delete the file
os.remove("example.txt")
print("File removed")

#handling File Errors and Exceptions

class SurveyFileHandler:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputfile = outputFile

    def create_test_file(self):
        file = open(self.inputFile, "w")
        file.write("Customer Name, Feedback\n Izabela Marin, 5 *\n" )
        file.close()
        print("File created successfully")

    def read_file(self):
        if not os.path.exists(self.inputFile):
            print("File not found")
            return None
        try:
            file = open(self.inputFile, "r")
            data = file.read()
            file.close()
            print("File read successfully.")
            if "Customer Name" not in data:
                raise ValueError("Customer Name not found")
            return data
        except PermissionError:
            print("Permission denied")
        except ValueError as e:
            print("The file format is not correct. Please, try again")
            print("Error: ", e)
        except Exception as e:
            print("Something went wrong. Please try again")
            print("Error: ", e)
        return None
    def write_file(self, data):
        try:
            file = open(self.outputfile, "w")
            file.write(data)
            file.close()
            print("File written successfully")
        except OSError:
            print("Not enough space for writing. Please free space and try again!")



handler = SurveyFileHandler("customer_feedback.csv","survey.csv")
handler.create_test_file()
data = handler.read_file()
if data:
    handler.write_file("Survey")