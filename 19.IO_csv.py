import os
import shutil
import csv

source_folder = 'incoming_logs'
destination_folder = 'archived_logs'
file_name ='cisco_device_logs.csv'

#we create the variables
source_path = os.path.join(source_folder, file_name)
destination_path = os.path.join(destination_folder, file_name)
#Step 1. Create folders if they do not exist
os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)
#Step 2 . Create csv file if it doesn't exist

if not os.path.exists(source_path):
    with open(source_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['DeviceId', 'Status', 'Timestamp']) #title of columns
        writer.writerow(['CISCO 9012', 'online', '2025-03-20:7:20:01'])
        writer.writerow(['CISCO 9013', 'online', '2025-03-20:7:20:01'])
        writer.writerow(['CISCO 9014', 'offline', '2025-03-20:7:20:01'])


#step 3 Read and move file if exists
if os.path.exists(source_path):
    print("Reading logs from: " + source_path)
    with open(source_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(f"Headers: {headers}")

        for row in reader:
            print(f"Row: {row}")
    shutil.move(source_path, destination_path) #moving the file
    print("Moving logs to: " + destination_path)
else:
    print("Log not found")