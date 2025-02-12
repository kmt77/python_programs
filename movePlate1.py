import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLATE_WIDTH, PLATE_HEIGHT = 150, 50
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag the Plate (Timer-Based)")

# Plate Initial Position
plate_x, plate_y = (WIDTH // 2 - PLATE_WIDTH // 2, HEIGHT // 2 - PLATE_HEIGHT // 2)
dragging = False  # Track if plate should move
offset_x, offset_y = 0, 0  # Store initial offset

# Timer Setup (Runs every 10ms)
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 10)

# Game Loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit on close

        elif event.type == TIMER_EVENT:
            # Check if the left mouse button is pressed
            mouse_pressed = pygame.mouse.get_pressed()[0]  # [0] is left button
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Get current mouse position

            if mouse_pressed:
                if not dragging:
                    # If just clicked, check if inside the plate and start dragging
                    if plate_x <= mouse_x <= plate_x + PLATE_WIDTH and plate_y <= mouse_y <= plate_y + PLATE_HEIGHT:
                        dragging = True
                        offset_x = plate_x - mouse_x
                        offset_y = plate_y - mouse_y

                if dragging:
                    # Update plate position with offset
                    plate_x = mouse_x + offset_x
                    plate_y = mouse_y + offset_y
            else:
                dragging = False  # Stop dragging when mouse is released

    # Draw the plate
    pygame.draw.rect(screen, BLUE, (plate_x, plate_y, PLATE_WIDTH, PLATE_HEIGHT))

    pygame.display.flip()  # Update display

pygame.quit()
