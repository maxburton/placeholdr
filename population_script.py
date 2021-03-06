# -*- coding: utf-8 -*-

import os

from geoposition import Geoposition

from placeholdr_project import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'placeholdr_project.settings')

import django

django.setup()
#settings.configure()

from placeholdr.models import User, UserProfile, Place, Trip, TripNode, TripReview, PlaceReview, PlaceTag, TripTag
from django.template.defaultfilters import slugify
import urllib.request

def populate():
	# Much secure
	users = [
		# 1
		{"username": "michael", "password": "pass1357",
		 "bio": "Just a dad looking for some places suggested by some like-minded people!",
		 "livesIn": "London", "rep": 2360,
		 "picture": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/3/3b/Jens_Fink-Jensen.jpg", 'media/profile_images/michael.jpg')[0], #"https://previews.123rf.com/images/libertos/libertos1205/libertos120500022/13701871-cheerful-middle-aged-man-in-a-baseball-cap-.jpg"
		 },

		# 2
		{"username": "itsnaomi", "password": "pass1357",
		 "bio": "Just passing through!", "livesIn": "Brussels", "rep": 0,
		 "picture": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Maria_Elena_Boschi_-_Festival_Economia_2016.jpg/1920px-Maria_Elena_Boschi_-_Festival_Economia_2016.jpg", 'media/profile_images/naomi.jpg')[0]
		 },

		# 3
		{"username": "samtakespics", "password": "pass1357",
		 "bio": "I'm a photographer and travel around a lot for my work, taking pictures for travel guides. "
				"My favourite kind of places are the ones with scenic views.",
		 "livesIn": "Arizona", "rep": 1240,
		 "picture": urllib.request.urlretrieve("https://thumb9.shutterstock.com/display_pic_with_logo/3471602/355236068/stock-photo-close-up-of-young-handsome-indian-photographer-taking-a-photograph-asian-man-holding-camera-355236068.jpg", 'media/profile_images/sam.jpg')[0]
		 },

		# 4
		{"username": "_amy_", "password": "pass1357",
		 "bio": "I'm a Geography student with a passion for maps, travelling, and coffee",
		 "livesIn": "Glasgow", "rep": 5,
		 "picture": ""
		 },

		# 5
		{"username": "baracko", "password": "pass1357",
		 "bio": "I'm a busy man, but I like to take trips in my free time. Distance is never a problem",
		 "livesIn": "Chicago", "rep": 80,
		 "picture": urllib.request.urlretrieve("https://pbs.twimg.com/media/CtUtSbAW8AE9NvM.jpg", 'media/profile_images/barack.jpg')[0]
		 },

		# 6
		{"username": "davidm", "password": "pass1357",
		 "bio": "I am a Senior Lecturer at the School of Computing Science "
				"in the College of Science and Engineering at"
				" the University of Glasgow. ",
		 "livesIn": "Edinburgh", "rep": 100,

		 "picture": ""#urllib.request.urlretrieve("https://www.gla.ac.uk/media/media_209689_en.jpg", 'media/profile_images/david.jpg')[0]
		 },

		 # 7
		{"username": "gustavethetower", "password": "pass1357",
		 "bio": "I am the greatest architect to ever live, prove me wrong",
		 "livesIn": "Paris", "rep": 450,

		 "picture": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/7/7f/Caricature_Gustave_Eiffel.png", 'media/profile_images/gustave.jpg')[0]
		 },

		 # 8
		{"username": "ocin", "password": "pass1357",
		 "bio": "Oh flower of Scotland!",
		 "livesIn": "Paisley", "rep": 12,
		 "picture": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/d/d4/Igel01.jpg", 'media/profile_images/ocin.jpg')[0]
		 },

		 # 9
		{"username": "homerj", "password": "pass1357",
		 "bio": "No TV and no beer make Homer something something... ",
		 "livesIn": "Springfield", "rep": 780,
		 "picture": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/en/0/02/Homer_Simpson_2006.png", 'media/profile_images/homer.jpg')[0]
		 },

		 # 10
		{"username": "fawkes", "password": "pass1357",
		 "bio": "Firework Fanatic",
		 "livesIn": "London", "rep": 400,
		 "picture": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/0/01/Gaj_Foksi.jpg", 'media/profile_images/fawkes.jpg')[0]
		 }
	]

	places = [

		# 1
		{"userId": 2, "lat": "50.890163106", "long": "4.337998648",
		 "desc": "The Atomium was erected in 1958 as part of the World Fair exhibition. "
				 "Modelled on an iron atom that has been magnified 165 billion times, it"
				 " consists of 9 metal spheres. The structure weighs 2400 tons and is 102m high. "
				 "The top sphere has a restaurant and provides panoramic views. The other spheres contain "
				 "exhibition spaces.",
		 "name": "Atomium",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Atomium_320_by_240_CCBY20_flickr_Mike_Cattell.jpg/1200px-Atomium_320_by_240_CCBY20_flickr_Mike_Cattell.jpg", 'media/place_images/atomium.jpg')[0]
		 },

		# 2
		{"userId": 6, "lat": "55.876623", "long": "-4.285432",
		 "desc": "Speciality Coffee & OG Brunch based in Glasgow, Scotland. "
				 "A speciality coffee roaster and cafe, putting avocado on toast since 2012.",
		 "name": "Papercup Glasgow",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/8/84/Caf%C3%A9_M%C3%A9lange%2C_Wien.jpg", 'media/place_images/papercup.jpg')[0]
		 },

		# 3
		{"userId": 4, "lat": "55.87226070000001", "long": "-4.282248600000003",
		 "desc": "Located in one of the West End's most vibrant & community spirited streets, "
				 "you'll find the Glaswegian hub of Artisan Roast.",
		 "name": "Artisan Roast",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/2/27/Arrow_Hotel_interior_coffee_shop_2.JPG", 'media/place_images/artisan.jpg')[0]
		 },

		# 4
		{"userId": 3, "lat": "36.056595", "long": "-112.125092",
		 "desc": "The Grand Canyon is one of the seven natural wonders of the world, "
				 "and one of the largest canyons on Earth. It stretches for 450km. "
				 "Parts of the canyon are more than 30km wide and one kilometer deep. "
				 "Many writers have tried to describe the wonder of the Grand Canyon, but it "
				 "is beyond words.",
		 "name": "Grand Canyon",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/a/aa/Dawn_on_the_S_rim_of_the_Grand_Canyon_%288645178272%29.jpg", 'media/place_images/canyon.jpg')[0]
		 },

		# 5
		{"userId": 6, "lat": "55.8721211", "long": "-4.2882005",
		 "desc": "Founded in 1451, the University of Glasgow is the fourth oldest university "
				 "in the English-speaking world. The University moved from High Street to Gilmorehill"
				 " in 1870. The campus was originally centred around the buildings erected on the "
				 "top of the hill, designed by George Gilbert Scott.",
		 "name": "University of Glasgow",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/a/aa/University_of_Glasgow%2C_East_Quadrangle_-_landscape.jpg", 'media/place_images/glasgow.jpg')[0]
		 },

		# 6
		{"userId": 1, "lat": "63.881363", "long": "-22.453115",
		 "desc": "Mineral-rich hot water from far beneath the earth forms the spectacular lagoon, "
				 "where a luxurious health spa has been developed in the rugged lava landscape. "
				 "The lagoon's geothermal seawater is known for its positive effects on the skin.",
		 "name": "Blue Lagoon",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Blue_Lagoon_Main_Building.JPG/800px-Blue_Lagoon_Main_Building.JPG", 'media/place_images/lagoon.jpg')[0]
		 },

		# 7
		{"userId": 6, "lat": "57.322858", "long": "-4.424382",
		 "desc": "Loch Ness is Scotland's most famous loch. "
				 "Over 300 million years ago a collision of tectonic plates forced the land to bend and buckle, "
				 "forming high mountains and deep gorges. The depths of these gorges were gradually filled with"
				 " water and a string of lochs were formed; Loch Oich, Loch Lochy and Loch Ness.",
		 "name": "Loch Ness",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/d/de/Loch_Ness_Panorama.png", 'media/place_images/lochness.jpg')[0]
		 },

		# 8
		{"userId": 5, "lat": "55.9417628996", "long": "-3.1856492574",
		 "desc": "The University of Edinburgh, founded in 1582, is the sixth-oldest university in the English-speaking world"
				 " and one of Scotland's ancient universities.",
		 "name": "University of Edinburgh",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/7/75/Old_College_of_Edinburgh_University.JPG", 'media/place_images/edinburgh.jpg')[0]
		 },

		# 9
		{"userId": 6, "lat": "56.3380603144", "long": "-2.78913684344",
		"desc": "Founded in the 15th century, St Andrews is Scotland's"
				" first university and the third oldest in the English speaking world.",
		"name": "University of St Andrews",
		"picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/0/0d/St_Salvators_chapel_and_north_street_-St_Andrews.jpg", 'media/place_images/saints.jpg')[0]
		 },

		# 10
		{"userId": 3, "lat": "50.8484703", "long": "4.353890500000034",
		 "desc": "Delirium Café is a bar which holds the Guinness World Record for the most beers offered with 2004. "
				 "Today they are getting close to 2500.",
		 "name": "Delirium Café",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/4/44/CafeDelirium.JPG", 'media/place_images/delirium.jpg')[0]
		 },

		# 11
		{"userId": 1, "lat": "64.6699154", "long": "-17.181654900000012",
		 "desc": "Vatnajökull National Park is one of three national parks in Iceland. "
				 "The unique qualities of Vatnajökull National Park are primarily its great variety of landscape features,"
				 " created by the combined forces of rivers, glacial ice, and volcanic and geothermal activity.",
		 "name": "Vatnajökull National Park",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/8/84/Skaftafell_National_Park%2C_Svartifoss_%286817603945%29.jpg", 'media/place_images/vatnajokull.jpg')[0]
		 },

		# 12
		{"userId": 5, "lat": "37.81194099999999", "long": "-107.6645057",
		 "desc": "The historic mining town of Silverton, Colorado will offer you nice mountain views during any roadtrip or visit.",
		 "name": "Silverton",
		 "picLink": urllib.request.urlretrieve("https://c1.staticflickr.com/3/2825/9910259186_dfbd578808_b.jpg", 'media/place_images/silverton.jpg')[0]
		 },

		# 13
		{"userId": 4, "lat": "56.9625746", "long": "-4.917060600000013",
		 "desc": "Loch Lochy (Scottish Gaelic, Loch Lòchaidh) is a large freshwater loch."
				 " With a mean depth of 70 m (230 ft), it is the third-deepest loch of Scotland.",
		 "name": "Loch Lochy",
		 "picLink": urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/e/eb/Loch_Lochy.jpg", 'media/place_images/lochy.jpg')[0]
		 },
	]

	trips = [
		# 1
		{"userId": 6,
		 "desc": "Head to Loch Ness from Glasgow before coming back for a coffee in town and see the university's buildings",
		 "name": "A Scottish Daytrip",
		 },
		# 2
		{"userId": 3, "desc": "Ride along some scenic routes and stop at very scenic places",
		 "name": "Nature in the US"},
		# 3
		{"userId": 1, "desc": "Trek in cold cold Iceland before getting warm in a lagoon",
		 "name": "Hot and Cold"},
		# 4
		{"userId": 3, "desc": "Have some drinks in Belgium and see some sights",
		 "name": "Beer Trip"},
		# 5
		{"userId": 5, "desc": "Have a look at some universities and how pretty they are",
		 "name": "Academic Roadtrip"},
		# 6
		{"userId": 4,
		 "desc": "This trip is for coffee fanatics who aren't scared of dying of a coffee overdose by visiting a lot of coffee places",
		 "name": "Hyperactive Coffee"},
	]

	tripNodes = [
		# A Scottish Daytrip
		{"placeId": 7, "tripId": 1, "tripPoint": 0},
		{"placeId": 13, "tripId": 1, "tripPoint": 1},
		{"placeId": 3, "tripId": 1, "tripPoint": 2},
		{"placeId": 5, "tripId": 1, "tripPoint": 3},

		# Nature in the US
		{"placeId": 12, "tripId": 2, "tripPoint": 0},
		{"placeId": 4, "tripId": 2, "tripPoint": 1},

		# Iceland
		{"placeId": 11, "tripId": 3, "tripPoint": 0},
		{"placeId": 6, "tripId": 3, "tripPoint": 1},

		# Brussels
		{"placeId": 1, "tripId": 4, "tripPoint": 0},
		{"placeId": 10, "tripId": 4, "tripPoint": 1},

		# Academic Roadtrip
		{"placeId": 9, "tripId": 5, "tripPoint": 0},
		{"placeId": 5, "tripId": 5, "tripPoint": 1},
		{"placeId": 8, "tripId": 5, "tripPoint": 2},

		# Coffee
		{"placeId": 2, "tripId": 6, "tripPoint": 0},
		{"placeId": 3, "tripId": 6, "tripPoint": 1}
	]

	placeReviews = [
		# Blue Lagoon
		{"userId": 1, "placeId": 6, "stars": 2,
		 "review": "It was nice and #warm in the water but way too cold outside. Risky"},
		{"userId": 5, "placeId": 6, "stars": 5, "review": "The right amount of hot and cold"},

		# Grand Canyon
		{"userId": 5, "placeId": 4, "stars": 5,
		 "review": "Very #pretty and very #warm. Good place for some philosophical thinking. "},

		# UofG
		{"userId": 6, "placeId": 5, "stars": 4, "review": "In spite of the rain, the buildings were very pretty. "},
		{"userId": 4, "placeId": 5, "stars": 3,
		 "review": "Very #pretty but I wish you could visit the main building tower as well"},

		# Atomium
		{"userId": 3, "placeId": 1, "stars": 3,
		 "review": "Very #scenic views. Very crowded though"},

		# Artisan Roast
		{"userId": 4, "placeId": 3, "stars": 5,
		 "review": "Some good #coffee to get you ready to write essays."},
		{"userId": 6, "placeId": 3, "stars": 2, "review": "Papercup makes better coffee"},

		# Artisan Roast
		{"userId": 4, "placeId": 2, "stars": 5,
		 "review": "I love #coffee"},

		# Loch Ness
		{"userId": 1, "placeId": 7, "stars": 2, "review": "Disappointed by the lack of monster"},

		# Delirium
		{"userId": 3, "placeId": 10, "stars": 4, "review": "I liked it"},

		# Iceland national park
		{"userId": 1, "placeId": 11, "stars": 4, "review": "Very #pretty, very cold, some nice trekking"},

		# Silverton
		{"userId": 5, "placeId": 12, "stars": 2, "review": "I mean it looked nice from afar but is there really anything to do there"},

		# Loch Lochy
		{"userId": 4, "placeId": 13, "stars": 4, "review": "I can't believe there's a place called Loch Lochy"},
	]

	tripReviews = [
		# Scottish daytrip
		{"userId": 6, "tripId": 1, "stars": 4,
		 "review": "Some very #nice scenery. I didn't see the Loch Ness monster but the good coffee afterwards made up for it"},
		{"userId": 4, "tripId": 1, "stars": 5, "review": "Deserves 5 stars just for Loch Lochy"},

		# US nature
		{"userId": 3, "tripId": 2, "stars": 5, "review": "Very #dry landscapes but still very #pretty"},
		{"userId": 5, "tripId": 2, "stars": 5, "review": "Good trip for some escape overall"},

		# Iceland
		{"userId": 1, "tripId": 3, "stars": 3, "review": "Could be way warmer"},
		{"userId": 3, "tripId": 3, "stars": 5, "review": "Iceland is insanely #pretty"},


		# Beers
		{"userId": 2, "tripId": 4, "stars": 4, "review": "A lot of hangovers but definitely worth it"},
		{"userId": 3, "tripId": 4, "stars": 3, "review": "Not enough beers"},

		# Academia
		{"userId": 4, "tripId": 5, "stars": 3,
		 "review": "It was nice but it reminded me of the work I'm supposed to be doing"},
		{"userId": 6, "tripId": 5, "stars": 4,
		 "review": "Glasgow is definitely the prettiest out of the three"},

		# Coffee
		{"userId": 4, "tripId": 6, "stars": 4, "review": "Could be better"},
	]

	users_fav = [
		{"username": "michael", "favPlace": 2, "recommendedTrip": 3},
		{"username": "_amy_", "favPlace": 13, "recommendedTrip": 3},
		{"username": "samtakespics", "favPlace": 4, "recommendedTrip": 2},
		{"username": "homerj", "favPlace": 10, "recommendedTrip": 4},
		{"username": "gustavethetower", "favPlace": 5, "recommendedTrip": 2},
		{"username": "fawkes", "favPlace": 7, "recommendedTrip": 1},
		{"username": "davidm", "favPlace": 5, "recommendedTrip": 5},
	]
	
	place_tags = [
		{"userId":5, "placeId":4, "tagText":"pretty"},
		{"userId": 5, "placeId": 4, "tagText": "warm"},
		{"userId": 4, "placeId": 3, "tagText": "coffee"},
		{"userId": 4, "placeId": 2, "tagText": "coffee"},
		{"userId": 1, "placeId": 11, "tagText": "pretty"},
		{"userId":1, "placeId":6, "tagText":"warm"},
		{"userId":3, "placeId":1, "tagText":"scenic"}
	]
	
	trip_tags = [
		{"userId":6, "tripId":1, "tagText":"nice"},
		{"userId":3, "tripId":2, "tagText":"dry"},
		{"userId": 3, "tripId": 2, "tagText": "pretty"},
		{"userId":3, "tripId":3, "tagText":"pretty"}
	]
	
	following = [
		{"username": "michael", "follows": ["samtakespics", "baracko", "homerj"]},
		{"username": "baracko", "follows": ["fawkes", "davidm", "gustavethetower"]},
		{"username": "_amy_", "follows": ["samtakespics"]},
		{"username": "davidm", "follows": ["baracko", "gustavethetower", "fawkes"]}
	]

	for user in users:
		corrected_image_url = user["picture"].replace("media/","")
		us = add_user(user["username"], user["password"], user["bio"], user["livesIn"], user["rep"], corrected_image_url)

	for place in places:
		corrected_image_url = place["picLink"].replace("media/","")
		p = add_place(place["userId"], place["lat"], place["long"], place["desc"], place["name"], corrected_image_url)

	for trip in trips:
		t = add_trip(trip["userId"], trip["desc"], trip["name"])

	for tripR in tripReviews:
		tr = add_trip_review(tripR["userId"], tripR["tripId"], tripR["stars"], tripR["review"])

	for placeR in placeReviews:
		pr = add_place_review(placeR["userId"], placeR["placeId"], placeR["stars"], placeR["review"])

	for trip_n in tripNodes:
		t_n = add_trip_node(trip_n["tripId"], trip_n["placeId"], trip_n["tripPoint"])

	for fav in users_fav:
		f = add_favourites(fav["username"], fav["favPlace"], fav["recommendedTrip"])
		
	for p_tag in place_tags:
		p_t = add_place_tag(p_tag["userId"], p_tag["placeId"], p_tag["tagText"])
		
	for t_tag in trip_tags:
		t_t = add_trip_tag(t_tag["userId"], t_tag["tripId"], t_tag["tagText"])

	for user in following:
		for u in user["follows"]:
			f = add_following(user["username"], u)


