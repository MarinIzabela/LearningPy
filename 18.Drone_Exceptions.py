class Drone():
    def __init__(self,drone_id, battery, status):
        self.drone_id = drone_id
        self.battery = battery
        self.status = status

    def isReady(self):
        if self.status == 'Inactive':
            raise ValueError('Inactive drone')
        if self.status == 'Damaged ':
            raise ValueError('Damaged drone')
        if self.battery < 30:
            raise ValueError('Battery too low')
        return True
class RescueDrone(Drone):
    pass;

def dispatch(drone):
    try:
        userInput = input(f"Enter 'Y' to dispatch Drone {drone.drone_id}: ")
        if userInput.strip().upper() != 'Y':
            raise ValueError("Dispatch Cancelled")

        drone.isReady()

        print(f" Dispatching Drone {drone.drone_id}")
        return True

    except Exception as e:
        print(e)
        return False



#//------------------Main-------------------------

drones = [
    RescueDrone('D001', 80, 'Active'),
    RescueDrone('D002', 25, 'Active'),
    RescueDrone('D003', 90, 'Inactive'),
    RescueDrone('D004', 50, 'Active'),
]

error_count = 0
MAX_ERRORS = 3
for drone in drones:
    if(drone.status == 'Inactive'):
        print(f" Skipping{drone.drone_id}(status: {drone.status})")
        continue
    success = dispatch(drone)

    if not success:
        error_count += 1
    if error_count >= MAX_ERRORS:
        print(f" Too many dispatch errors.Stopping...")
        break