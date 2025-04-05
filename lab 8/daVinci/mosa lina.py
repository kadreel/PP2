import pygame        #btw it's laggy. R = red, G = green, B = blue, V = eraser, space = circle/square, LMB/RMB = increase/decrease radius

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    clock = pygame.time.Clock()
    active = True
    bg = (0, 0, 0)
    
    font = pygame.font.SysFont('consolas', 20)
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    brush_shape = 'circle'  # default to circular brush
    eraser_mode = False  # flag for eraser mode
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
                if event.key == pygame.K_SPACE:
                    brush_shape = 'rectangle' if brush_shape == 'circle' else 'circle'
                if event.key == pygame.K_v:
                    eraser_mode = not eraser_mode
                if event.key == pygame.K_l:
                    eraser_radius = min(200, eraser_radius + 3)
                if event.key == pygame.K_k:
                    eraser_radius = max(1, eraser_radius - 3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and active == True:
                position = event.pos
                if not eraser_mode:
                    points = points + [position]
                    points = points[-512:]
                else:
                    points = [p for p in points if not is_point_near(p, position, eraser_radius)]
        
        screen.fill(bg)
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, brush_shape)
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
    
    if color_mode == 'blue':
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
        
        if brush_shape == 'circle':
            pygame.draw.circle(screen, color, (x, y), width)
        elif brush_shape == 'rectangle':
            pygame.draw.rect(screen, color, (x - width//2, y - width//2, width, width))
    

main()
