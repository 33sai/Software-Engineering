"""
Read binary file and save as HCL text file
HCL is like a settings file format
"""
from task1_required import load_from_binary  # We use the binary reader from Task 1

def make_hcl_file(schedule):
    """
    Convert schedule data to HCL format
    HCL files look like: key = value with blocks in { }
    """
    lines = []  # We'll build the file line by line
    
    # Add some comments at the top
    lines.append("# Schedule file in HCL format")
    lines.append("# Made from binary data")
    lines.append("")
    
    # Basic settings at the top
    lines.append(f'variant = {schedule["variant"]}')
    lines.append(f'isu = {schedule["isu"]}')
    lines.append(f'week = "{schedule["week"]}"')
    lines.append('')
    
    # For each day, create a block
    for day_name, events in schedule['days'].items():
        # Start day block
        lines.append(f'day "{day_name}" {{')
        
        # Add each event as a sub-block
        for event in events:
            lines.append('  event {')
            
            # Add all the event details
            for field, value in event.items():
                # If value has quotes, we need to escape them with \
                safe_value = value.replace('"', '\\"')
                lines.append(f'    {field} = "{safe_value}"')
                
            lines.append('  }')
            
        lines.append('}')  # Close day block
        lines.append('')   # Empty line between days
    
    # Join all lines with newlines
    return '\n'.join(lines)

if __name__ == '__main__':
    print("=== EXTRA TASK 1 (+15% of grade) ===")
    print("Converting binary to HCL...")
    
    # Step 1: Load schedule from binary file
    schedule_data = load_from_binary('schedule_503266_v82.bin')
    print("Loaded schedule from binary file")
    
    # Step 2: Convert to HCL format
    hcl_text = make_hcl_file(schedule_data)
    
    # Step 3: Save as HCL file
    with open('schedule_503266_v82.hcl', 'w', encoding='utf-8') as file:
        file.write(hcl_text)
        
    print("Saved as HCL file: schedule_503266_v82.hcl")
    
    # Show a preview
    print("\nFirst few lines of HCL file:")
    for line in hcl_text.split('\n')[:10]:
        print(line)