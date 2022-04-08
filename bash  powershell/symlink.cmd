::for each subfolderfolder in folder
:: make symlink
set $folder = "F:\client_files" 
set $subfolderfolder="F:\client_files\*"
set $destination="J:\Hydrus Network\db\client_files\"
::for each subfolderfolder in folder
mklink /d $destination $subfolderfolder
