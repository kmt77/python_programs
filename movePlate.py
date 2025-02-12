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
pygame.display.set_caption("Drag the Plate")

# Plate Initial Position
plate_x, plate_y = (WIDTH // 2 - PLATE_WIDTH // 2, HEIGHT // 2 - PLATE_HEIGHT // 2)
dragging = False  # Track whether the plate is being dragged
offset_x, offset_y = 0, 0  # Offset from the mouse position

# Game Loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit on close

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Check if mouse is inside the plate
            if plate_x <= mouse_x <= plate_x + PLATE_WIDTH and plate_y <= mouse_y <= plate_y + PLATE_HEIGHT:
                dragging = True
                offset_x = plate_x - mouse_x
                offset_y = plate_y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False  # Stop dragging on release

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                # Move plate with maintained offset
                mouse_x, mouse_y = event.pos
                plate_x = mouse_x + offset_x
                plate_y = mouse_y + offset_y

    # Draw the plate
    pygame.draw.rect(screen, BLUE, (plate_x, plate_y, PLATE_WIDTH, PLATE_HEIGHT))

    pygame.display.flip()  # Update display
    pygame.time.delay(10)  # Small delay for smooth movement

pygame.quit()
