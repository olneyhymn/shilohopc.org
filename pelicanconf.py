#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admin'
SITENAME = u'Shiloh Presbyterian Church | Raleigh, NC'
SITEURL = ''

PATH = 'content'
MARKUP = ('md', 'html')
STATIC_PATHS = ['./static']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (,)

# Social widget
# SOCIAL = (,)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = './pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites', 'assets']
WEBASSETS = True
BOOTSTRAP_FLUID = False
FAVICON = "static/favicon.ico"
CATEGORIES_SAVE_AS = None
TAGS_SAVE_AS = None
AUTHORS_SAVE_AS = None
ARCHIVES_SAVE_AS = None


CUSTOM_CSS = 'static/custom.css'

# Navbar
SITELOGO = 'static/logo.jpg'
HIDE_SITENAME = True

# Body
HIDE_SIDEBAR = True
INDEX_SAVE_AS = None
BANNER = 'static/skyline_20.jpg'
OFFICERS = [("Matthew Holst", "matthew.holst@shilohopc.org", "Matthew Holst served as pastor of Geneva Orthodox Presbyterian Church in Marietta, Georgia from 2010 to 2016; before that he ministered in Cambridge Presbyterian Church (UK) for one year. Matt is a 2008 graduate of Greenville Presbyterian Theological Seminary. His wife, Stacy is a native of Greenville SC and together they have four children. He was installed as senior pastor of Shiloh in June 2016. ", "Pastor", 'holst'),
            ("Irfon Hughes", "irfon.hughes@shilohopc.org",
             "Irfon and Ann Hughes and their 5 children came to the USA in 1984. He is a Welsh speaking Welsh American. They have been married for 47 years and have 16 grandchildren. Irfon pastored 2 congregations in Massachusetts and Western Pennsylvania, and retired in 2008. However retirement has been hard to achieve and has been an assistant pastor in Providence PCA in Fayetteville NC and more recently has become associate pastor at Shiloh OPC in Raleigh. He and Ann have moved to Fuquay Varina NC. He still loves to preach, read History, historical theology, supports missionary endeavor and pastoral studies, and plays golf, in that order. He is getting ever closer to meeting his Lord and looks forward to that.", "Pastor", 'hughes'),
            ("Kevin Joyner", "kevin.joyner@shilohopc.org",
             "Kevin has been married to his wife Catrin (Hughes) since September of 1999, and they live in Fuquay-Varina.  They have been blessed with five children: Lydia, Abigail, Philip, Simeon, and Knox.  Kevin is a native of Greenville, North Carolina, and he has served as an elder in the Orthodox Presbyterian Church since 2006.", "Elder", 'joyner'),
            ("Mark Honeck", "mark.honeck@shilohopc.org",
             "After retiring from farming in NW Ohio, Mark Honeck and his wife Skip (Kathleen) moved to North Carolina to be closer to family.  We are thankful that the Lord brought us into fellowship with Shiloh congregation, and we are thankful as well for the opportunity to serve Him and his people. \"For from Him and through Him and to Him are all things.  To Him be the glory forever. Amen.\"  Rom. 11:36", "Elder", 'honeck'),
            ("Mark Kirby", "mark.kirby@shilohopc.org",
             "Mark Kirby is a native North Carolinian and a home builder and has lived in the Triangle area since 1993. Mark and his wife, Christin, live in Raleigh and have been blessed with four children - Oakley, Charlie, Coleman and Sally. They enjoy time together as a family, particularly when they can be outside enjoying the beautiful NC weather.", "Elder", 'kirby'),
            ("McRay Simmons", "mcray.simmons@shilohopc.org",
             "McRay Simmons and his wife Cathy live in Fuquay Varina.  They are the proud parents of two, both of whom are married to Godly spouses by the grace of God, and grandparents of five very special covenant children.  The deacons at Shiloh pray that we will serve Christ's church at Shiloh and beyond by staying \"dressed for action and keep[our] lamps burning, and be like men who are waiting for [our] master to come home from the wedding feast, so that[we] may open the door to him at once when he comes and knocks.\"  Luke 12:35-36", "Deacon", 'simmons'),
            ("Pete Tola", "pete.tola@shilohopc.org",
             "Pete Tola is a Raleigh native, Navy veteran and a graduate of NC State.  He is the proud father of a daughter whose  salvation is secured by her faith in Jesus Christ.  He welcomes the opportunity to serve alongside the body of believers called Shiloh. \"They that profess themselves to be Christ's are known not only by what they say, but by what they practice.  For the tree is known by its fruits.\" - Ignatius", "Deacon", 'tola'),
            ("Tim Hopper", "tim.hopper@shilohopc.org",
             "Tim Hopper moved to the area in 2010 for graduate school and started worshipping at Shiloh a few weeks after it was started. He works as a statistician and computer programmer. Tim and his wife Maggie live in Raleigh.", "Deacon", 'hopper'),
            ]
