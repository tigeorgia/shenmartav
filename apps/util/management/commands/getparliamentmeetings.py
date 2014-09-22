import requests, BeautifulSoup, urllib3, os

from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from apps.util.models import Announcement
from settings import DEFAULT_FROM_EMAIL, PARLIAMENT_TEAM_EMAIL_ADDRESSES

class Command(BaseCommand):

    def handle(self, *args, **options):

        url = 'http://www.parliament.ge/ge/anonsi'
        is_sending_email = False

        print 'Parsing ' + url + '...',

        data = {}
        headers = {'Content-Type' : 'application/x-www-form-urlencoded',
                   'Referer' : url}
        response_content = requests.get(url, data=data, headers=headers).text

        print "Checking the parsed meetings with the ones we parsed in the past..."

        bsoup = BeautifulSoup.BeautifulSoup(response_content)

        mylistdiv = bsoup.findAll("div", {"class": "news_list no-image"})[0]
        meetings = mylistdiv.findChildren()
        number_of_meetings = len(meetings) / 3

        print str(number_of_meetings) + " meetings have been found."

        all_announcements = Announcement.objects.all()

        new_announcements_array = []

        for i in range(0, number_of_meetings-1):
            link_value = meetings[i*3].attrs[0][1]
            text_value = meetings[(i*3)+1].text
            found = False
            for announcement in all_announcements:
                if link_value in announcement.url:
                    found = True

            if not found:
		print "There is a new announcement: {0} - {1}".format(text_value.encode("utf-8"), link_value)
                new_announcements_array = new_announcements_array + [[text_value, link_value]]
                new_announcement = Announcement(text=text_value, url=link_value)
                new_announcement.save()
                is_sending_email = True

        if is_sending_email:
            print "Sending email"
            if len(new_announcements_array) > 1:
                email_body = "New announcements have been posted on the 'Upcoming event' page, on parliament.ge:\n"
            else:
                email_body = "A new announcement has been posted on the 'Upcoming event' page, on parliament.ge:\n"

            for announcement in new_announcements_array:
                email_body = email_body + "- " + announcement[0] + ": " + announcement[1] + "\n"

            email_body = email_body + "\nTo see all the announcement, visit this page: http://www.parliament.ge/ge/anonsi\n\n"

            email_body = email_body + "(This e-mail has been generated and sent automatically. Don't reply to it. If you have any questions, please go see the IT team)."

            send_mail('myparliament.ge - new annoucements', email_body, DEFAULT_FROM_EMAIL, PARLIAMENT_TEAM_EMAIL_ADDRESSES, fail_silently=False)

        print "Done."