def add_user(name, pword, bio, livesIn, rep, picture):
    u = User.objects.get_or_create(username=name, password=pword)[0]
    u.set_password(u.password)
    u.save()
    up = UserProfile.objects.get_or_create(user=u, bio=bio, livesIn=livesIn, rep=rep, picture=picture)[0]
    return up


def add_place(puserId, plat, plong, pdesc, pname, ppic):
    p = Place.objects.get_or_create(name=pname, userId=UserProfile.objects.get(pk=puserId), position=Geoposition(float(plat),float(plong)), desc=pdesc,
                                    picLink=ppic,
                                    slug=slugify(pname))[0]
    return p


def add_trip(tuserId, tdesc, tname):
    t = Trip.objects.get_or_create(name=tname, userId=UserProfile.objects.get(pk=tuserId), desc=tdesc,
                                   slug=slugify(tname))[0]
    return t


def add_trip_node(tnTripId, tnPlaceId, tnTripPoint):
    tn = TripNode.objects.get_or_create(tripId=Trip.objects.get(pk=tnTripId), placeId=Place.objects.get(pk=tnPlaceId),
                                        tripPoint=tnTripPoint)[0]
    return tn


def add_place_review(prUId, prPId, prS, prR):
    pr = PlaceReview.objects.get_or_create(userId=UserProfile.objects.get(pk=prUId), placeId=Place.objects.get(pk=prPId),
                                           stars=prS, review=prR)[0]
    return pr