CONFERENCES = [
    ("2012 Reformation Conference", "Science, Evil, and the Environment: Answering Contemporary Challenges to the Christian Faith", "Speakers: Scott Oliphint and James Wanlinss",
     "In our first annual Reformation Conference, Dr. James Wanlinss, Associate Professor of Physics at Presbyterian College, and Dr. K. Scott Oliphint is professor of apologetics and systematic theology at Westminster Theological Seminary addressed three contemporary challenges to the Christian faith.", "http://www.sermonaudio.com/search.asp?sourceonly=true&currSection=sermonssource&keyword=shiloh&keywordDesc=&subsetcat=series&subsetitem=Reformation+Conference+2012"),
    ("2013 Men’s Conference", "The Masculine Mandate", "Speakers: Dr. Rick Phillips",
     "In our first men's conference, Dr. Richard Phillips spoke on the masculine mandate from Genesis 1:28.. Rick is the senior minister of Second Presbyterian Church (PCA) in Greenville, SC. A former professor of leadership at West Point, he is the author of over twenty books and commentaries.", "http://www.sermonaudio.com/search.asp?sourceonly=true&currSection=sermonssource&keyword=shiloh&keywordDesc=&subsetcat=series&subsetitem=The+Masculine+Mandate"),
    ("2013 Reformation Conference", "Can We Trust the Bible?", "Speakers: Derek Thomas, James Anderson, Rosaria Butterfield", "Dr. Derek Thomas, Dr. James Anderson, and Dr. Rosaria Butterfield will be speaking on the topic \"Can We Trust the Bible?\" Dr. Thomas is the Distinguished Visiting Professor of Systematic and Historical Theology at Reformed Theological Seminary and Minister of Preaching and Teaching at First Presbyterian Church in Columbia, SC. Dr. Anderson is an ordained minister in the Associate Reformed Presbyterian Church and Associate Professor of Theology and Philosophy at Reformed Theological Seminary. Dr. Butterfield was a professor of English at Syracuse University and is wife of a local pastor.", "http://www.sermonaudio.com/search.asp?seriesOnly=true&currSection=sermonstopic&sourceid=shiloh&keyword=Reformation+Conference+2013&keyworddesc=Reformation+Conference+2013"),
    ("2014 Reformation Conference with truthXchange", "Tell the Truth: Christian Witness in a Pagan Planet", "Speakers: Dr. Peter Jones, Dr. Calvin Beisner, Dr. Joe Boot, Mrs. Pamela Frost, and Dr. Thaddeus Williams",
     "The first in a new series of Reformation Day symposiums. This free, 1.5 day event will take place at Shiloh Presbyterian Church and will be an opportunity to hear deep, theological teaching, participate in discussion times, and to have fellowship with other believers who are passionate about living out their faith in today’s “spiritual but not religious” culture.", "http://www.sermonaudio.com/search.asp?seriesOnly=true&currSection=sermonstopic&sourceid=shiloh&keyword=Reformation+Conference+2014&keyworddesc=Reformation+Conference+2014"),
    ("2016 Reformation Conference", "Evangelism and Christian Worldview", "Speakers: Allen Curry and Andrew Hoffecker",
     "Dr. Allen Curry on Evangelism and Dr. Andrew Hoffecker on Building a Christian Worldview. Sessions on Friday evening starting at 6:30 PM and Saturday morning at 9 AM. Sunday morning worship and Sunday school with both men.", "http://www.sermonaudio.com/search.asp?seriesOnly=true&currSection=sermonstopic&sourceid=shiloh&keyword=Reformation+Conference+2016&keyworddesc=Reformation+Conference+2016"),
    ("2016 Missions Conference", "Go Into All the World", "Speakers: Nick Batzig and Eric Hausler", "Church planters Nick Batzig and Eric Hausler speak on evangelism, outreach, and planting reformed churches.", "http://www.sermonaudio.com/search.asp?seriesOnly=true&currSection=sermonstopic&sourceid=shiloh&keyword=2017+Missions+Conference&keyworddesc=2017+Missions+Conference"),
]
CONNECT = [("http://www.sermonaudio.com/source_detail.asp?sourceid=shiloh", "volume-up", "SermonAudio.com"),
("https://www.youtube.com/channel/UCk0RaoXLCsZHd0Z8FrHa5aw", "youtube", "YouTube"),
("http://www.twitter.com/shilohopc", "twitter-square", "Twitter"),
("http://www.facebook.com/shilohopc", "facebook-square", "Facebook"),
("https://www.instagram.com/shilohopc", "instagram", "Instagram"),
("tel:(919)578-1331", "phone", "(919) 578-1331"),
("mailto:info@shilohopc.org", "envelope", "info@shilohopc.org"),
]