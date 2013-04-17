#!/bin/sh

# shenmartav deployment script on REMOTE server
# CAREFUL NOW!

ROOT="/home/tigeorgia/myparliament"
DEPLOY="${ROOT}/deploy"

cd ${ROOT}

echo "Saving settings and translations ..."
if [ ! -d ${DEPLOY} ]; then
	mkdir ${DEPLOY}
	if [ "$?" -ne "0" ]; then
		exit 1
	fi
fi
cp -a shenmartav/locale shenmartav/settings.py* ${DEPLOY}/

echo 'Installing code ...'
tar xjf code.tar.bz2
rm -rf old
mv shenmartav old
mv ${DEPLOY}/code shenmartav

echo "Restoring settings and translations ..."
cp -a ${DEPLOY}/settings.* ${DEPLOY}/locale shenmartav/

rm -rf ${DEPLOY}/

#echo 'Installing database ...'
#bunzip2 --force db.sql.bz2
#sudo su --command "${ROOT}/shenmartav/deployment/redo_db.sh ${ROOT}/db.sql" postgres

#echo 'Adjusting site ...'
#./shenmartav/deployment/update_site.py

echo 'Collecting static files ...'
./shenmartav/manage.py collectstatic

#echo 'Updating search indices ...'
#./shenmartav/manage.py update_index

echo 'Restarting webserver ...'
sudo /etc/init.d/apache2 restart

echo 'DONE.' # You still might have to update search indices: manage.py update_index'

# rm db.sql code.tar.bz2
