import pyautogui
import time
import os
#created 7/25/25 by Wilson :)
class TextColors:
    red = "\u001b[0;31m"
    green = "\u001b[0;32m"
    yellow = "\u001b[0;33m"
    blue = "\u001b[0;34m"
    magenta = "\u001b[0;35m"
    cyan = "\u001b[0;36m"
    white = "\u001b[0;37m"
    underline = "\u001b[4m"
    bold = "\u001b[1m"
    inverse = "\u001b[7m"
    end = "\u001b[0m"
    bright_cyan = "\u001b[36;1m"
    bright_blue = "\u001b[34;1m"
    bright_magenta = "\u001b[95;1m"

t = TextColors
claim_chest_attempts = 10
endurance_count = 0
claimed_chest_counter = 0
uptime_start = time.time()
start_time = round(time.time())


def get_uptime():
    return time.time() - uptime_start

class main_screen:
    '''
    The First Cycle of the Twine Macro. This is what is used before you start loading into the game.
    
    Parameters:
        begin: Initializes the program, and allows some small customizable features. Less useful to the core functionality of the program.
        main_screen_actions: Completes all of the necessary main screen actions. (ex. Selecting Twine on the Map, Loading into Twine etc.)
        launch_and_load: Launches the Storm Shield with lots of customizability.
    '''
    def __init__(self, begin_time, buffer, name, mouse_speed, launch_countdown, pixel_x, pixel_y, pixel_r, pixel_g, pixel_b, tol):
        self.begin_time = begin_time
        self.buffer = buffer
        self.name = name
        self.mouse_speed = mouse_speed
        self.launch_countdown = launch_countdown
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y
        self.pixel_r = pixel_r
        self.pixel_g = pixel_g
        self.pixel_b = pixel_b
        self.tol = tol
        
        



    def begin(begin_time: int = 10, name: str = 'Wilson'):
        '''Initializes the program. 
        
        Arguments:
            begin_time: Time before the script begins in **seconds**. Default time is 10 seconds.
            name: Name of the person who creates this macro using these building blocks. Defaults to "Wilson".'''
        
        print(f"{t.cyan}Built by {t.bold}{name}{t.end}")
        time.sleep(2)
        os.system('cls')
        try:
            for x in range(begin_time, 0, -1):
                print(f"{t.bright_blue}Beginning in {t.end}{t.bright_cyan}{x}{t.end} {t.bright_blue}seconds.{t.end} {t.bright_magenta}(Ctrl + C to skip this loading.){t.end}")
                time.sleep(1)
                os.system('cls')
        except KeyboardInterrupt:
            os.system('cls')
            print(f"{t.bold}Skipped Loading.{t.end}")
            time.sleep(0.3)

    def main_screen_actions(buffer: int = 2, mouse_speed: float = 0.3,
                            map_x: int = 645, map_y: int = 103, tp_x: int = 1356, tp_y: int = 624,
                            enter_x: int = 1471, enter_y: int = 941, shb_x: int = 1218, shb_y: int = 796,
                            lhb_x: int = 1693, lhb_y: int = 905, launch_x: int = 1172, launch_y: int = 942
                            ):
        '''Completes all of the necessary main screen actions. (ex. Selecting Twine on the Map, Loading into Twine etc.)
        
        Arguments:
            buffer: Input a number to clarify the amount of time in **seconds** needed in between inputs. (Default is 2 seconds)
            mouse_speed: Input how fast you want the mouse to travel from point to point in **seconds**. (Default is 0.3 seconds) 
            map_x: X Value of the map button. (Default is 645)
            map_y: Y Value of the map button. (Default is 103)
            tp_x: X Value of the twine peaks pin. (Default is 1356)
            tp_y: Y Value of the twine peaks pin. (Default is 624)
            enter_x: X Value of the "Enter" button. (Default is 1471)
            enter_y: Y Value of the "Enter" button. (Default is 941)
            shb_x: X Value of the Twine Homebase. (Default is 1218)
            shb_y: Y Value of the Twine Homebase. (Default is 796)
            lhb_x: X Value of the loading homebase button. (Default is 1693)
            lhb_y: Y Value of the loading homebase button. (Default is 905)
            launch_x: X Value of the "Launch" button. (Default is 1172)
            launch_y: Y Value of the "Launch" button. (Default is 942)
            '''
        
        #create some x/y vars later, done 7/25/25

        try:
            os.system('cls')
            print(f"{t.green}{t.bold}Twine Wave 24 Macro Started!{t.end} 🌴⚡ {t.bright_magenta}(Ctrl + C to end macro at any time){t.end}")
            time.sleep(buffer)
            pyautogui.moveTo(map_x,map_y,mouse_speed)
            pyautogui.click(map_x,map_y)
            print("Map Pressed... 🗺️")
            time.sleep(buffer)
            pyautogui.moveTo(tp_x,tp_y,mouse_speed)
            pyautogui.click(tp_x,tp_y)
            print(f"{t.red}Twine Peaks Selected...{t.end}☠️")
            time.sleep(buffer)
            pyautogui.moveTo(enter_x,enter_y,mouse_speed)
            pyautogui.click(enter_x,enter_y)
            print("Entering Twine Peaks... 🌋")
            time.sleep(buffer)
            pyautogui.moveTo(shb_x,shb_y,mouse_speed)
            pyautogui.click(shb_x,shb_y)
            print("Selecting Homebase... 🏠")
            time.sleep(buffer)
            pyautogui.moveTo(lhb_x,lhb_y,mouse_speed)
            pyautogui.click(lhb_x,lhb_y)
            print("Loading Homebase... 🔃")
            time.sleep(buffer)
            pyautogui.moveTo(launch_x,launch_y,mouse_speed)
            pyautogui.click(launch_x,launch_y)
            print(f"{t.green}Launching Zone...{t.end}✅")
            time.sleep(buffer)
        except KeyboardInterrupt:
            os.system('cls')
            print(f"{t.bold}Skipped Loading.{t.end}")
            time.sleep(0.3)

    def launch_and_load(launch_countdown: int = 10, pixel_x: int = 1742, pixel_y: int = 872, pixel_r: int = 239, pixel_g: int = 218, pixel_b: int = 0, tol: int = 10):
        '''
        Handles launching and loading into the game. 

        Arguments:
            launch_countdown (Launch Countdown): Sends a countdown in **seconds** before clicking on the launch button. (Default is 10 seconds.)
            pixel_x (X Coordinate): **X** coordinate to click on. (Default is 1742).
            pixel_y (Y Coordinate): **Y** coordinate to click on. (Default is 872).
            pixel_r (Red Pixel): **Red** color value on pixel (x,y), works from 0-255. (Default is 239).
            pixel_g (Green Pixel): **Green** color value on pixel (x,y), works from 0-255. (Default is 218).
            pixel_b (Blue Pixel): **Blue** color value on pixel (x,y), works from 0-255. (Default is 0).
            tol (***tolerance***): Range of colors that it can go up/down by. (ex.) If a color is 100 and tolerance is 5, it can search from 95-105. Default is 10).
        '''
        os.system('cls')
        try:
            for x in range(launch_countdown, 0, -1):
                print(f"{t.green}{t.bold}Found!{t.end}")
                print(f"{t.yellow}{t.underline}Launching into homebase in {x} second(s)...{t.end}")
                time.sleep(1)
                os.system('cls')
        except KeyboardInterrupt:
            os.system('cls')
            print(f"{t.bold}Skipped Launch Wait.{t.end}")
            time.sleep(0.3)
        try:
            while True:
                    if pyautogui.pixelMatchesColor(pixel_x, pixel_y, (pixel_r, pixel_g, pixel_b), tolerance=tol):
                        pyautogui.moveTo(pixel_x, pixel_y)
                        pyautogui.click(pixel_x, pixel_y)
                        break
                    else:
                        os.system('cls')
                        print(f"{t.blue}Waiting for pixel.{t.end}")
                        time.sleep(0.4)
                        os.system('cls')
                        print(f"{t.blue}Waiting for pixel..{t.end}")
                        time.sleep(0.4)
                        os.system('cls')
                        print(f"{t.blue}Waiting for pixel...{t.end}")
                        time.sleep(0.4)
        except KeyboardInterrupt:
            os.system('cls')
            print(f"{t.bold}Halted pixel search in launch function.{t.end}")
            time.sleep(0.3)

