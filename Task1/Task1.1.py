import time
import os

# for illustration
"""

 -- a --
|       |
f       b
|       |
 -- g --
|       |
e       c
|       |
 -- d ---

"""""
def clear_screen():
    #if your system is Linux or MacOS, replace 'cls' with 'clear'
    os.system('cls' )


def display_gear(gear_number):
    # check for valid gear number
    if not 0 <= gear_number <= 8:
        print(f"Invalid gear number: {gear_number}. Please use 0-8.")
        return
    # each true or false refers to a segment of the gear that will be on 
    segments = {
        0: [True, True, True, True, True, True, False],
        1: [False, True, True, False, False, False, False],
        2: [True, True, False, True, True, False, True],
        3: [True, True, True, True, False, False, True],
        4: [False, True, True, False, False, True, True],
        5: [True, False, True, True, False, True, True],
        6: [True, False, True, True, True, True, True],
        7: [True, True, True, False, False, False, False],
        8: [True, True, True, True, True, True, True]
    }
    # get all we need as segments 

    active_segments = segments.get(gear_number, [])
    grid = [[' ' for _ in range(4)] for _ in range(5)]
    # handle active segments
    if active_segments[0]: grid[0] = ['#'] * 4                     # Top (A)
    if active_segments[1]: 
        for row in range(1, 3): grid[row][3] = '#'                 # Upper-right (B)
    if active_segments[2]: 
        for row in range(3, 5): grid[row][3] = '#'                 # Lower-right (C)
    if active_segments[3]: grid[4] = ['#'] * 4                     # Bottom (D)
    if active_segments[4]: 
        for row in range(3, 5): grid[row][0] = '#'                 # Lower-left (E)
    if active_segments[5]: 
        for row in range(1, 3): grid[row][0] = '#'                 # Upper-left (F)
    if active_segments[6]: grid[2] = ['#'] * 4                     # Middle (G)

    return grid

def animate_shift_row_by_row(from_gear, to_gear, row_delay=0.2):
    
    clear_screen()
    from_grid = display_gear(from_gear)
    to_grid = display_gear(to_gear)

    print(f"Shifting from Gear {from_gear} to Gear {to_gear}:\n")

    # for visual effect
    for row in from_grid:
        print(''.join(row))
    time.sleep(1)  

    
    for i in range(5):
        clear_screen()
        print(f"Shifting from Gear {from_gear} to Gear {to_gear}:\n")
        
        
        for j in range(5):
            if j <= i:
                print(''.join(to_grid[j]))
            else:
                print(''.join(from_grid[j]))
        
        time.sleep(row_delay)  

    
    clear_screen()
    print(f"Gear {to_gear}:\n")
    for row in to_grid:
        print(''.join(row))

def main():
    try:
        from_gear = int(input("Enter starting gear (0-8): "))
        to_gear = int(input("Enter target gear (0-8): "))
        if 0 <= from_gear <= 8 and 0 <= to_gear <= 8:
            animate_shift_row_by_row(from_gear, to_gear)
        else:
            print("Gear numbers must be between 0 and 8.")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()