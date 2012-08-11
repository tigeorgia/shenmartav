#!/bin/sh

# shenmartav deployment script on LOCAL development machine
# CAREFUL NOW!

ROOT="/home/tig/shenmartav/"
DB="deploy/db.sql.bz2"
CODE="deploy/code"
EXCLUDES="--exclude=settings.py --exclude=settings.pyc --exclude=locale*"
TARBALL="deploy/code.tar.bz2"

cd ${ROOT}
rm -f ${CODE}.tar.bz2 ${DB}

#echo 'Updating version...'
#./shenmartav/deployment/update_version.sh

echo 'Preparing code tarball...'
cp -a shenmartav ${CODE}
rm -rf ${CODE}/.git
tar -cjf ${TARBALL} ${EXCLUDES} ${CODE}
rm -rf ${CODE}

#echo 'Preparing database dump...'
#dbdump="db-`date +'%Y%m%d'`.sql"
#pg_dump -U shenmartav -h localhost shenmartav > dumps/${dbdump}
#tar cjf dumps/${dbdump}.bz2 dumps/${dbdump}
#cp dumps/${dbdump}.bz2 ${DB}

echo 'Copying to server...'
scp ${TARBALL} shen:/home/tigeorgia/shenmartav/
