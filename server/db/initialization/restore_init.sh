#!/bin/sh

echo ">>>>  Right before DB initialization <<<<"
# use while loop to check if the database is running
timeout=2
while true
do
    netstat -uplnt | grep :5432 | grep LISTEN > /dev/null
    verifier=$?
    if [ 0 = $verifier ]
        then
            echo "Running database initialization script"
            psql -U postgres -d postgres < /initialization/restore_init.txt
            break
        else
            echo "DB is not running yet"
            sleep $timeout
            timeout=$(( timeout*2 ))
            echo "Waiting for $timeout seconds"
    fi
done
