#/bin/env bash

# To run:
# /usr/bin/time ./get.sh
#

models=(
    "sites.site"
    "auth.group"
    "socialaccount.socialapp"
    "coderdojochi.cdcuser"
    "coderdojochi.course"
    "coderdojochi.equipmenttype"
    "coderdojochi.location"
    "coderdojochi.meetingtype"
    "coderdojochi.raceethnicity"
    "coderdojochi.guardian"
    "coderdojochi.meeting"
    "coderdojochi.mentor"
    "coderdojochi.student"
    "coderdojochi.session"
    "coderdojochi.mentororder"
    "coderdojochi.order"
)

for i in "${!models[@]}"
do
    echo "Exporting '${models[$i]}' to '`printf %02d $i`-${models[$i]}.json'"
    heroku run --app production-wac python -W ignore manage.py dumpdata "${models[$i]}" --indent 2 -- > "`printf %02d $i`-${models[$i]}.json"
done