import pygame
from sys import exit
from random import choice, randint

# Function to change the state of traffic lights based on time:
def traffic_lights_state(current_time, t0, dt, traffic_lights):
    north_light_state = "red"
    east_light_state= "red"
    west_light_state = "red"
    south_light_state = "red"

    # Conditions to change the state of the traffic lights according to time: (Subject to change) 
    if dt >= 0 and dt < (signals_loop//4):
        north_light_state = "green"
        screen.blit(traffic_lights["green_light_north"],(190, 410))
    elif dt == (signals_loop//4) or dt == ((signals_loop//4)*4): 
        north_light_state = "red"
        screen.blit(traffic_lights["yellow_light_north"],(190, 410))
    else:
        north_light_state = "red"
        screen.blit(traffic_lights["red_light_north"],(190, 410))
    
    if dt > (signals_loop//4) and dt < ((signals_loop//4)*2):
        east_light_state = "green"
        screen.blit(traffic_lights["green_light_east"],(190, 130))
    elif dt == ((signals_loop//4)*2) or dt == (signals_loop//4):
        east_light_state = "red"
        screen.blit(traffic_lights["yellow_light_east"],(190, 130))
    else:
        east_light_state = "red"
        screen.blit(traffic_lights["red_light_east"],(190, 130))

    if dt > ((signals_loop//4)*2) and dt < ((signals_loop//4)*3):
        south_light_state = "green"
        screen.blit(traffic_lights["green_light_south"],(450, 130))
    elif dt == ((signals_loop//4)*3) or dt == ((signals_loop//4)*2):
        south_light_state = "red"
        screen.blit(traffic_lights["yellow_light_south"],(450, 130))
    else:
        south_light_state = "red"
        screen.blit(traffic_lights["red_light_south"],(450, 130))
    
    if dt > ((signals_loop//4)*3) and dt < ((signals_loop//4)*4):
        west_light_state = "green"
        screen.blit(traffic_lights["green_light_west"],(470, 390))
    elif dt == ((signals_loop//4)*4) or dt == ((signals_loop//4)*3):
        west_light_state = "red"
        screen.blit(traffic_lights["yellow_light_west"],(470, 390))
    else:
        west_light_state = "red"
        screen.blit(traffic_lights["red_light_west"],(470, 390))
    
    return dt, north_light_state, west_light_state, east_light_state, south_light_state

# Function to move the vehicles towards North:
def vehicle_movement_north(vehicle_list, north_light_state):
    # Checking if vehicle_list is not empty:
    if vehicle_list:        
        # enumarate is used to iterate over the index and the object both:
        for idx, (vehicle_surface, vehicle_rect) in enumerate(vehicle_list):       
            if vehicle_rect.y > 400 and vehicle_rect.y < 435 and north_light_state == "red":
                # Just show a static picture of the vehicle:
                screen.blit(vehicle_surface, vehicle_rect)          
            else:
                # Move the vehicle up
                vehicle_rect.y -= 5
                
                # Check for collisions with other vehicles
                for other_idx, (other_surface, other_rect) in enumerate(vehicle_list):
                    # Checking if the current vehicle collides with any other vehicle in the list:
                    if idx != other_idx and vehicle_rect.colliderect(other_rect):
                        # Adjust the position to avoid overlap
                        if vehicle_rect.y < other_rect.y:
                            # This would be implemented if direction is South:
                            vehicle_rect.y = other_rect.y - vehicle_rect.height
                        else:
                            # This would be implemented if direction is North: 
                            vehicle_rect.y = other_rect.y + other_rect.height

                screen.blit(vehicle_surface, vehicle_rect)

        # List comprehension that removes the vehicles that have moved off the screen's dimensions:
        vehicle_list = [(vehicle_surface, vehicle_rect) for vehicle_surface, vehicle_rect in vehicle_list if vehicle_rect.y > -100]

        return vehicle_list
    else:
        return []

# Function to move vehicles towards South: (Comments are same as North)
def vehicle_movement_south(vehicle_list, south_light_state):
    if vehicle_list:
        for idx, (vehicle_surface, vehicle_rect) in enumerate(vehicle_list):
            if vehicle_rect.y > 160 and vehicle_rect.y < 175 and south_light_state == "red":
                screen.blit(vehicle_surface, vehicle_rect)
            else:
                # Move the vehicle down
                vehicle_rect.y += 5
                
                # Check for collisions with other vehicles
                for other_idx, (other_surface, other_rect) in enumerate(vehicle_list):
                    if idx != other_idx and vehicle_rect.colliderect(other_rect):
                        # Adjust the position to avoid overlap
                        if vehicle_rect.y < other_rect.y:
                            vehicle_rect.y = other_rect.y - vehicle_rect.height
                        else:
                            vehicle_rect.y = other_rect.y + other_rect.height

                screen.blit(vehicle_surface, vehicle_rect)

        # Remove vehicles that have moved off the screen
        vehicle_list = [(vehicle_surface, vehicle_rect) for vehicle_surface, vehicle_rect in vehicle_list if vehicle_rect.y < 800]

        return vehicle_list
    else:
        return []

# Function to move vehicles towards East:  (Comments are same as North)
def vehicle_movement_east(vehicle_list, east_light_state):
    if vehicle_list:
        for idx, (vehicle_surface, vehicle_rect) in enumerate(vehicle_list):
            if vehicle_rect.x > 210 and vehicle_rect.x < 230 and east_light_state == "red":
                screen.blit(vehicle_surface, vehicle_rect)
            else:
                # Move the vehicle to the right
                vehicle_rect.x += 5
                
                # Check for collisions with other vehicles
                for other_idx, (other_surface, other_rect) in enumerate(vehicle_list):
                    if idx != other_idx and vehicle_rect.colliderect(other_rect):
                        # Adjust the position to avoid overlap
                        if vehicle_rect.x < other_rect.x:
                            vehicle_rect.x = other_rect.x - vehicle_rect.width
                        else:
                            vehicle_rect.x = other_rect.x + other_rect.width

                screen.blit(vehicle_surface, vehicle_rect)

        # Remove vehicles that have moved off the screen
        vehicle_list = [(vehicle_surface, vehicle_rect) for vehicle_surface, vehicle_rect in vehicle_list if vehicle_rect.x < 900]

        return vehicle_list
    else:
        return []

# Function to move vehicles towards West:  (Comments are same as North)
def vehicle_movement_west(vehicle_list, west_light_state):
    if vehicle_list:
        for idx, (vehicle_surface, vehicle_rect) in enumerate(vehicle_list):
            if vehicle_rect.x > 460 and vehicle_rect.x < 495 and west_light_state == "red":
                screen.blit(vehicle_surface, vehicle_rect)
            else:
                # Move the vehicle to the left
                vehicle_rect.x -= 5
                
                # Check for collisions with other vehicles
                for other_idx, (other_surface, other_rect) in enumerate(vehicle_list):
                    if idx != other_idx and vehicle_rect.colliderect(other_rect):
                        # Adjust the position to avoid overlap
                        if vehicle_rect.x < other_rect.x:
                            vehicle_rect.x = other_rect.x - vehicle_rect.width
                        else:
                            vehicle_rect.x = other_rect.x + other_rect.width

                screen.blit(vehicle_surface, vehicle_rect)

        # Remove vehicles that have moved off the screen
        vehicle_list = [(vehicle_surface, vehicle_rect) for vehicle_surface, vehicle_rect in vehicle_list if vehicle_rect.x > -100]

        return vehicle_list
    else:
        return []

# Initializing all pygame modules:
pygame.init()

# Setting the dimensions of the simulation window:
screen = pygame.display.set_mode((800, 680))

# Naming our window: 
pygame.display.set_caption("Automated Traffic Signals")
 
clock = pygame.time.Clock()

# Background Image:
main_bg_surf = pygame.image.load("Images/main_bg.jpg").convert_alpha()

# Traffic Lights:
red_light = pygame.image.load("Images/red_light.png").convert_alpha()
yellow_light = pygame.image.load("Images/yellow_light.png").convert_alpha()
green_light = pygame.image.load("Images/green_light.png").convert_alpha()

traffic_lights = {
"red_light_north": pygame.transform.rotozoom(red_light, 0, 0.2),
"yellow_light_north": pygame.transform.rotozoom(yellow_light, 0, 0.2),
"green_light_north": pygame.transform.rotozoom(green_light, 0, 0.2),

"red_light_east": pygame.transform.rotozoom(red_light, -90, 0.2),
"yellow_light_east": pygame.transform.rotozoom(yellow_light, -90, 0.2),
"green_light_east": pygame.transform.rotozoom(green_light, -90, 0.2),

"red_light_south": pygame.transform.rotozoom(red_light, 180, 0.2),
"yellow_light_south": pygame.transform.rotozoom(yellow_light, 180, 0.2),
"green_light_south": pygame.transform.rotozoom(green_light, 180, 0.2),

"red_light_west": pygame.transform.rotozoom(red_light, 90, 0.2),
"yellow_light_west": pygame.transform.rotozoom(yellow_light, 90, 0.2),
"green_light_west": pygame.transform.rotozoom(green_light, 90, 0.2),
}

# Vehicles:
truck1_surf = pygame.image.load("Images/truck1.svg").convert_alpha()
truck2_surf = pygame.image.load("Images/truck2.svg").convert_alpha()
truck3_surf = pygame.image.load("Images/truck3.svg").convert_alpha()

vehicles = {
"car1_surf": pygame.image.load("Images/car1.svg").convert_alpha(),
"car2_surf": pygame.image.load("Images/car2.svg").convert_alpha(),
"car3_surf": pygame.image.load("Images/car3.svg").convert_alpha(),
"car4_surf": pygame.image.load("Images/car4.svg").convert_alpha(),
"truck1_surf": pygame.transform.rotozoom(truck1_surf, 180, 1),
"truck2_surf": pygame.transform.rotozoom(truck2_surf, 180, 1),
"truck3_surf": pygame.transform.rotozoom(truck3_surf, 180, 1),
}

t0 = 0
signals_loop = 40
signals_loop = signals_loop - (signals_loop % 4)

# Creating a custom event:
vehicle_timer = pygame.USEREVENT + 1
# Triggering the above event whenever this timer reaches 3500:
pygame.time.set_timer(vehicle_timer, 3500)

# Creating empty lists for every direction:
vehicle_rect_list_north = []
vehicle_rect_list_south = []
vehicle_rect_list_east = []
vehicle_rect_list_west = []

# Game loop:
while True:
    
    # Closes the window whenever user crosses it:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Checking if the event vehicle_timer is triggered or not:
        if event.type == vehicle_timer:

            # Randomly selecting a direction to spawn a vehicle:
            side_choice = choice(["north", "south", "east", "west"])

            # Randomly choosing a vehicle:
            vehicle_choice = choice(list(vehicles.values()))
            
            if side_choice == "north":
                # Rotating the image of the vehicle as per the need of direction:
                vehicle_choice_rotated = pygame.transform.rotozoom(vehicle_choice, -90, 1)
                # Creating a rectangle of the chosen vehicle and appending it in vehicle_rect_list_north:
                vehicle_rect_list_north.append((vehicle_choice_rotated, vehicle_choice_rotated.get_rect(midtop = (345, randint(700, 1000)), width = 200, height = randint(100, 110))))

            elif side_choice == "south":
                vehicle_choice_rotated = pygame.transform.rotozoom(vehicle_choice, 90, 1)
                vehicle_rect_list_south.append((vehicle_choice_rotated, vehicle_choice_rotated.get_rect(midbottom = (450, randint(-300, -50)), width = 200, height = randint(100, 110))))

            elif side_choice == "east":
                vehicle_choice_rotated = pygame.transform.rotozoom(vehicle_choice, 180, 1)
                vehicle_rect_list_east.append((vehicle_choice_rotated, vehicle_choice_rotated.get_rect(midright = (randint(-300, -50), 295), width = randint(110, 120), height = 200)))

            elif side_choice == "west":
                vehicle_choice_rotated = pygame.transform.rotozoom(vehicle_choice, 0, 1)
                vehicle_rect_list_west.append((vehicle_choice_rotated, vehicle_choice_rotated.get_rect(midleft = (randint(900, 1200), 390), width = randint(100, 110), height = 200)))

    # Displaying the four way crossing image in the background:
    screen.blit(main_bg_surf,(0,0))

    # Getting the current time of the loop running and dividing it by 1000 to convert from milliseconds to seconds:
    current_time = pygame.time.get_ticks() // 1000

    # Getting change in time since the last one:
    dt = current_time - t0

    # If the traffic lights loop is completed, setting t0 to current time so that we can calculate the time correctly next time:
    if dt > signals_loop:
        t0 = current_time
    
    dt, north_light_state, west_light_state, east_light_state, south_light_state = traffic_lights_state(current_time, t0, dt, traffic_lights)

    # Calling the vehicle_movement functions:
    vehicle_rect_list_north = vehicle_movement_north(vehicle_rect_list_north, north_light_state)
    vehicle_rect_list_south = vehicle_movement_south(vehicle_rect_list_south, south_light_state)
    vehicle_rect_list_east = vehicle_movement_east(vehicle_rect_list_east, east_light_state)
    vehicle_rect_list_west = vehicle_movement_west(vehicle_rect_list_west, west_light_state)
    
    # Updating the screen in every loop:
    pygame.display.update()
    # Setting the max FPS of the loop:
    clock.tick(60)