property locationName : "move" #name of your gpx filex

###########################
tell application "System Events"
    tell process "Xcode"
        click menu item locationName of menu 1 of menu item "Simulate Location" of menu 1 of menu bar item "Debug" of menu bar 1
    end tell
end tell