def add_trip_review(trUId, trTId, trS, trR):
    tr = TripReview.objects.get_or_create(userId=UserProfile.objects.get(pk=trUId), tripId=Trip.objects.get(pk=trTId),
                                          stars=trS, review=trR)[0]
    return tr


def add_favourites(username, pid, tid):
    u = User.objects.get_or_create(username=username)[0]
    up = UserProfile.objects.get_or_create(user=u)[0]
    up.favPlace = Place.objects.get_or_create(pk=pid)[0]
    up.recommendedTrip = Trip.objects.get_or_create(pk=tid)[0]
    up.save()
	
def add_place_tag(ptUId, ptPId, ptTT):
    pt = PlaceTag.objects.get_or_create(userId=UserProfile.objects.get(pk=ptUId), placeId=Place.objects.get(pk=ptPId),
                                           tagText=ptTT)[0]
    return pt
	
def add_trip_tag(ttUId, ttTId, ttTT):
    tt = TripTag.objects.get_or_create(userId=UserProfile.objects.get(pk=ttUId), tripId=Trip.objects.get(pk=ttTId),
                                           tagText=ttTT)[0]
    return tt


def add_following(username, following):
    u = User.objects.get_or_create(username=username)[0]
    up = UserProfile.objects.get_or_create(user=u)[0]
    f = User.objects.get_or_create(username=following)[0]
    fp = UserProfile.objects.get_or_create(user=f)[0]
    up.follows.add(fp)
    up.save()

if __name__ == '__main__':
    print("Starting Placeholdr (tm) population script...")
    populate()
    print("Populated!")