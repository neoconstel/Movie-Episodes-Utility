sudo echo
echo installing movie episode utility

export APP=movie-episode-utility
sudo mkdir $APP
sudo cp *.py $APP
sudo python3 -m zipapp $APP
sudo chmod 777 $APP*
sudo rm -r $APP

export APP_DIR="/usr/share"
sudo mkdir $APP_DIR/$APP
sudo mv $APP.pyz $APP_DIR/$APP

sudo cp uninstall.sh $APP_DIR/$APP
sudo cp manual $APP_DIR/$APP

export APP_ENTRY=episode-utility
sudo touch $APP_ENTRY
sudo chmod 777 $APP_ENTRY
sudo echo "#!/bin/bash
if [ \"\$1\" == \"--uninstall\" ]; then
	sudo $APP_DIR/$APP/uninstall.sh
elif [ \"\$1\" == \"--help\" ]; then
	less $APP_DIR/$APP/manual
elif [ \$# == 0 ]; then
	python3 $APP_DIR/$APP/$APP.pyz
else
	echo Invalid command. Run \\\"$APP_ENTRY --help\\\" to view the manual
fi" > $APP_ENTRY
export APP_ENTRY_DIR="/usr/bin"
sudo mv $APP_ENTRY $APP_ENTRY_DIR
echo movie episode utility successfully installed. Run \"$APP_ENTRY\" from terminal to launch.

