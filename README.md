Work in Gnome 3.38
U need to set only 1 argunet - folder with all u wallpapers.
Script try to detect current wallpaper in u wallpapers list and if found - set next if not found set first.
U can set script call in auto start or set by crontab

```
cp ./wallpapers-changer.desktop ~/.config/autostart/
chmod +x ~/.config/autostart/wallpapers-changer.desktop
```

```
cp ./changer.py /etc/changer.py
chmod +x /etc/changer.py
```

U also need to rename username to .desktop file
