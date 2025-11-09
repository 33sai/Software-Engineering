"""
Read TOML file and save as binary, then read it back
No libraries allowed - we write everything ourselves
"""
import struct  # For working with binary data

def read_toml_file(file_path):
    """
    Read TOML file and understand its structure
    We go through each line and figure out what it means
    """
    # This will store all our schedule information
    schedule = {
        'variant': 0,    # Your variant number
        'isu': 0,        # Your ISU number
        'week': '',      # Week type
        'days': {}       # Days with their events
    }
    
    current_day = None    # Which day we're currently reading
    current_event = None  # Which event we're currently reading
    
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        all_lines = file.readlines()
    
    # Look at each line one by one
    for line in all_lines:
        line = line.strip()  # Remove extra spaces
        
        # Skip empty lines and comments (lines starting with #)
        if not line or line.startswith('#'):
            continue
            
        # Check if this line starts a new day section like [[tuesday.events]]
        if line.startswith('[[') and line.endswith(']]'):
            day_name = line[2:-2].strip()  # Get the text inside [[ ]]
            if '.' in day_name:
                day_part = day_name.split('.')[0]  # Get just the day name (tuesday)
                current_day = day_part
                current_event = {}  # Start a new empty event
            continue
            
        # Check if this line has a key=value pair
        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            # Remove quotes from strings like "четная" -> четная
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
                
            # If we're not inside a day section, these are top-level settings
            if current_day is None:
                if key == 'variant':
                    schedule['variant'] = int(value)
                elif key == 'isu':
                    schedule['isu'] = int(value)
                elif key == 'week':
                    schedule['week'] = value
                    
            # If we're inside a day section, these are event details
            elif current_event is not None:
                current_event[key] = value
                
                # An event is complete when it has subject, start, and end times
                if 'subject' in current_event and 'start' in current_event and 'end' in current_event:
                    # Add the completed event to the current day
                    if current_day not in schedule['days']:
                        schedule['days'][current_day] = []
                    schedule['days'][current_day].append(current_event)
                    current_event = {}  # Reset for next event
        
    return schedule

def save_as_binary(schedule, output_path):
    """
    Save schedule data as a binary file
    We convert everything to bytes so computers can read it fast
    """
    with open(output_path, 'wb') as file:
        # Save basic info first
        file.write(struct.pack('i', schedule['variant']))  # Save variant as 4 bytes
        file.write(struct.pack('i', schedule['isu']))      # Save ISU as 4 bytes
        
        # Save week text - first save length, then the text itself
        week_bytes = schedule['week'].encode('utf-8')
        file.write(struct.pack('i', len(week_bytes)))  # Length of week text
        file.write(week_bytes)                         # The actual week text
        
        # Save how many days we have
        file.write(struct.pack('i', len(schedule['days'])))
        
        # Save each day and its events
        for day_name, events in schedule['days'].items():
            # Save day name - first length, then name
            day_bytes = day_name.encode('utf-8')
            file.write(struct.pack('i', len(day_bytes)))
            file.write(day_bytes)
            
            # Save how many events this day has
            file.write(struct.pack('i', len(events)))
            
            # Save each event's details
            for event in events:
                # Save each field in the same order every time
                for field in ['type', 'subject', 'teacher', 'room', 'address', 'start', 'end', 'mode']:
                    value = event.get(field, '')  # Get value or empty string if missing
                    value_bytes = value.encode('utf-8')
                    file.write(struct.pack('i', len(value_bytes)))  # Save length
                    file.write(value_bytes)                         # Save value

def load_from_binary(input_path):
    """
    Read schedule data back from binary file
    This is the reverse of save_as_binary
    """
    schedule = {
        'variant': 0,
        'isu': 0,
        'week': '',
        'days': {}
    }
    
    with open(input_path, 'rb') as file:
        # Read basic info back
        schedule['variant'] = struct.unpack('i', file.read(4))[0]
        schedule['isu'] = struct.unpack('i', file.read(4))[0]
        
        # Read week text back
        week_len = struct.unpack('i', file.read(4))[0]
        schedule['week'] = file.read(week_len).decode('utf-8')
        
        # Read how many days we have
        days_count = struct.unpack('i', file.read(4))[0]
        
        # Read each day back
        for _ in range(days_count):
            # Read day name
            day_len = struct.unpack('i', file.read(4))[0]
            day_name = file.read(day_len).decode('utf-8')
            
            # Read how many events this day has
            events_count = struct.unpack('i', file.read(4))[0]
            events_list = []
            
            # Read each event back
            for _ in range(events_count):
                event = {}
                # Read each field in same order we saved them
                for field in ['type', 'subject', 'teacher', 'room', 'address', 'start', 'end', 'mode']:
                    value_len = struct.unpack('i', file.read(4))[0]
                    value = file.read(value_len).decode('utf-8')
                    event[field] = value
                events_list.append(event)
                
            schedule['days'][day_name] = events_list
            
    return schedule

if __name__ == '__main__':
    print("=== MAIN TASK (50% of grade) ===")
    print("Reading TOML and saving as binary...")
    
    # Step 1: Read and understand the TOML file
    my_schedule = read_toml_file('schedule_503266_v82.toml')
    print(f"Found: variant={my_schedule['variant']}, ISU={my_schedule['isu']}, week={my_schedule['week']}")
    
    # Step 2: Save as binary file
    save_as_binary(my_schedule, 'schedule_503266_v82.bin')
    print("Saved as binary file: schedule_503266_v82.bin")
    
    # Step 3: Read it back to make sure it worked
    recovered_schedule = load_from_binary('schedule_503266_v82.bin')
    print("Successfully read back from binary file")
    
    # Show what we got back
    for day_name, events in recovered_schedule['days'].items():
        print(f"  {day_name}: {len(events)} classes")