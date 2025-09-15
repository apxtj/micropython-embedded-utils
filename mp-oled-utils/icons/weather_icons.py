# weather_icons.py

def draw_icon_clear(oled, cx, cy):
    cx += -10; cy += -8
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            oled.pixel(cx + dx, cy + dy, 1)
    rays = [(6,0), (-6,0), (0,6), (0,-6), (4,4), (-4,4), (4,-4), (-4,-4)]
    for dx, dy in rays:
        oled.line(cx, cy, cx + dx, cy + dy, 1)

def draw_icon_clouds(oled, cx, cy):
    cx += -2
    oled.fill_rect(cx - 17, cy - 9, 12, 6, 1)
    oled.fill_rect(cx - 13, cy - 12, 10, 6, 1)
    oled.line(cx - 17, cy - 3, cx - 2, cy - 3, 1)

def draw_icon_rain(oled, cx, cy):
    cx += -2; cy += -4
    draw_icon_clouds(oled, cx, cy)
    oled.line(cx - 14, cy - 2, cx - 14, cy + 2, 1)
    oled.line(cx - 10, cy - 2, cx - 10, cy + 3, 1)
    oled.line(cx - 6, cy - 2, cx - 6, cy + 0, 1)

def draw_icon_drizzle(oled, cx, cy):
    cx += -2; cy += -4
    draw_icon_clouds(oled, cx, cy)
    oled.pixel(cx - 13, cy + 1, 1)
    oled.pixel(cx - 9, cy + 2, 1)
    oled.pixel(cx - 5, cy + 1, 1)

def draw_icon_thunderstorm(oled, cx, cy):
    cx += -2; cy += -4
    draw_icon_clouds(oled, cx, cy)
    oled.line(cx - 10, cy - 2, cx - 12, cy + 2, 1)
    oled.line(cx - 12, cy + 2, cx - 8, cy + 2, 1)
    oled.line(cx - 8, cy + 2, cx - 10, cy + 6, 1)

def draw_icon_snow(oled, cx, cy):
    cx += -2; cy += -4
    draw_icon_clouds(oled, cx, cy)
    oled.line(cx - 8, cy - 2, cx - 8, cy + 4, 1)
    oled.line(cx - 11, cy + 1, cx - 5, cy + 1, 1)
    oled.line(cx - 10, cy - 1, cx - 6, cy + 3, 1)
    oled.line(cx - 6, cy - 1, cx - 10, cy + 3, 1)

def draw_icon_mist(oled, cx, cy):
    cx += -10; cy += -8
    for i in range(-1, 2):
        y = cy + i * 3
        oled.line(cx - 7, y, cx + 7, y, 1)

def draw_weather_icon(oled, weather_condition, cx, cy):
    if weather_condition == 'Clear':
        draw_icon_clear(oled, cx, cy)
    elif weather_condition == 'Clouds':
        draw_icon_clouds(oled, cx, cy)
    elif weather_condition == 'Rain':
        draw_icon_rain(oled, cx, cy)
    elif weather_condition == 'Drizzle':
        draw_icon_drizzle(oled, cx, cy)
    elif weather_condition == 'Thunderstorm':
        draw_icon_thunderstorm(oled, cx, cy)
    elif weather_condition == 'Snow':
        draw_icon_snow(oled, cx, cy)
    elif weather_condition in ['Mist', 'Fog', 'Haze']:
        draw_icon_mist(oled, cx, cy)
    else:
        oled.text('?', cx - 14, cy - 12)

def clear_weather_icon_area(oled, cx, cy):
    oled.fill_rect(cx - 22, cy - 20, 40, 40, 0)
