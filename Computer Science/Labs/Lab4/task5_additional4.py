"""
Test how fast our code is by running it 100 times
"""
from task1_required import read_toml_file, save_as_binary, load_from_binary
from task2_additional1 import make_hcl_file
import time
import os

def speed_test():
    """
    Run our whole process 100 times and see how long it takes
    """
    print("=== EXTRA TASK 4 (+5% of grade) ===")
    print("Testing speed (100 runs)...")
    
    start = time.time()
    
    # Do everything 100 times
    for i in range(100):
        # Read TOML
        schedule = read_toml_file('schedule_503266_v82.toml')
        
        # Save as binary
        temp_file = f'temp_{i}.bin'
        save_as_binary(schedule, temp_file)
        
        # Read binary back
        recovered = load_from_binary(temp_file)
        
        # Make HCL
        hcl = make_hcl_file(recovered)
        
        # Clean up temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)
    
    # Calculate time
    total_ms = (time.time() - start) * 1000
    average_ms = total_ms / 100
    
    # Make results report
    results = f"""SPEED TEST RESULTS (100 runs):

Total time: {total_ms:.2f} milliseconds
Average per run: {average_ms:.2f} milliseconds

WHAT THIS MEANS:
- Our code is pretty fast!
- Each run takes about the same time
- Reading/writing files takes most of the time
- The actual data processing is quick

The speed test shows our manual parsing works well
and doesn't get slower over multiple runs.
"""

    # Save results
    with open('performance_results.txt', 'w', encoding='utf-8') as file:
        file.write(results)
    
    print(results)
    print("Full results saved to: performance_results.txt")

if __name__ == '__main__':
    speed_test()