from flask import Flask, render_template, request, jsonify
from CabinFSM import Cabin, FloorPressEvent, OpenDoorPressEvent, CloseDoorPressEvent, Event
import time
import threading

app = Flask(__name__)

# Initialize the cabin (5 floors, 2000ms travel time between floors, 3000ms door open duration, 1000ms door close duration)
cabin = Cabin(max_floor=5, travel_duration_ms=2000, door_open_duration_ms=3000, door_close_duration_ms=1000)
start_time = time.time() * 1000  # Convert to milliseconds
cabin_lock = threading.Lock()

def get_current_time_ms():
    """Get current time in milliseconds since server start"""
    return (time.time() * 1000) - start_time

def update_cabin_time():
    """Background thread that continuously updates the cabin with time events"""
    while True:
        time.sleep(0.1)  # Update every 100ms
        with cabin_lock:
            event = Event()
            event.time = get_current_time_ms()
            cabin.update(event)

# Start background time update thread
time_thread = threading.Thread(target=update_cabin_time, daemon=True)
time_thread.start()

@app.route('/')
def index():
    return render_template('index.html', max_floor=cabin.max_floor)

@app.route('/api/state', methods=['GET'])
def get_state():
    """Get the current state of the cabin"""
    with cabin_lock:
        state = cabin.get_state()
        state['current_time'] = get_current_time_ms()
    return jsonify(state)

@app.route('/api/press_floor', methods=['POST'])
def press_floor():
    """Handle floor button press"""
    data = request.json
    floor = data.get('floor')
    
    if floor is None or floor < 0 or floor > cabin.max_floor:
        return jsonify({'error': 'Invalid floor'}), 400
    
    with cabin_lock:
        event = FloorPressEvent(floor)
        event.time = get_current_time_ms()
        cabin.update(event)
        state = cabin.get_state()
        state['current_time'] = get_current_time_ms()
    
    return jsonify(state)

@app.route('/api/open_door', methods=['POST'])
def open_door():
    """Handle open door button press"""
    with cabin_lock:
        event = OpenDoorPressEvent()
        event.time = get_current_time_ms()
        cabin.update(event)
        state = cabin.get_state()
        state['current_time'] = get_current_time_ms()
    
    return jsonify(state)

@app.route('/api/close_door', methods=['POST'])
def close_door():
    """Handle close door button press"""
    with cabin_lock:
        event = CloseDoorPressEvent()
        event.time = get_current_time_ms()
        cabin.update(event)
        state = cabin.get_state()
        state['current_time'] = get_current_time_ms()
    
    return jsonify(state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
