import pygame        #btw it's laggy. R = red, G = green, B = blue, V = eraser, space = circle/square, LMB/RMB = increase/decrease radius, 1-4 = shapes
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    clock = pygame.Clock()
    active = True
    bg = (0, 0, 0)
    
    font = pygame.font.SysFont('consolas', 20)
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    brush_shape = 'circle'                                                  #DEFAULT CIRCLES
    eraser_mode = False
    eraser_radius = 30
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_LCTRL:
                    active = not active
                if event.key == pygame.K_SPACE and brush_shape == 'circle':
                    brush_shape = 'rectangle'
                else:
                    brush_shape = 'circle'
                if event.key == pygame.K_v:
                    eraser_mode = not eraser_mode                                       #KEYS FOR SWITCHING AROUND
                if event.key == pygame.K_1:
                    brush_shape = 'right_triangle'
                if event.key == pygame.K_2:
                    brush_shape = 'equilateral_triangle'
                if event.key == pygame.K_3:
                    brush_shape = 'rhombus'
                if event.key == pygame.K_4:
                    brush_shape = 'square'
                print(brush_shape)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and eraser_mode == False:
                    radius = min(200, radius + 1)
                elif event.button == 3 and eraser_mode == False:                            #BRUSH SIZES, BOTH DRAWING AND ERASING
                    radius = max(1, radius - 1)
                elif event.button == 1 and eraser_mode == True:
                    eraser_radius = min(200, eraser_radius + 1)
                elif event.button == 3 and eraser_mode == True:
                    eraser_radius = max(1, eraser_radius - 1)
            
            if event.type == pygame.MOUSEMOTION and active == True:
                position = event.pos
                if not eraser_mode:
                    points = points + [position]
                    points = points[-512:]
                else:
                    points = [p for p in points if not is_point_near(p, position, eraser_radius)]
        
        screen.fill(bg)
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, brush_shape)                                     #draw.
            i += 1

        if eraser_mode:
            text = f"Eraser radius: {eraser_radius}"
        else:
            text = f"Brush radius: {radius}"
        radii = font.render(f'{text}', True, (255, 255, 255))
        screen.blit(radii, (10, 10))

        pygame.display.flip()
        
        clock.tick(60)

def is_point_near(point, mouse_position, radius):
    return abs(point[0] - mouse_position[0]) < radius and abs(point[1] - mouse_position[1]) < radius

def drawLineBetween(screen, index, start, end, width, color_mode, brush_shape):
    c1 = max(0, min(255, 2 * index // 2 - 256))
    c2 = max(0, min(255, 2 * index // 2))
    
    if color_mode == 'blue':                                    #colors.
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        
        if brush_shape == 'circle':                                                         #IF MODE, THEN DO THAT MODE
            pygame.draw.circle(screen, color, (x, y), width)
        elif brush_shape == 'rectangle':
            pygame.draw.rect(screen, color, (x - width//2, y - width//2, width, width * 2))
        elif brush_shape == 'square':
            pygame.draw.rect(screen, color, (x - width//2, y - width//2, width, width))
        elif brush_shape == 'right_triangle':
            draw_right_triangle(screen, color, (x, y), width)
        elif brush_shape == 'equilateral_triangle':
            draw_equilateral_triangle(screen, color, (x, y), width)
        elif brush_shape == 'rhombus':
            draw_rhombus(screen, color, (x, y), width)

def draw_right_triangle(screen, color, center, size):                           #WEIRD SHAPES DEFS
    points = [
        (center[0], center[1] - size // 2),
        (center[0], center[1] + size // 2),
        (center[0] + size, center[1] + size // 2),
    ]
    pygame.draw.polygon(screen, color, points)

def draw_equilateral_triangle(screen, color, center, size):
    height = math.sqrt(3) * size / 2
    points = [
        (center[0], center[1] - height / 2),
        (center[0] - size / 2, center[1] + height / 2),
        (center[0] + size / 2, center[1] + height / 2),
    ]
    pygame.draw.polygon(screen, color, points)

def draw_rhombus(screen, color, center, size):
    half_diag1 = size
    half_diag2 = size
    points = [
        (center[0] - half_diag1 // 2, center[1]),
        (center[0], center[1] - half_diag2 // 2),
        (center[0] + half_diag1 // 2, center[1]),
        (center[0], center[1] + half_diag2 // 2),
    ]
    pygame.draw.polygon(screen, color, points)

main()
