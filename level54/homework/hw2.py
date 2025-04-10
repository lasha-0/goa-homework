def get_size(width, height, depth):
    surface_area = 2 * (width * height + height * depth + width * depth)
    volume = width * height * depth
    return [surface_area, volume]