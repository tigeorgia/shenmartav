#!/bin/sh

# shenmartav deployment script on LOCAL development machine
# CAREFUL NOW!

ROOT=/home/tig/shenmartav/
DB=deploy/db.sql.bz2
CODE=deploy/code

cd ${ROOT}
rm -f ${CODE}.tar.bz2 ${DB}

echo 'Updating version...'
./shenmartav/deployment/update_version.sh

echo 'Preparing code tarball...'
cp -a shenmartav ${CODE}
rm -rf ${CODE}/.git
tar cjf ${CODE}.tar.bz2 ${CODE}
rm -rf ${CODE}

echo 'Preparing database dump...'
dbdump="db-`date +'%Y%m%d'`.sql"
pg_dump -U shenmartav -h localhost shenmartav > dumps/${dbdump}
tar cjf dumps/${dbdump}.bz2 dumps/${dbdump}
cp dumps/${dbdump}.bz2 ${DB}

echo 'Copying to server...'
scp deploy/* shen:/home/tigeorgia/shenmartav/
