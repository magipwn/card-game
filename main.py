import pygame
import sys

def main():
    pygame.init()
    # Create window
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Basic Card Game")
    #Load sprite image (replace 'test.png' with your image file)
    try:
        sprite = pygame.image.load("card.png").convert_alpha()
    except pygame.error as e:
        print(f"Failed to load image: {e}")
    # Sprite position
    sprite_pos = (150, 200)
    #clock
    clock = pygame.time.Clock()
    running = True
    facingLeft = False
    facingRight = False
    walkCount = 0
    # mouse poperties
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Define rectangle dimensions
    mouseWidth = 100
    mouseHeight = 100
    mouse_rect = pygame.Rect(mouse_x, mouse_y, mouseWidth, mouseHeight)
    def draw_rect_at_mouse():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Create rectangle object (Pygame's Rect)
        mouse_rect = pygame.Rect(mouse_x - mouseWidth // 2, mouse_y - mouseHeight // 2, mouseWidth, mouseHeight)
        # Draw the rectangle
        pygame.draw.rect(screen, (255, 0, 0), mouse_rect)  # Red color
          # ... (Other drawing, update display) ...
    # Calculate top-left position to center sprite on sprite position
        sprite_rect = sprite.get_rect()
        sprite_pos = (mouse_x - sprite_rect.width // 2, mouse_y - sprite_rect.height // 2)

    while running:

        isMouseClicked:bool = pygame.mouse.get_pressed()[0]
        # Fill screen background
        screen.fill((50, 50, 50))
        
        
        
        

        sprite_rect = sprite.get_rect()
        
        for event in pygame.event.get():
               if isMouseClicked == True:
                    draw_rect_at_mouse()
                    if pygame.Rect.colliderect(mouse_rect, sprite_rect) == True:
                        
                        sprite_pos = (mouse_x - sprite_rect.width // 2, mouse_y - sprite_rect.height // 2)
                        
                        
               if event.type == pygame.MOUSEMOTION:
                    draw_rect_at_mouse()
               if event.type == pygame.QUIT:
                    running = False

        
                    
        # Draw sprite at position only if mouse is pressed and mouserect and spriterect collides
        screen.blit(sprite, sprite_pos)
        # Update display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
