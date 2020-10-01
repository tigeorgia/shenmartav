=========================
READ ME for shenmartav CMS
=========================
Hello and welcome to the shenmartav CMS!

The CMS is built on the Django Admin (https://docs.djangoproject.com/en/dev/ref/contrib/admin/) and DjangoCMS (https://www.django-cms.org/) . You can access it via the URL /admin, e.g.

http://shenmartav.ge/en/admin/

In the following, only the relevant sections of the admin will be explained.



Rosetta
=======
In the header you will find, apart from 'Change password' and 'Log out' a link to Rosetta (http://code.google.com/p/django-rosetta/):

http://shenmartav.ge/en/admin/rosetta/

Content that was marked as translatable by a developer can be edited here. Translations become live without having to restart the application server, but the translation process is somehow buggy as you can see in https://github.com/tigeorgia/shenmartav.ge/issues/56 .



Blog
====
The next interesting item is the blog feature of the site. It is based on Django Basic Apps (https://github.com/nathanborror/django-basic-apps). It can be accessed via

http://shenmartav.ge/en/admin/blog/post/

Categories or Blogroll are not used and the comment feature has been somewhat disabled as we are using Facebook comments.



Draft Laws
==========
The draft laws can be browsed and edited, but usually that won't be necessary. It might actually be overwritten by a subsequent import.

http://shenmartav.ge/en/admin/draftlaw/draftlaw/



Income Declarations
===================
The income declarations can be browsed and edited, but usually that won't be necesssary. It might actually be overwritten by a subsequent import.

http://shenmartav.ge/en/admin/incomedeclaration/incomedeclaration/



Questions
=========
This is something where editor involvement is required. When a visitor asks a question to a representative (currently Georgian MPs only), it will be found here, initially non-public:

http://shenmartav.ge/en/admin/question/question/

A question can be made public by ticking the checkbox next to it (or them) and using the action 'Mark selected questions as public'. Once that is done, a message with that question is sent to http://parliament.ge, but it seems that feature is a bit unstable (possibly on their side), see https://github.com/tigeorgia/shenmartav.ge/issues/49 for a discussion. If you want to resend the question to the parliament, just empty the text area 'Parliament response' and save the question. These messages have a sender email address the answer from parliament will go to, it is constructed like this:

ask+<representative slug>-<question id>@<site domain>

So the mail server for your site domain should be configured appropriately.



Representatives
===============
This app is a bit more complex.

Party
-----
Representatives belong to parties which you can set up here. Also, parties belong to units, further down.

http://shenmartav.ge/en/admin/representative/party/


Representatives
---------------
Representatives can be viewed and edited here, but the data might be overwritten by subsequent imports (unlikely at this stage, though) or management scripts to update assets or voting records, etc.

http://shenmartav.ge/en/admin/representative/representative/


Terms
-----
A rather new feature that is not in use yet, because the relationships have to be set up by an editor first or else the visitors would not see any representatives. See https://github.com/tigeorgia/shenmartav.ge/issues/95 for the current discussion.

http://shenmartav.ge/en/admin/representative/term/

Representatives served in 0 to n terms and each unit as an active term and 0 to n inactive terms.


Unit
----
Representatives gather in units, like Ajaran Supreme Council, Parliament of Georgia or Tbilisi City Hall.

http://shenmartav.ge/en/admin/representative/unit/



Sites
=====
Well, currently only one site per installation is supported, but it's domain and name need to be setup here:

http://shenmartav.ge/en/admin/sites/site/



SMS Alerts
==========
Transparency International Georgia operates an SMS alert service, check here to subscribe http://parliament.transparency.ge/subscribe/?lang=en .
These alert can be added here for them to be displayed on the front page.

http://shenmartav.ge/en/admin/smsalert/smsalert/

Originally, this was intended to actually send out an alert through a SMS gateway. But currently that part is defunct as there are problems with short codes and the connections to Georgia's mobile network operators.



Voting Records
==============
The voting records can be browsed and edited, but usually that won't be necesssary. It might actually be overwritten by a subsequent import.

http://shenmartav.ge/en/admin/votingrecord/votingrecord/
