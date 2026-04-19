# UDE Configuration Files Explanation

The **Unified Desktop Environment (UDE)** is highly configurable through the use of `.conf` files. These configuration files control the appearance and behavior of your desktop environment, including themes, taskbar settings, and time-based theme switching.

## `ude-config.conf`

This is the primary configuration file for UDE. It contains the settings for the general appearance of the desktop, taskbar, and desktop customization.

### Sections in `ude-config.conf`

1. **General Settings**

```ini
[general]
default_theme = "light-theme"
enable_time_based_theme_switch = true
default_theme: Specifies the theme to use when no time-based switching is enabled.
enable_time_based_theme_switch: If set to true, UDE will switch themes automatically based on time.
Taskbar Settings
[taskbar]
color = "#FFEB3B"
orientation = "bottom"
icon_placement = "center"
color: Specifies the color of the taskbar.
orientation: Specifies where the taskbar is placed (top, bottom, left, right).
icon_placement: Specifies where icons are placed on the taskbar (left, center, right).
Desktop Settings
[desktop]
background_color = "#FFFFFF"
background_image = "/path/to/image.jpg"
background_color: The background color of the desktop.
background_image: The path to an image to set as the desktop wallpaper.
Time-Based Theme Switching
[themes]
morning_theme = "light-theme"
afternoon_theme = "neutral-theme"
evening_theme = "dark-theme"
morning_start_time = "06:00"
morning_theme, afternoon_theme, evening_theme: Specifies which theme to use at different times of the day.
morning_start_time, afternoon_start_time: Time when the theme should change (24-hour format).
time-based-config.conf

This file contains the specific settings for time-based theme switching. You can define the exact time frames for morning, afternoon, evening, and night themes.

Example configuration:

morning_theme = "light-theme"
afternoon_theme = "neutral-theme"
evening_theme = "dark-theme"
morning_start = "06:00"
afternoon_start = "12:00"
evening_start = "18:00"
night_start = "00:00"
