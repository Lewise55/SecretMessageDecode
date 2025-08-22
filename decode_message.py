import requests

def get_secret_message(google_doc_url: str):
    response = requests.get(google_doc_url)
    if response.status_code != 200:
        print("Failed to fetch document.")
        return

    content = response.text.strip().splitlines()
    
    grid_data = []
    max_x = max_y = 0

    for line in content:
        parts = line.strip().split()
        if len(parts) < 3:
            continue
        x, y, char = int(parts[0]), int(parts[1]), parts[2]
        grid_data.append((x, y, char))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in grid_data:
        grid[y][x] = char

    message = ''
    for row in grid:
        for c in row:
            if c.isupper():
                message += c

    print("Secret Message:", message)