class in_game:
    '''
    The Second Cycle of the Twine Macro. This is what is used when you load into the game and tracks data throughout the game.
    '''
    def __init__(self, wait_time, move_left, move_up, console_buffer, con_x1, con_x2, con_y1, con_y2, interact, pixel_x, pixel_y, pixel_r, pixel_g, pixel_b, tol):
        self.wait_time = wait_time
        self.move_left = move_left
        self.move_up = move_up
        self.console_buffer = console_buffer
        self.con_x1 = con_x1
        self.con_x2 = con_x2
        self.con_y1 = con_y1
        self.con_y2 = con_y2
        self.interact = interact
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y
        self.pixel_r = pixel_r
        self.pixel_g = pixel_g
        self.pixel_b = pixel_b
        self.tol = tol
    
    def move_to_console(wait_time: int = 30, move_left: str = 'a', move_up: str = 'w', interact: str = 'e', console_buffer: int = 3, pixel_x: int = 259, pixel_y: int = 993, pixel_r: int = 110, pixel_g: int = 216, pixel_b: int = 75, tol: int = 10, con_x1: int = 666, con_y1: int = 609, con_x2: int = 950, con_y2: int = 785):
        '''Handles detecting when you load into the game and moving towards the console and beginning the endurance.
        
        Arguments:
            wait_time (Wait Time): Waiting buffer in **seconds** right after loading to prevent lag. (Default value is 30 seconds).
            move_left (Move Left): Keybind used for moving left. (Default is 'a').
            move_up (Move Forward): Keybind used for moving forward. (Default is 'w').
            interact (Interact): Keybind used for interacting. (Default is 'e').
            console_buffer (Console Buffer): Handles buffers in **seconds** inside of the console. (Default is 3 seconds).
            pixel_x (X Coordinate): **X** coordinate to click on. (Default is 1742).
            pixel_y (Y Coordinate): **Y** coordinate to click on. (Default is 872).
            pixel_r (Red Pixel): **Red** color value on pixel (x,y), works from 0-255. (Default is 239).
            pixel_g (Green Pixel): **Green** color value on pixel (x,y), works from 0-255. (Default is 218).
            pixel_b (Blue Pixel): **Blue** color value on pixel (x,y), works from 0-255. (Default is 0).
            tol (***tolerance***): Range of colors that it can go up/down by. (ex.) If a color is 100 and tolerance is 5, it can search from 95-105. Default is 10).
            con_x1 (Console X [1]): X value of the first part of the storm shield console. (Default is 666).
            con_y1 (Console Y [1]): Y value of the first part of the storm shield console. (Default is 609).
            con_x2 (Console X [2]): X value of the second part of the storm shield console. (Default is 950).
            con_y2 (Console Y [2]): Y value of the second part of the storm shield console. (Default is 785).
        '''
        try:
            while True:
                if pyautogui.pixelMatchesColor(pixel_x, pixel_y, (pixel_r, pixel_g, pixel_b), tolerance=tol):
                    os.system('cls')
                    print(f"{t.green}{t.bold}Entered Homebase!{t.end}")
                    time.sleep(2)
                    os.system('cls')
                    for x in range(wait_time, 0, -1):
                        print(f"{t.red}{t.bold}Waiting {x}s to avoid possible lag.{t.end} ")
                        time.sleep(1)
                        os.system('cls')
                    print(f"Moving to console... 🏃‍♂️💨")
                    pyautogui.keyDown(move_left)
                    time.sleep(4.4)
                    pyautogui.keyUp(move_left)
                    time.sleep(0.2)
                    pyautogui.keyDown(move_up)
                    time.sleep(1.5)
                    pyautogui.keyUp(move_up)
                    time.sleep(2)  
                    os.system('cls')
                    print("Arrived At Console... 👍")

                    pyautogui.keyDown(interact)
                    time.sleep(console_buffer)
                    pyautogui.keyUp(interact)
                    time.sleep(console_buffer)
                    pyautogui.moveTo(con_x1, con_y1)
                    pyautogui.click(con_x1, con_y1)
                    time.sleep(console_buffer)
                    pyautogui.moveTo(con_x2, con_y2)
                    pyautogui.click(con_x2, con_y2)

                    print(f"{t.green}Endurance Started!{t.end} 😎")
                    time.sleep(5)
                    break
                else:
                    print(f"{t.bold}Launching.{t.end}")
                    time.sleep(0.4)
                    os.system('cls')
                    print(f"{t.bold}Launching..{t.end}")
                    time.sleep(0.4)
                    os.system('cls')
                    print(f"{t.bold}Launching...{t.end}")
                    time.sleep(0.4)
                    os.system('cls')
        except KeyboardInterrupt:
            os.system('cls')
            print(f"{t.bold}Halted pixel search in console function.{t.end}")
            time.sleep(0.3)

    def endurance_wait_reset(claim_buffer: int = 2,
            pixel_x1: int = 1, pixel_y1: int = 85, pixel_r1: int = 81, pixel_g1: int = 150, pixel_b1: int = 220, tol_1: int = 10,
            pixel_x2: int = 956, pixel_y2: int = 966, pixel_r2: int = 22, pixel_g2: int = 27, pixel_b2: int = 45, tol_2: int = 10,
            pixel_x3: int = 1654, pixel_y3: int = 1045, pixel_r3: int = 134, pixel_g3: int = 138, pixel_b3: int = 159, tol_3: int = 10,
            net_x: int = 974, net_y: int = 387, net_r: int = 255, net_g: int = 69, net_b: int = 39, net_tol: int = 5, net_byp_x: int = 990, net_byp_y: int = 650
            ):
        
        '''Has various x/y/tolerance coordinates for various different things.
        
        
        Arguments:
            pixel_x1: X Value to track if an endurance has been completed or not. By default scans a blue pixel in the main screen. (Default is 1)
            pixel_y1: Y Value to track if an endurance has been completed or not. By default scans a blue pixel in the main screen. (Default is 85)
            pixel_r1: Red Value for tracking if an endurance has been completed. (Default is 81)
            pixel_g1: Green Value for tracking if an endurance has been completed. (Default is 150)
            pixel_b1: Blue Value for tracking if an endurance has been completed. (Default is 220)
            tol_1: Tolerance value for tracking if an endurance has been completed. (Default is 10)
            pixel_x2: X Value to check for the chest claim button. By default scans a blue pixel in the main screen. (Default is 956)
            pixel_y2: Y Value to check for the chest claim button. By default scans a blue pixel in the main screen. (Default is 966)
            pixel_r2: Red Value for checking for the chest claim button. (Default is 22)
            pixel_g2: Green Value for checking for the chest claim button. (Default is 27)
            pixel_b2: Blue Value for checking for the chest claim button. (Default is 45)
            tol_2: Tolerance value for checking for the chest claim button. (Default is 10)
            pixel_x3: X Value to check for the chest claim all button. By default scans a blue pixel in the main screen. (Default is 1654)
            pixel_y3: Y Value to check for the chest claim all button. By default scans a blue pixel in the main screen. (Default is 1045)
            pixel_r3: Red Value for checking for the claim all claim button. (Default is 134)
            pixel_g3: Green Value for checking for the claim all claim button. (Default is 138)
            pixel_b3: Blue Value for checking for the claim all claim button. (Default is 159)
            tol_3: Tolerance value for checking for the claim all claim button. (Default is 5)
            net_x: X Value to track if the network has disconnected. (Default is 974)
            net_y: Y Value to track if the network has disconnected. (Default is 384)
            net_r: Red Value for checking if the network has disconnected. (Default is 255)
            net_g: Green Value for checking if the network has disconnected. (Default is 69)
            net_b: Blue Value for checking if the network has disconnected. (Default is 39)
            net_tol: Tolerance value for checking if the network has disconnected. (Default is 5)
            net_byp_x: X Value to bypass the network disconnect screen. (Default is 990)
            net_byp_y: Y Value to bypass the network disconnect screen. (Default is 650)
        '''

        global endurance_count
        global claimed_chest_counter
        global start_time

        uptime = time.time() - uptime_start
        try:
            while True:
                if pyautogui.pixelMatchesColor(pixel_x1, pixel_y1, (pixel_r1, pixel_g1, pixel_b1), tolerance=tol_1):
                    endurance_count += 1
                    print(f"{t.magenta}{t.bold}Endurance Finished! Beginning restart now...{t.end}")
                    time.sleep(5)
                    break
                else:
                    os.system('cls')
                    wave = 0
                    current_time = time.time()
                    elapsed = current_time - start_time
                    print(f"{t.cyan}Built by {t.bold}Wilson{t.end}")
                    print(f"\n{t.blue}Endurances Done:{t.end} {t.cyan}{endurance_count}{t.end}")
                    print(f"{t.blue}Time Elapsed:{t.end} {t.cyan}{get_uptime()}s{t.end}")
                    thresholds = [170, 377, 599, 821, 1043, 1265, 1487, 1709, 1936, 2168, 2405, 2657, 2924, 3206, 3488, 3770, 4052, 4349, 4661, 4988, 5330, 5672, 6014, 6356, 6713, 7085, 7487, 7889, 8291, 8693]
                    elapsed = current_time - start_time
                    wave = next((i+1 for i, t in enumerate(thresholds) if elapsed <= t), "Error 1: Wave Overflow Error.")
                    print(f"{t.bright_blue}Wave:{t.end} {t.bright_cyan}{wave}{t.end}" if isinstance(wave, int) else wave)
                    print(f"{t.magenta}{t.underline}Claimed Chest Counter:{t.end}{t.bright_magenta} {claimed_chest_counter}{t.end}")
                    print(f"{t.green}Checking for Chests... 📦{t.end}") #chest
                    for x in range(claim_chest_attempts):
                        if pyautogui.pixelMatchesColor(pixel_x2, pixel_y2, (pixel_r2, pixel_g2, pixel_b2), tolerance=tol_2):
                            return False
                        
                        pyautogui.moveTo(pixel_x2, pixel_y2, claim_buffer)
                        pyautogui.click(pixel_x2, pixel_y2)
                        time.sleep(3)

                        if pyautogui.pixelMatchesColor(pixel_x3, pixel_y3, (pixel_r3, pixel_g3, pixel_b3), tolerance=tol_3):
                            return False
                        
                        pyautogui.moveTo(pixel_x3, pixel_y3, claim_buffer)
                        pyautogui.click(pixel_x3, pixel_y3)
                        print(f"{t.green}{t.bold}Chest Claimed! ✅{t.end}")
                        claimed_chest_counter += 1
                        time.sleep(3)

                        if pyautogui.pixelMatchesColor(pixel_x1, pixel_y1, (pixel_r1, pixel_g1, pixel_b1), tolerance=tol_1):
                            return True
                        
                        print(f"{t.green}{t.bold}All rewards claimed!{t.end}")
                        print(f"Total Chests Claimed: {claimed_chest_counter}")
                        time.sleep(1.7)

                        return claimed_chest_counter > 0
                    if pyautogui.pixelMatchesColor(net_x, net_y, (net_r, net_g, net_b), net_tol): #network
                        print(f"Network Status: {t.red}Network Down{t.end}")
                        time.sleep(1)
                        pyautogui.moveTo(net_byp_x, net_byp_y)
                        pyautogui.click(net_byp_x, net_byp_y)
                    else:
                        print(f"Network Status: {t.green}Network Up{t.end}")

                    time.sleep(1)
        except KeyboardInterrupt:
            os.system('cls')
            print(f"{t.bold}Halted pixel search in wait function.{t.end}")
            time.sleep(0.3)
