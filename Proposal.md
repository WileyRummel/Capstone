# Behind the counter (name pending)
### Wiley Rummel

A restaurant review system for the pros. Get reviews from certified service industry veterans.  Anonymous service scoring keeps reviews honest; industry knowledge keeps them worthwhile. 

>As a food lover I want to get restaurant reviews that I know I can trust without having to search through bad reviews from people who don’t know what they’re talking about.

## Objectives & Tasks
Allow users to sign up.  After signing up, users must pass a simple quiz on their industry knowledge if they wish to comment.  If a user scores over 70% they pass, otherwise they are restricted from reviewing until they are able to pass the test.  After a quiz failure, users must wait 24 hours before testing again. 
Use Vomato API to create a restaurant database.  Show users default results based on current location(city,st or zip).
Allow certified users to add new restaurants that might not present.
Get users current location to generate default list to show on homepage and search results; can change search results based on user desired location.

## Models

1. Restaurants: 
- “Star” rating average
- location
- Reviews linked
- Cuisine
- Price
- Great for… ie: brunch, happy hour, quick, large groups, dive bar etc
2. Users
- Certified, boolean
- FOH or BOH (for more review data)
- Current work (to prevent self review, hidden)
- Can make reviews
3. Reviews
- Star rating
- Text body
- Great for (linked with restaurant model)
- Restaurant it is placed on

## Pages

1. Home Page:
- Displays 4 latest reviews based on current location. 
- Lets you search for a restaurant by name or top in area by rating or review or great for:...
- Login and signup options 

2. Login + Sign up
- Basic login for existing user
- Sign up below with the user models schema inputs.
- After enrolling you can take the quiz.  If fail must wait 24 hrs, then 48 hrs, then one month. 
- Quiz is multiple choice, 10 questions. 70% or above is a pass.  

3. Restaurant pages
- Default pic for the restaurant
- Average Score, FOH score, BOH score
- Location
- Reviews for the page ordered by recency
- Link to website or social 

4. User profile page
- Settings options
- Instructions on use
- Site Rules
- Ability to refer friends.  2 referrals results in no need to quiz. 

5. Search results page
- List of restaurants and their most recent review
- Clicking brings you to that restaurant's main page

## Timeline

### Milestone One

- Initiate backend with Django. 
- Create Restaurant Model.   
- Build Restaurant DataBase with models and migrate information from zomato API.  
- Create Users Model.  
- Create review Model.  
- Create basic website with forms to login and sign up and leave a review.

### Milestone Two

- Build certification system. 
- Design quiz and referral system in JS.  
- Design new restaurant form.  
- Fully style HTML pages: Home, Search, Quiz, Login/SignUp, User Profile. 
- Build restaurant list search engine and HTML. 

### Milestone Three

- Load home page on Geo location. 
- Style it up, make sure it is fully responsive.  
- Beta test quiz system, review system, user profiles and settings.  

### Milestone Four (stretch goals)

- Make a dark mode or themes?  
- Extension that links with Yelp? 
- Special forum for certified users to post especially bad Yelp/Google/TripAdvisor reviews. 
- Comment section to discuss.  Only visible when signed in and certified.   
