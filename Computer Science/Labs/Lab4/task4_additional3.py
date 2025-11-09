"""
Read binary file and save as XML
XML is like HTML but for data
"""
from task1_required import load_from_binary

def make_xml_file(schedule):
    """
    Convert schedule to XML format
    XML uses tags like <day> and <event>
    """
    lines = []
    
    # XML header - tells programs this is XML
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    
    # Main tag with basic info as attributes
    lines.append(f'<schedule variant="{schedule["variant"]}" isu="{schedule["isu"]}" week="{schedule["week"]}">')
    
    # Add each day
    for day_name, events in schedule['days'].items():
        lines.append(f'  <day name="{day_name}">')
        
        # Add each event
        for event in events:
            lines.append('    <event>')
            
            # Add event details as separate tags
            for field, value in event.items():
                # Fix special characters that break XML
                safe_value = (
                    value.replace('&', '&amp;')   # & becomes &amp;
                    .replace('<', '&lt;')         # < becomes &lt;
                    .replace('>', '&gt;')         # > becomes &gt;
                    .replace('"', '&quot;')       # " becomes &quot;
                )
                lines.append(f'      <{field}>{safe_value}</{field}>')
                
            lines.append('    </event>')
            
        lines.append('  </day>')
    
    lines.append('</schedule>')
    
    return '\n'.join(lines)

if __name__ == '__main__':
    print("=== EXTRA TASK 3 (+20% of grade) ===")
    print("Converting binary to XML...")
    
    # Load from binary
    schedule_data = load_from_binary('schedule_503266_v82.bin')
    print("Loaded schedule from binary")
    
    # Convert to XML
    xml_text = make_xml_file(schedule_data)
    
    # Save as XML file
    with open('schedule_503266_v82.xml', 'w', encoding='utf-8') as file:
        file.write(xml_text)
        
    print("Saved as XML file: schedule_503266_v82.xml")
    
    # Show a bit of the XML
    print("\nFirst few lines of XML:")
    for line in xml_text.split('\n')[:8]:
        print(line)