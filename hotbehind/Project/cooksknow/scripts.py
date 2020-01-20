# if __name__ == '__main__':
#     main()

from .models import Cuisine, Setting, Restaurant




# CUISINE_CHOICES = [
#     'African', 'American', 'Argentine', 'Asian', 'BBQ', 'Bagels', 'Bakery', 'Bar Food', 'Beverages', 'Brazilian', 'Breakfast', 'British', 'Bubble Tea', 'Burger', 'Cafe', 'Cajun', 'California', 'Cantonese', 'Caribbean', 'Chilean', 'Chinese', 'Coffee and Tea', 'Colombian', 'Creole', 'Crepes', 'Cuban', 'Deli', 'Desserts', 'Dim Sum', 'Diner', 'Donuts', 'Drinks Only', 'Eastern European', 'Ethiopian', 'European', 'Fast Food', 'Filipino', 'Fish and Chips', 'Fondue', 'French', 'Frozen Yogurt', 'Fusion', 'German', 'Greek', 'Grill', 'Hawaiian', 'Healthy Food', 'Ice Cream', 'Indian', 'Indonesian', 'International', 'Iranian', 'Irish', 'Israeli', 'Italian', 'Jamaican', 'Japanese', 'Juices', 'Kebab', 'Korean', 'Laotian', 'Latin American', 'Lebanese', 'Malaysian', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Mongolian', 'Moroccan', 'Nepalese', 'New American', 'New Mexican', 'Pacific', 'Pacific Northwest', 'Patisserie', 'Peruvian', 'Pizza', 'Polish', 'Pub Food', 'Pub Grub', 'Ramen', 'Russian', 'Salad', 'Salvadorean', 'Sandwich', 'Scandinavian', 'Seafood', 'Soul Food', 'Southern', 'Southwestern', 'Spanish', 'Steak', 'Sushi', 'Swedish', 'Taco', 'Taiwanese', 'Tapas', 'Tea', 'Teriyaki', 'Tex-Mex', 'Thai', 'Tibetan', 'Turkish', 'Vegetarian', 'Vietnamese']
# SETTING_CHOICES = [
#     'Delivery', 'Dine-out', 'Nightlife', 'Catching-up', 'Takeaway', 'Cafes', 'Daily Menus', 'Breakfast', 'Lunch', 'Dinner', 'Pubs&Bars', 'Pocket Friendly Delivery', 'Clubs & Lounges'
# ]

