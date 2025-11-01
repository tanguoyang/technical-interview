class Event:
    def __init__(self):
        self.type = "Basic"
        self.time = 0

class FloorPressEvent(Event):
    def __init__(self, floor):
        super().__init__()
        self.type = "Floor Press"
        self.floor = floor

class OpenDoorPressEvent(Event):
    def __init__(self):
        super().__init__()
        self.type = "Open Door"

class CloseDoorPressEvent(Event):
    def __init__(self):
        super().__init__()
        self.type = "Close Door"


class Cabin:
    def __init__(self, max_floor, travel_duration_ms, door_open_duration_ms, door_close_duration_ms=1000):
        # Current state of the FSM - should be one of:
        # "Stationary", "In Motion", "Door Opening", "Door Open", "Door Closing"
        self.FSM = "Stationary" 
        
        # Current floor position (0 to max_floor)
        self.floor = 0
        
        # Configuration parameters
        self.max_floor = max_floor                          # Highest floor number
        self.travel_duration_ms = travel_duration_ms        # Time to travel between adjacent floors
        self.door_open_duration_ms = door_open_duration_ms  # How long doors stay open before auto-closing
        self.door_close_duration_ms = door_close_duration_ms # Time it takes for doors to physically open/close
        
        # Queue of floor requests (list of integers)
        self.floor_requests = []

        # Timing trackers (milliseconds)
        self.door_open_time = 0      # When doors started opening
        self.door_close_time = 0     # When doors started closing
        self.travel_start_time = 0   # When travel to next floor started
        self.current_time = 0        # Current time (updated from events)
        
        # Next destination floor (None when stationary or doors open/opening/closing)
        self.next_floor = None

    def update(self, event: Event):
        """
        Main FSM update method - this is called for every event.
        
        You need to implement the state machine logic here!
        
        Tips:
        - Update self.current_time from event.time first
        - Use if/elif statements to handle different states
        - Within each state, check event.type to handle different events
        - Use helper methods (_open_door, _close_door, _start_moving) to avoid repetition
        - Remember to check time elapsed for transitions (e.g., door opening -> door open)
        """
        
        # Always update current time from the event
        self.current_time = event.time

        # TODO: Implement state machine logic here
        # 
        # Structure suggestion:
        # if self.FSM == "Stationary":
        #     # Handle events for Stationary state
        #     pass
        #
        # elif self.FSM == "In Motion":
        #     # Handle events for In Motion state
        #     pass
        #
        # elif self.FSM == "Door Opening":
        #     # Handle events for Door Opening state
        #     pass
        #
        # elif self.FSM == "Door Open":
        #     # Handle events for Door Open state
        #     pass
        #
        # elif self.FSM == "Door Closing":
        #     # Handle events for Door Closing state
        #     pass

        # Hint for Stationary state:
        # - Check if Open Door button pressed -> open doors
        # - Check if Floor Press for current floor -> open doors
        # - Check if Floor Press for different floor -> add to queue
        # - Check if there are pending requests -> start moving
        
        # Hint for In Motion state:
        # - Check if Floor Press -> add to queue
        # - Check if travel time elapsed -> arrive at floor, open doors
        
        # Hint for Door Opening state:
        # - Check if Floor Press for different floor -> add to queue
        # - Check if opening time elapsed -> transition to Door Open
        
        # Hint for Door Open state:
        # - Check if Close Door pressed -> close doors
        # - Check if Open Door pressed -> reset timer
        # - Check if Floor Press for current floor -> reset timer
        # - Check if Floor Press for different floor -> add to queue
        # - Check if auto-close timer expired -> close doors
        
        # Hint for Door Closing state:
        # - Check if Open Door pressed -> reopen (safety feature)
        # - Check if Floor Press for current floor -> reopen (safety feature)
        # - Check if Floor Press for different floor -> add to queue
        # - Check if closing time elapsed -> go to Stationary or In Motion

        pass  # Remove this when you implement the method
    
    def _start_moving(self):
        """
        Helper method to start moving to the next floor in the request queue.
        
        This method:
        1. Picks the nearest floor from floor_requests
        2. Removes it from the queue
        3. Sets it as next_floor
        4. Changes state to "In Motion"
        5. Records the travel start time
        """
        pass

    def _open_door(self):
        """
        Helper method to start opening the doors.
        
        This method:
        1. Records when doors started opening
        2. Changes state to "Door Opening"
        
        The doors will automatically transition to "Door Open" after
        door_close_duration_ms milliseconds have passed.
        """

        pass
      
      

    def _close_door(self):
        """
        Helper method to start closing the doors.
        
        This method:
        1. Records when doors started closing
        2. Changes state to "Door Closing"
        
        The doors will automatically transition to "Stationary" or "In Motion"
        after door_close_duration_ms milliseconds have passed.
        """
        self.door_close_time = self.current_time
        self.FSM = "Door Closing"
    
    def get_state(self):
        """
        Returns the current state of the cabin for display/debugging.
        You don't need to modify this method.
        """
        return {
            "state": self.FSM,
            "floor": self.floor,
            "next_floor": self.next_floor,
            "pending_requests": self.floor_requests
        }
