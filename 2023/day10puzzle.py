from collections import deque
from PIL import Image, ImageDraw

def create_image(input):
    input_grid = [list(line.strip()) for line in input]
    width, height = len(input_grid[0]), len(input_grid)
    image = Image.new('RGB', (width * 10, height * 10), "black")
    draw = ImageDraw.Draw(image)

    for y, row in enumerate(input_grid):
        for x, cell in enumerate(row):
            draw_pipe(draw, x, y, cell)
            if cell == 'S':
                start_position = (x, y)
    return image, start_position

def draw_pipe(draw, x, y, pipe_type):
    # Define the cell size and the cell's coordinates
    cell_size = 10
    top_left = (x * cell_size, y * cell_size)
    bottom_right = (x * cell_size + cell_size, y * cell_size + cell_size)
    center = (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2)
    center_top = (center[0], top_left[1])
    center_bottom = (center[0], bottom_right[1])
    left_center = (top_left[0], center[1])
    right_center = (bottom_right[0], center[1])


    if pipe_type == '|':
        draw.line([center_top, center_bottom], fill='white')
    elif pipe_type == '-':
        draw.line([left_center, right_center], fill='white')
    elif pipe_type == 'L':
        draw.line([center_top, center, right_center], fill='white')
    elif pipe_type == 'J':
        draw.line([center_top, center, left_center], fill='white')
    elif pipe_type == '7':
        draw.line([center_bottom, center, left_center], fill='white')
    elif pipe_type == 'F':
        draw.line([center_bottom, center, right_center], fill='white')
    elif pipe_type == 'S':
        draw.line([center_bottom, center_top, center, right_center, left_center], fill='white') # kinda hardcoded based, could have gone wrong but works

def flood_fill_image(pil_image, start_position):
    editable_image = pil_image.convert("RGB")
    fill_color = (255, 0, 0) 
    fill_position = (start_position[0] * 10 + 5, start_position[1] * 10 + 5)  # Adjusting for the cell size
    ImageDraw.floodfill(editable_image, xy=fill_position, value=fill_color)

    return editable_image

def bfs_max_distance(image, start_position):
    cell_size = 10  # Size of each cell in the image
    width, height = image.size
    visited = set()
    queue = deque([(start_position[0]*cell_size+5, start_position[1]*cell_size+5, 0)])  # (x, y, distance)

    max_distance = 0
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) in visited or not (0 <= x < width and 0 <= y < height):
            continue

        visited.add((x, y))

        if image.getpixel((x, y)) != (255, 0, 0):  # Skip non-filled pixels
            continue

        max_distance = max(max_distance, dist)

        # Add neighboring pixels to the queue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            queue.append((x + dx, y + dy, dist + 1))

    # Scale down the distance to grid cell units
    return max_distance // cell_size  # scaling down to original size

def fill_outside(grid, fill_char='O'):
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    def fill(x, y):
        if not (0 <= x < width and 0 <= y < height) or grid[y][x] in ['|', '-', 'L', 'J', '7', 'F', 'S']:
            return
        grid[y][x] = fill_char
        fill(x + 1, y)
        fill(x - 1, y)
        fill(x, y + 1)
        fill(x, y - 1)

    fill(0, 0)  # Start filling from the top-left corner

def count_enclosed_cells(grid):
    # Count all cells that are not marked by the fill and are not part of the main loop
    return sum(cell not in ['|', '-', 'L', 'J', '7', 'F', 'S', 'x'] for row in grid for cell in row)

def mark_main_loop(grid, filled_image, cell_size):
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            pixel_x, pixel_y = x * cell_size + cell_size // 2, y * cell_size + cell_size // 2
            if filled_image.getpixel((pixel_x, pixel_y)) == (255, 0, 0):  # Red, the fill color
                grid[y][x] = 'L'  # Marking loop cells with 'L'

if __name__ == "__main__":
    with open("2023/day10input.txt") as f:
        input = f.readlines()
        image, start_position = create_image(input)
        image.show()
        filled_image = flood_fill_image(image, start_position)
        filled_image.show()
        max_dist = bfs_max_distance(filled_image, start_position)
        print(f"Maximum distance from starting position: {max_dist}")
        grid = [list(line.strip()) for line in input]
        mark_main_loop(grid, filled_image, 10)
        fill_outside(grid)
        enclosed_cells = count_enclosed_cells(grid)
        print(f"Number of cells enclosed by the loop: {enclosed_cells}")
