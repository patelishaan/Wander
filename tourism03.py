import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import streamlit as st
from geopy.geocoders import Nominatim

def locator(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)

    if location:
        st.write(location.latitude, location.longitude)
        #return (location.latitude, location.longitude)

    else:
        st.write('location not found')
        return None


def predictions(user_input):

    stop_words = set(stopwords.words('english'))
    #feelings = str(input('how do you want to feel ?'))
    lowercase = user_input.lower()
    tokens = word_tokenize(lowercase)
    # print(tokens)
    wo_stopwords = []
    for word in tokens:
        if word not in stop_words:
            wo_stopwords.append(word)
    feelings_db = {
        "relaxed": ["Goa", "Kerala", "Pondicherry", "Alleppey", "Gokarna", "Coorg", "Varkala", "Kasol", "Tarkarli",
                    "Mahabalipuram"],
        "adventurous": ["Manali", "Leh", "Rishikesh", "Spiti Valley", "Andaman", "Auli", "Tawang", "Shillong",
                        "Mount Abu", "Kedarnath"],
        "solitude": ["Dharamshala", "Mussoorie", "Rishikesh", "Coorg", "Kasol", "Spiti Valley", "Tawang", "Sikkim",
                     "Almora", "Gulmarg"],
        "romantic": ["Udaipur", "Jaipur", "Agra", "Jaisalmer", "Mysore", "Shimla", "Nainital", "Ooty", "Kumarakom",
                     "Kodaikanal"],
        "cultural": ["Jaipur", "Varanasi", "Hampi", "Mysore", "Madurai", "Amritsar", "Kolkata", "Ahmedabad",
                     "Khajuraho", "Patna"],
        "spiritual": ["Varanasi", "Haridwar", "Rishikesh", "Amritsar", "Puri", "Bodh Gaya", "Tirupati", "Dwarka",
                      "Shirdi", "Ujjain"],
        "historic": ["Delhi", "Agra", "Jaipur", "Hampi", "Lucknow", "Hyderabad", "Aurangabad", "Kolkata", "Ahmedabad",
                     "Gwalior"],
        "festive": ["Kolkata", "Jaipur", "Mumbai", "Goa", "Varanasi", "Amritsar", "Bangalore", "Ahmedabad", "Pune",
                    "Chennai"],
        "nature": ["Munnar", "Ooty", "Shillong", "Cherrapunji", "Kodaikanal", "Nainital", "Ranikhet", "Gulmarg",
                   "Wayanad", "Pachmarhi"],
        "adrenaline": ["Leh", "Manali", "Rishikesh", "Auli", "Spiti Valley", "Tawang", "Kedarnath", "Ladakh", "Andaman",
                       "Zanskar"],
        "beaches": ["Goa", "Pondicherry", "Gokarna", "Alleppey", "Varkala", "Tarkarli", "Mahabalipuram", "Diu", "Puri",
                    "Kanyakumari"],
        "mountains": ["Manali", "Leh", "Dharamshala", "Mussoorie", "Nainital", "Gulmarg", "Shimla", "Darjeeling",
                      "Auli", "Gangtok"],
        "wildlife": ["Ranthambore", "Jim Corbett", "Kaziranga", "Sundarbans", "Gir", "Bandhavgarh", "Pench", "Periyar",
                     "Nagarhole", "Tadoba"],
        "honeymoon": ["Goa", "Udaipur", "Manali", "Shimla", "Munnar", "Ooty", "Kumarakom", "Coorg", "Pondicherry",
                      "Andaman"],
        "photography": ["Jodhpur", "Udaipur", "Varanasi", "Jaipur", "Agra", "Hampi", "Leh", "Spiti Valley",
                        "Rann of Kutch", "Tawang"],
        "offbeat": ["Ziro", "Chopta", "Spiti Valley", "Tawang", "Majuli", "Gurez Valley", "Mawlynnong", "Dholavira",
                    "Lepchajagat", "Auroville"],
        "luxury": ["Udaipur", "Jaipur", "Goa", "Mumbai", "New Delhi", "Jodhpur", "Ranthambore", "Kumarakom", "Kerala",
                   "Andaman"],
        "winter": ["Manali", "Gulmarg", "Auli", "Leh", "Nainital", "Shimla", "Darjeeling", "Srinagar", "Mussoorie",
                   "Tawang"],
        "urban" : ["Delhi", "Lucknow", "Shimla", "Mumbai", "Noida", "Bengaluru", "Kolkata"]
    }

    itinerary_db = {
        "Goa": [
            "Visit Calangute Beach",
            "Explore Fort Aguada",
            "Party at Baga Beach",
            "Visit Dudhsagar Falls",
            "Explore Basilica of Bom Jesus"
        ],
        "Kerala": [
            "Backwaters cruise in Alleppey",
            "Visit Munnar Tea Gardens",
            "Relax at Kovalam Beach",
            "Explore Thekkady Wildlife Sanctuary"
        ],
        "Pondicherry": [
            "Promenade Beach walk",
            "Visit Auroville",
            "Explore French Quarter",
            "Tour Sri Aurobindo Ashram"
        ],
        "Alleppey": [
            "Houseboat ride on the backwaters",
            "Explore Alappuzha Beach",
            "Visit Krishnapuram Palace",
            "Witness the snake boat races"
        ],
        "Gokarna": [
            "Relax at Om Beach",
            "Visit Mahabaleshwar Temple",
            "Explore Paradise Beach",
            "Trek along Gokarna Beach"
        ],
        "Coorg": [
            "Visit Abbey Falls",
            "Explore Nagarhole National Park",
            "Visit Namdroling Monastery",
            "Walk through coffee plantations"
        ],
        "Varkala": [
            "Relax at Varkala Beach",
            "Visit Janardanaswamy Temple",
            "Cliffside walk at Varkala",
            "Explore Kappil Beach"
        ],
        "Kasol": [
            "Trek to Kheerganga",
            "Visit Manikaran Sahib Gurudwara",
            "Explore Parvati Valley",
            "Camp at Chalal village"
        ],
        "Tarkarli": [
            "Snorkeling at Tarkarli Beach",
            "Visit Sindhudurg Fort",
            "Scuba diving near Devbagh Beach",
            "Explore Tsunami Island"
        ],
        "Mahabalipuram": [
            "Explore Shore Temple",
            "Visit Arjuna’s Penance",
            "Explore Pancha Rathas",
            "Relax at Mahabalipuram Beach"
        ],
        "Manali": [
            "Visit Solang Valley",
            "Trek to Rohtang Pass",
            "Explore Old Manali",
            "Adventure sports at Beas River"
        ],
        "Leh": [
            "Visit Pangong Lake",
            "Explore Thiksey Monastery",
            "Drive through Khardung La Pass",
            "Explore Nubra Valley"
        ],
        "Rishikesh": [
            "River rafting in the Ganges",
            "Visit Laxman Jhula",
            "Attend Ganga Aarti at Triveni Ghat",
            "Explore Beatles Ashram"
        ],
        "Spiti Valley": [
            "Trek to Chandratal Lake",
            "Visit Key Monastery",
            "Explore Dhankar Monastery",
            "Drive to Kunzum Pass"
        ],
        "Andaman": [
            "Scuba diving at Havelock Island",
            "Visit Cellular Jail",
            "Relax at Radhanagar Beach",
            "Explore Ross Island"
        ],
        "Auli": [
            "Skiing in Auli",
            "Trek to Gorson Bugyal",
            "Visit Auli Artificial Lake",
            "Ropeway ride from Joshimath"
        ],
        "Tawang": [
            "Visit Tawang Monastery",
            "Explore Sela Pass",
            "Trek to Bumla Pass",
            "Visit Nuranang Waterfall"
        ],
        "Shillong": [
            "Visit Elephant Falls",
            "Explore Umiam Lake",
            "Trek to Laitlum Canyons",
            "Visit Don Bosco Museum"
        ],
        "Mount Abu": [
            "Visit Dilwara Temples",
            "Explore Nakki Lake",
            "Sunset view from Sunset Point",
            "Trek to Guru Shikhar"
        ],
        "Kedarnath": [
            "Visit Kedarnath Temple",
            "Trek to Vasuki Tal",
            "Explore Gaurikund",
            "Trek to Chorabari Glacier"
        ],
        "Dharamshala": [
            "Visit Dalai Lama Temple Complex",
            "Explore Bhagsu Waterfall",
            "Trek to Triund Hill",
            "Explore Kangra Fort"
        ],
        "Mussoorie": [
            "Visit Kempty Falls",
            "Explore Gun Hill",
            "Stroll along Mall Road",
            "Visit Lal Tibba"
        ],
        "Sikkim": [
            "Visit Tsomgo Lake",
            "Explore Rumtek Monastery",
            "Trek to Nathula Pass",
            "Visit Gangtok"
        ],
        "Almora": [
            "Visit Kasar Devi Temple",
            "Explore Binsar Wildlife Sanctuary",
            "Walk through Bright End Corner",
            "Visit Nanda Devi Temple"
        ],
        "Gulmarg": [
            "Skiing at Gulmarg Ski Resort",
            "Gondola ride to Apharwat Peak",
            "Trek to Khilanmarg",
            "Visit St. Mary’s Church"
        ],
        "Udaipur": [
            "Visit City Palace",
            "Boat ride on Lake Pichola",
            "Explore Saheliyon ki Bari",
            "Tour Jag Mandir"
        ],
        "Jaipur": [
            "Visit Amer Fort",
            "Explore City Palace",
            "Admire Hawa Mahal",
            "Visit Jantar Mantar"
        ],
        "Agra": [
            "Visit the Taj Mahal",
            "Explore Agra Fort",
            "Stroll through Mehtab Bagh",
            "Visit Fatehpur Sikri"
        ],
        "Jaisalmer": [
            "Visit Jaisalmer Fort",
            "Camel safari in Sam Sand Dunes",
            "Explore Patwon Ki Haveli",
            "Visit Bada Bagh"
        ],
        "Mysore": [
            "Visit Mysore Palace",
            "Explore Chamundi Hills",
            "Stroll through Brindavan Gardens",
            "Tour St. Philomena's Church"
        ],
        "Shimla": [
            "Stroll along The Ridge",
            "Visit Jakhoo Temple",
            "Explore Christ Church",
            "Toy Train ride to Kalka"
        ],
        "Nainital": [
            "Boat ride on Naini Lake",
            "Trek to Naina Peak",
            "Visit Naina Devi Temple",
            "Explore Snow View Point"
        ],
        "Ooty": [
            "Visit Botanical Gardens",
            "Boat ride on Ooty Lake",
            "Explore Doddabetta Peak",
            "Visit Rose Garden"
        ],
        "Kumarakom": [
            "Backwaters cruise",
            "Visit Kumarakom Bird Sanctuary",
            "Relax at Vembanad Lake",
            "Explore Pathiramanal Island"
        ],
        "Kodaikanal": [
            "Visit Coaker's Walk",
            "Boat ride on Kodaikanal Lake",
            "Explore Pillar Rocks",
            "Trek to Dolphin’s Nose"
        ],
        "Varanasi": [
            "Ganga Aarti at Dashashwamedh Ghat",
            "Visit Kashi Vishwanath Temple",
            "Boat ride on the Ganges",
            "Explore Sarnath"
        ],
        "Hampi": [
            "Explore Virupaksha Temple",
            "Visit Vittala Temple",
            "Climb Matanga Hill",
            "Walk through the Royal Enclosure"
        ],
        "Madurai": [
            "Visit Meenakshi Temple",
            "Explore Thirumalai Nayakkar Mahal",
            "Visit Gandhi Memorial Museum",
            "Stroll through Alagar Kovil"
        ],
        "Amritsar": [
            "Visit Golden Temple",
            "Explore Jallianwala Bagh",
            "Wagah Border ceremony",
            "Visit Partition Museum"
        ],
        "Kolkata": [
            "Visit Victoria Memorial",
            "Explore Howrah Bridge",
            "Tour Indian Museum",
            "Walk through Park Street"
        ],
        "Ahmedabad": [
            "Visit Sabarmati Ashram",
            "Explore Adalaj Stepwell",
            "Walk through Kankaria Lake",
            "Tour Sidi Saiyyed Mosque"
        ],
        "Khajuraho": [
            "Explore the Western Group of Temples",
            "Visit Kandariya Mahadev Temple",
            "Tour Lakshmana Temple",
            "Visit the Archaeological Museum"
        ],
        "Patna": [
            "Visit Golghar",
            "Explore Patna Museum",
            "Stroll through Gandhi Maidan",
            "Visit Takht Sri Patna Sahib"
        ],
        "Haridwar": [
            "Attend Ganga Aarti at Har Ki Pauri",
            "Visit Mansa Devi Temple",
            "Explore Chandi Devi Temple",
            "Visit Rajaji National Park"
        ],
        "Puri": [
            "Visit Jagannath Temple",
            "Relax at Puri Beach",
            "Explore Konark Sun Temple",
            "Stroll through Narendra Tank"
        ],
        "Bodh Gaya": [
            "Visit Mahabodhi Temple",
            "Explore Bodhi Tree",
            "Visit Great Buddha Statue",
            "Tour Tibetan Monastery"
        ],
        "Tirupati": [
            "Visit Sri Venkateswara Temple",
            "Explore Talakona Waterfalls",
            "Stroll through Chandragiri Fort",
            "Visit Sri Padmavathi Ammavari Temple"
        ],
        "Dwarka": [
            "Visit Dwarkadhish Temple",
            "Explore Bet Dwarka Island",
            "Stroll along Dwarka Beach",
            "Visit Rukmini Devi Temple"
        ],
        "Shirdi": [
            "Visit Sai Baba Temple",
            "Explore Shani Shingnapur",
            "Visit Dwarkamai",
            "Stroll through Wet N Joy Water Park"
        ],
        "Ujjain": [
            "Visit Mahakaleshwar Temple",
            "Explore Kal Bhairav Temple",
            "Tour Ram Ghat",
            "Visit Jantar Mantar"
        ],
        "Delhi": [
            "Visit Qutub Minar",
            "Explore Red Fort",
            "Stroll through India Gate",
            "Tour Humayun’s Tomb"
        ],
        "Lucknow": [
            "Explore Bara Imambara",
            "Stroll through Rumi Darwaza",
            "Visit Hazratganj",
            "Tour the British Residency"
        ],
        "Hyderabad": [
            "Visit Charminar",
            "Explore Golconda Fort",
            "Stroll through Chowmahalla Palace",
            "Visit Hussain Sagar Lake"
        ],
        "Aurangabad": [
            "Visit Ajanta and Ellora Caves",
            "Explore Bibi Ka Maqbara",
            "Tour Daulatabad Fort",
            "Stroll through Panchakki"
        ],
        "Gwalior": [
            "Visit Gwalior Fort",
            "Explore Jai Vilas Palace",
            "Visit Sun Temple",
            "Stroll through Sas Bahu Temples"
        ],
        "Mumbai": [
            "Visit Gateway of India",
            "Stroll through Marine Drive",
            "Explore Elephanta Caves",
            "Visit Chhatrapati Shivaji Maharaj Vastu Sangrahalaya"
        ],
        "Bangalore": [
            "Visit Lalbagh Botanical Garden",
            "Explore Bangalore Palace",
            "Stroll through Cubbon Park",
            "Tour ISKCON Temple"
        ],
        "Pune": [
            "Visit Shaniwar Wada",
            "Explore Aga Khan Palace",
            "Stroll through Osho Ashram",
            "Visit Sinhagad Fort"
        ],
        "Chennai": [
            "Stroll along Marina Beach",
            "Visit Kapaleeshwarar Temple",
            "Explore Fort St. George",
            "Tour Government Museum"
        ],
        "Munnar": [
            "Visit Tea Museum",
            "Explore Eravikulam National Park",
            "Stroll through Mattupetty Dam",
            "Trek to Anamudi Peak"
        ],
        "Cherrapunji": [
            "Visit Nohkalikai Falls",
            "Explore Mawsmai Caves",
            "Stroll through Seven Sisters Falls",
            "Walk along Living Root Bridges"
        ],
        "Ranikhet": [
            "Explore Chaubatia Gardens",
            "Visit Jhula Devi Temple",
            "Trek to Majhkhali",
            "Stroll through Rani Jheel"
        ],
        "Wayanad": [
            "Trek to Chembra Peak",
            "Explore Edakkal Caves",
            "Stroll through Banasura Sagar Dam",
            "Visit Soochipara Falls"
        ],
        "Pachmarhi": [
            "Visit Bee Falls",
            "Explore Jata Shankar Cave",
            "Trek to Dhupgarh Peak",
            "Stroll through Apsara Vihar"
        ],
        "Diu": [
            "Relax at Nagoa Beach",
            "Explore Diu Fort",
            "Visit St. Paul’s Church",
            "Stroll through Naida Caves"
        ],
        "Kanyakumari": [
            "Visit Vivekananda Rock Memorial",
            "Explore Thiruvalluvar Statue",
            "Stroll through Kanyakumari Beach",
            "Visit Kanyakumari Temple"
        ],
        "Darjeeling": [
            "Visit Tiger Hill for sunrise",
            "Ride the Darjeeling Toy Train",
            "Explore Peace Pagoda",
            "Visit Batasia Loop"
        ],
        "Gangtok": [
            "Visit MG Marg",
            "Explore Rumtek Monastery",
            "Trek to Tsomgo Lake",
            "Tour Nathula Pass"
        ],
        "Ranthambore": [
            "Safari in Ranthambore National Park",
            "Explore Ranthambore Fort",
            "Visit Padam Talao",
            "Stroll through Rajbagh Ruins"
        ],
        "Jim Corbett": [
            "Safari at Corbett National Park",
            "Visit Corbett Museum",
            "Explore Garjiya Devi Temple",
            "Trek along Corbett Waterfalls"
        ],
        "Kaziranga": [
            "Elephant Safari in Kaziranga",
            "Jeep Safari in the central range",
            "Visit Kaziranga National Orchid Park",
            "Explore nearby tea gardens"
        ],
        "Sundarbans": [
            "Boat safari in Sundarbans National Park",
            "Visit Sajnekhali Bird Sanctuary",
            "Explore Sudhanyakhali Watch Tower",
            "Visit Dobanki Watch Tower"
        ],
        "Gir": [
            "Safari in Gir National Park",
            "Visit Gir Interpretation Zone",
            "Explore Somnath Temple",
            "Visit Kamleshwar Dam"
        ],
        "Bandhavgarh": [
            "Safari in Bandhavgarh National Park",
            "Explore Bandhavgarh Fort",
            "Visit Badi Gufa",
            "Trek to Shesh Shaiya"
        ],
        "Pench": [
            "Safari in Pench National Park",
            "Visit Pench Dam",
            "Explore Rukhad Wildlife Sanctuary",
            "Trek along Pench River"
        ],
        "Periyar": [
            "Boat safari in Periyar Lake",
            "Visit Periyar Wildlife Sanctuary",
            "Explore Mangala Devi Temple",
            "Trek through Periyar Tiger Trail"
        ],
        "Nagarhole": [
            "Safari in Nagarhole National Park",
            "Visit Iruppu Falls",
            "Explore Kabini River",
            "Trek to Brahmagiri Hill"
        ],
        "Tadoba": [
            "Safari in Tadoba Andhari Tiger Reserve",
            "Visit Tadoba Lake",
            "Explore Moharli and Kolsa zones",
            "Trek through Tadoba hills"
        ],
        "Ziro": [
            "Visit Talley Valley Wildlife Sanctuary",
            "Explore Ziro Puto",
            "Trek to Midey",
            "Attend Ziro Music Festival"
        ],
        "Chopta": [
            "Trek to Tungnath Temple",
            "Hike to Chandrashila Peak",
            "Visit Deoria Tal",
            "Stroll through Chopta Meadows"
        ],
        "Majuli": [
            "Visit Kamalabari Satra",
            "Explore Auniati Satra",
            "Stroll through Mishing Village",
            "Visit Majuli Mask Craft"
        ],
        "Gurez Valley": [
            "Trek to Habba Khatoon Peak",
            "Visit Dawar village",
            "Explore Wular Lake",
            "Stroll along Kishanganga River"
        ],
        "Mawlynnong": [
            "Walk along Living Root Bridges",
            "Visit Mawlynnong Village",
            "Explore Sky View Point",
            "Stroll through Cleanest Village"
        ],
        "Dholavira": [
            "Explore Dholavira Archaeological Site",
            "Visit Fossil Park",
            "Stroll through Rann of Kutch",
            "Visit Dholavira Museum"
        ],
        "Lepchajagat": [
            "Trek to Hawa Ghar",
            "Explore Simana View Point",
            "Visit Jorpokhri Wildlife Sanctuary",
            "Stroll through Ghoom Monastery"
        ],
        "Auroville": [
            "Visit Matrimandir",
            "Explore Auroville Beach",
            "Stroll through Auroville Botanical Gardens",
            "Tour the Auroville Bakery"
        ],
        "Jodhpur": [
            "Visit Mehrangarh Fort",
            "Explore Umaid Bhawan Palace",
            "Stroll through Jaswant Thada",
            "Tour Mandore Gardens"
        ],
        "Rann of Kutch": [
            "Visit White Desert",
            "Explore Kala Dungar",
            "Tour Kutch Museum",
            "Attend Rann Utsav"
        ],
        "Zanskar": [
            "Trek through Chadar Trek",
            "Visit Zanskar Monastery",
            "Explore Pensi La Pass",
            "Rafting in Zanskar River"
        ],
        "Auroville": [
            "Visit Matrimandir",
            "Explore Auroville Beach",
            "Stroll through Auroville Botanical Gardens",
            "Tour the Auroville Bakery"
        ]
    }

    # print(wo_stopwords)
    feelings = []
    for words in wo_stopwords:
        if words in feelings_db.keys():
            feelings.append(words)
    print(feelings)
    extnd_feels = feelings.copy()
    for items in feelings:
        for syn in wordnet.synsets(items):
            for lema in syn.lemmas():
                extnd_feels.append(lema.name())
            # feelings.append(syn.name())
    print(extnd_feels)

    destinatons = set()
    for feelings in extnd_feels:
        if feelings in feelings_db:
            destinatons.update(feelings_db[feelings])
        else:
            pass

    # print(destinatons)

    # Track destination frequency based on extended feelings
    destination_freq = {}
    for feeling in extnd_feels:
        if feeling in feelings_db:
            for city in feelings_db[feeling]:
                if city in destination_freq:
                    destination_freq[city] += 1
                else:
                    destination_freq[city] = 1

    # Sort destinations based on frequency
    sorted_destinations = sorted(destination_freq.items(), key=lambda x: x[1], reverse=True)

    # Print the top 10 destinations
    print("\nTop 5 destinations:")
    #if destinatons
    for destination, freq in sorted_destinations[:5]:
        #print(f"{destination}")
        #st.write(f"{destination}")
        with st.expander(destination):
            st.write(itinerary_db[destination])

    #mapp = st.text_input('which of the following cities would you like to visit ?')
    #if st.button('submit to get map'):
     #   locator(mapp)


st.title("Wander AI")
st.write('Find your way through India - and yourself')
user_input = st.text_input('how do you want to feel ?')
if st.button('submit'):
    predictions(user_input)

