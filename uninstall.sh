sudo echo
echo installing movie episode utility

export APP=movie-episode-utility
export APP_DIR="/usr/share"
sudo rm -r "$APP_DIR/$APP"

export APP_ENTRY=episode-utility
export APP_ENTRY_DIR="/usr/bin"
sudo rm "$APP_ENTRY_DIR/$APP_ENTRY"
echo movie episode utility successfully uninstalled

