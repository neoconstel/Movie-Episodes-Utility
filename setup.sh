sudo echo
echo installing movie episode utility

export APP=episode-utility
sudo mkdir $APP
sudo cp *.py $APP
sudo python3 -m zipapp $APP
sudo chmod 777 $APP*
sudo rm -r $APP

export APP_DIR="/usr/share"
sudo mkdir $APP_DIR/$APP
sudo mv $APP.pyz $APP_DIR/$APP

export APP_ENTRY=episode-utility
sudo touch $APP_ENTRY
sudo chmod 777 $APP_ENTRY
sudo echo "#!/bin/bash" > $APP_ENTRY
sudo echo "python3 $APP_DIR/$APP/$APP.pyz" >> $APP_ENTRY
export APP_ENTRY_DIR="/usr/bin"
sudo mv $APP_ENTRY $APP_ENTRY_DIR
echo movie episode utility successfully installed. Run \"$APP_ENTRY\" from terminal to launch.