RESTAURANTS = [  # 34 long so far.
    {'name': 'Pok Pok', 'url': 'https://www.zomato.com/portland/pok-pok-richmond?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '3226 SE Division Street 97202', 'hours': '11:30 AM to 10 PM (Mon-Sun)', 'cuisine': 'Thai'},
    {'name': 'Screen Door', 'url': 'https://www.zomato.com/portland/screen-door-kerns?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1', 'location': '2337 E Burnside Street 97214',
        'hours': '8 AM to 2 PM, 5: 30 PM to 10 PM(Mon-Fri), 9 AM to 2: 30 PM, 5: 30 PM to 10 PM(Sat), 9 AM to 2: 30 PM, 5: 30 PM to 9 PM (Sun)', 'cuisine': 'Southern'},
    {'name': 'Andina Restaurant', 'url': 'https: // www.zomato.com/portland/andina-restaurant-pearl-district?utm_source= api_basic_user & utm_medium = api & utm_campaign = v2.1',
        'location': '1314 NW Glisan Street, Pearl District 97209', 'hours': '11: 30 AM to 2: 30 PM, 4 PM to 11 PM (Mon-Fri), 10: 30 AM to 2: 30 PM, 4 PM to 11 PM (Sat-Sun)', 'cuisine': 'Latin American, Tapas, Peruvian'},
    {'name': "Mother's Bistro & Bar", 'url': 'https://www.zomato.com/portland/mothers-bistro-bar-portland?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '212 SW Stark St, Portland 97204', 'hours': 'Closed (Mon),7 AM to 9 PM (Tue-Thu),7 AM to 10 PM (Fri),8 AM to 10 PM (Sat),8 AM to 2:30 PM (Sun)', 'cuisine': 'American, Breakfast'},
    {'name': 'Voodoo Doughnut', 'url': 'https://www.zomato.com/portland/voodoo-doughnut-chinatown-old-town?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '22 SW 3rd Avenue, Portland 97204', 'hours': '24 Hours', 'cuisine': 'Donuts'},
    {'name': 'Portland City Grill', 'url': 'https://www.zomato.com/portland/portland-city-grill-downtown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '111 SW 5th Avenue 97204', 'hours': '11 AM to 12 Midnight (Mon-Thu),11 AM to 1 AM (Fri),4 PM to 1 AM (Sat),9:30 AM to 10 PM (Sun)', 'cuisine': 'Asian, Seafood, Steak'},
    {'name': 'Tin Shed Garden Cafe', 'url': 'https://www.zomato.com/portland/tin-shed-garden-cafe-alberta?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '1438 NE Alberta Street, Portland 97211', 'hours': '7 AM to 9 PM (Mon-Sun)', 'cuisine': 'American, Burger'},
    {'name': 'Pambiche', 'url': 'https://www.zomato.com/portland/pambiche-kerns?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '2811 NE Glisan Street 97232', 'hours': '11 AM to 10 PM (Mon-Thu),11 AM to 12 Midnight (Fri),9 AM to 12 Midnight (Sat),9 AM to 10 PM (Sun)', 'cuisine': 'Cuban'},
    {'name': 'Deschutes Brewery Portland Public House', 'url': 'https://www.zomato.com/portland/deschutes-brewery-portland-public-house-pearl-district?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '210, NW 11th Avenue, Pearl District, Portland 97209', 'hours': '11 AM to 10 PM (Mon-Thu, Sun), 11 AM to 12 Midnight (Fri-Sat)', 'cuisine': 'American, Bar Food'},
    {'name': 'Montage', 'url': 'https://www.zomato.com/portland/montage-buckman?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1', 'location': '301 SE Morrison Street 97214',
        'hours': '5 PM to 2 AM (Mon-Thu),5 PM to 4 AM (Fri),10 AM to 2 PM, 5 PM to 4 AM (Sat),10 AM to 2 PM, 5 PM to 2 AM (Sun)', 'cuisine': 'Cajun, Soul Food'},
    {'name': "Jake's Famous Crawfish", 'url': 'https://www.zomato.com/portland/jakes-famous-crawfish-downtown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '401 SW 12th Avenue 97205', 'hours': '11:30 AM to 10 PM (Mon-Thu), 11:30 AM to 11 PM (Fri-Sat), 10 AM to 10 PM (Sun)', 'cuisine': 'Seafood, Pacific Northwest'},
    {'name': 'Papa Haydn', 'url': 'https://www.zomato.com/portland/papa-haydn-nob-hill-uptown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '701 NW 23rd Avenue 97210', 'hours': '11:30 AM to 10 PM (Mon-Thu),11:30 AM to 12 Midnight (Fri-Sat),10 AM to 10 PM (Sun)', 'cuisine': 'American, Breakfast, Desserts'},
    {'name': 'Toro Bravo', 'url': 'https://www.zomato.com/portland/toro-bravo-boise-eliot?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '120 NE Russell Street, Portland 97212', 'hours': '5 PM to 10 PM (Mon, Tue, Wed, Thu, Sun), 5 PM to 11 PM (Fri-Sat)', 'cuisine': 'Latin American, Spanish, Tapas'},
    {'name': 'Pine State Biscuits', 'url': 'https://www.zomato.com/portland/pine-state-biscuits-alberta?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '2204 NE Alberta Street, Portland 97211', 'hours': '7 AM to 3 PM (Mon-Sun)', 'cuisine': 'American, Coffee and Tea, Southern'},
    {'name': "Kenny & Zuke's Delicatessen", 'url': 'https://www.zomato.com/portland/kenny-zukes-delicatessen-downtown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '1038 SW Stark Street 97205', 'hours': '7 AM to 8 PM (Mon-Thu), 7 AM to 9 PM (Fri), 8 AM to 9 PM (Sat), 8 AM to 8 PM (Sun)', 'cuisine': 'Breakfast, Sandwich'},
    {'name': 'Nicholas', 'url': 'https: // www.zomato.com/portland/nicholas-buckman?utm_source = api_basic_user&utm_medium = api&utm_campaign = v2.1',
        'location': '318 SE Grand Avenue, Portland 97214', 'hours': '11 AM to 9 PM (Mon-Sat), 12 Noon to 9 PM (Sun)', 'cuisine': 'Greek, Mediterranean, Middle Eastern'},
    {'name': '¿Por Qué No?', 'url': 'https: // www.zomato.com/portland/por-que-no-boise-eliot?utm_source = api_basic_user&utm_medium = api&utm_campaign = v2.1',
        'location': '3524 N Mississippi Avenue, Portland 97227', 'hours': '11 AM to 10 PM (Mon-Sat), 11 AM to 9: 30 PM (Sun)', 'cuisine': 'Taco, Mexican'},
    {'name': "Podnah's Pit BBQ", 'url': 'https://www.zomato.com/portland/podnahs-pit-bbq-alberta?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1', 'location': '1625 NE Killingsworth Street, Portland 97211',
     'hours': '11 AM to 10 PM (Mon-Fri),9 AM to 10 PM (Sat),9 AM to 9 PM (Sun)', 'cuisine': 'BBQ, Breakfast, Southern'},
    {'name': 'Clyde Common', 'url': 'https://www.zomato.com/portland/clyde-common-downtown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '1014 SW Stark Street, Portland 97205', 'hours': '3 PM to 12 Midnight (Mon-Sun)', 'cuisine': 'New American'},
    {'name': 'Apizza Scholls', 'url': 'https://www.zomato.com/portland/apizza-scholls-hawthorne?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '4741 SE Hawthorne Boulevard, Portland 97215', 'hours': '5 PM to 9:30 PM (Mon-Fri),11:30 AM to 2:30 PM, 5 PM to 9:30 PM (Sat-Sun)', 'cuisine': 'Pizza'},
    {'name': '¿Por Qué No?', 'url': 'https://www.zomato.com/portland/por-que-no-hawthorne?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '4635 SE Hawthorne Boulevard, Portland 97215', 'hours': '11 AM to 9:30 PM (Mon, Tue, Wed, Thu, Sun), 11 AM to 10 PM (Fri-Sat)', 'cuisine': 'Taco, Mexican'},
    {'name': 'Higgins', 'url': 'https://www.zomato.com/portland/higgins-downtown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '1239 SW Broadway, Portland 97205', 'hours': '11:30 AM to 2 PM, 5 PM to 10:30 PM (Mon-Fri),5 PM to 10:30 PM (Sat-Sun)', 'cuisine': 'Pacific Northwest'},
    {'name': 'Voodoo Doughnut', 'url': 'https://www.zomato.com/portland/voodoo-doughnut-kerns?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '1501 NE Davis St, Portland 97232', 'hours': '24 Hours (Mon-Sun)', 'cuisine': 'Donuts'},
    {'name': 'Piazza Italia', 'url': 'https://www.zomato.com/portland/piazza-italia-pearl-district?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '1129 NW Johnson Street 97209', 'hours': 'Lunch, Dinner (Sun, Mon, Tue, Wed, Thu, Fri, Sat)', 'cuisine': 'Italian'},
    {'name': 'Tasty n Alder', 'url': 'https://www.zomato.com/portland/tasty-n-alder-downtown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '580 SW 12th Avenue, Portland 97205', 'hours': '9 AM to 10 PM(Mon, Tue, Wed, Thu, Sun), 9 AM to 11PM(Fri-Sat)', 'cuisine': 'Pacific Northwest, Steak'},
    {'name': 'Petite Provence', 'url': 'https: // www.zomato.com/portland/petite-provence-alberta?utm_source = api_basic_user & utm_medium = api & utm_campaign = v2.1',
        'location': '1824 NE Alberta Street, Portland 97211', 'hours': '7 AM to 9 PM(Mon, Tue, Wed, Thu, Sun), 7 AM to 10 PM(Fri-Sat)', 'cuisine': 'French, Bakery, Desserts'},
    {'name': 'Bunk Sandwiches', 'url': 'https://www.zomato.com/portland/bunk-sandwiches-downtown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '211 SW 6th Ave, Portland 97209', 'hours': '8 AM to 3 PM (Mon-Sun)', 'cuisine': 'Sandwich'},
    {'name': 'Hopworks Urban Brewery', 'url': 'https://www.zomato.com/portland/hopworks-urban-brewery-southeast?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '2944 SE Powell Boulevard 97202', 'hours': '11 AM to 11 PM (Mon, Tue, Wed, Thu, Sun), 11 AM to 12 Midnight (Fri-Sat)', 'cuisine': 'Burger, Pizza'},
    {'name': 'Gravy', 'url': 'https://www.zomato.com/portland/gravy-boise-eliot?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '3957 N Mississippi Avenue, Portland 97227', 'hours': '7:30 AM to 3 PM (Mon-Sun)', 'cuisine': 'American'},
    {'name': 'Besaws', 'url': 'https://www.zomato.com/portland/besaws-nob-hill-uptown?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1', 'location': '1545 NW 21st Avenue 97209',
        'hours': '8 AM to 3 PM, 5 PM to 9 PM (Mon-Wed, Sun), 8 AM to 3 PM, 5 PM to 10 PM (Thu-Sat)', 'cuisine': 'American, Breakfast, Pacific Northwest'},
    {'name': 'Russell Street Bar.B.Que', 'url': 'https://www.zomato.com/portland/russell-street-bar-b-que-boise-eliot?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '325 NE Russell Street, Portland 97212', 'hours': '11 AM to 9 PM (Mon, Tue, Wed, Thu, Sun), 11 AM to 10 PM (Fri-Sat)', 'cuisine': 'BBQ, Southern'},
    {'name': 'Le Pigeon', 'url': 'https://www.zomato.com/portland/le-pigeon-kerns?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '738 E Burnside Street 97214', 'hours': '5 PM to 10 PM (Mon-Sun)', 'cuisine': 'French'},
    {'name': 'Fire on the Mountain Buffalo Wings - Burnside', 'url': 'https://www.zomato.com/portland/fire-on-the-mountain-buffalo-wings-burnside-kerns?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
        'location': '1708 East Burnside Street 97214', 'hours': '11 AM to 12 Midnight (Mon-Sun)', 'cuisine': 'BBQ, Burger, Bar Food'},
    {'name': 'Blue Star Donuts', 'url': 'https://www.zomato.com/portland/blue-star-donuts-portland?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1', 'location': '1237 SW Washington St, Portland 97205', 'hours': '7 AM to 7 PM (Mon-Fri),8 AM to 7 PM (Sat-Sun)', 'cuisine': 'Breakfast, Vegetarian, Donuts'}]
# print(len(RESTAURANTS))


# for x in CUISINE_CHOICES:
#     Cuisine.objects.create(options=x)  # error no 'objects' member

# for y in SETTING_CHOICES:
#     Setting.objects.create(options=y) 



#script to create restaurants in the database.  Adds required fields (name, website, location, hours) and then iterates through cuisines and adds them to the manytomany relatioships
# for z in RESTAURANTS:
#     r = Restaurant.objects.create(name=z['name'], website=z['url'], location=z['location'], hours=z['hours'])
#     cuisine_list = z['cuisine'].split(', ')
#     for a in cuisine_list:
#         r.cuisines.add(Cuisine.objects.get(options = a))

print("success")