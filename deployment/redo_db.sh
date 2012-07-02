#!/bin/bash
#
# Drop current database and recreate it from given dumpfile.
# $ pg_dump -U shenmartav -h localhost shenmartav > dump.sql
#
# To create a database from scratch, you need a GIS-enabled template.
# As user postgres execute these:
# $ createdb --template=template0 -E UTF8 -U postgres template_postgis
# (8.4) $ createlang plpgsql template_postgis
# (8.4) $ psql -d template_postgis -f /usr/share/postgresql/8.4/contrib/postgis.sql
# (9.1) $ psql -d template_postgis -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
# $ psql -c "CREATE USER shenmartav PASSWORD 'shenmartav'"
# $ psql -c "CREATE DATABASE shenmartav OWNER shenmartav TEMPLATE template_postgis ENCODING 'utf8';"

DBNAME='shenmartav'
DBUSER='shenmartav'
PSQL=/usr/bin/psql


if [ -z "${1}" ]; then
    echo "Usage: ${0} <dump.sql>"
    exit 1
fi

${PSQL} --command="DROP DATABASE ${DBNAME}"
${PSQL} --command="CREATE DATABASE ${DBNAME} OWNER ${DBUSER} TEMPLATE template_postgis ENCODING 'utf8';"
${PSQL} ${DBNAME} < ${1}
