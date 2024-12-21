# # import streamlit as st
# # import requests
# # from geopy.distance import geodesic

# # # Set page title and layout
# # st.set_page_config(page_title="Nearest Hotels Finder", layout="wide")
# # # st.header("Hello")
# # # Function to fetch user's current location
# # def get_current_location():
# #     try:
# #         location_data = requests.get("https://ipinfo.io/json").json()
# #         loc = location_data.get("loc", "0,0").split(",")
# #         return (float(loc[0]), float(loc[1]))
# #     except Exception as e:
# #         st.error("Could not fetch location. Please check your internet connection.")
# #         return None

# # # Function to find nearest hotels (dummy data for now)
# # def get_nearest_hotels(user_location):
# #     hotels = [
# #         {"name": "Hotel Sunshine", "location": (28.644800, 77.216721), "distance": 0},
# #         {"name": "City Inn", "location": (28.641800, 77.214721), "distance": 0},
# #         {"name": "Grand Palace", "location": (28.647800, 77.220721), "distance": 0}
# #     ]

# #     for hotel in hotels:
# #         hotel["distance"] = geodesic(user_location, hotel["location"]).kilometers

# #     return sorted(hotels, key=lambda x: x["distance"])

# # # Main App
# # st.title("Nearest Hotels Finder")
# # st.write("Find the nearest hotels based on your current location.")

# # # Get user's current location
# # user_location = get_current_location()

# # if user_location:
# #     st.success(f"Your current location: {user_location}")

# #     # Fetch and display nearest hotels
# #     hotels = get_nearest_hotels(user_location)

# #     st.header("Nearest Hotels:")
# #     for hotel in hotels:
# #         st.write(f"- **{hotel['name']}**: {hotel['distance']:.2f} km away")
# # else:
# #     st.warning("Unable to determine your location.")

# # # Footer
# # st.markdown("---")
# # st.write("Created with Streamlit | [GitHub](https://github.com) | [Contact](mailto:example@example.com)")
# # ----------------------------------------------------------------------------------------------------------------
# # v2
# # import streamlit as st
# # import requests
# # from geopy.distance import geodesic
# # import folium
# # from streamlit_folium import st_folium

# # # Set page title and layout
# # st.set_page_config(page_title="Nearest Hotels Finder", layout="wide")

# # # Function to fetch user's current location
# # def get_current_location():
# #     try:
# #         location_data = requests.get("https://ipinfo.io/json").json()
# #         loc = location_data.get("loc", "0,0").split(",")
# #         return (float(loc[0]), float(loc[1]))
# #     except Exception as e:
# #         st.error("Could not fetch location. Please check your internet connection.")
# #         return None

# # # Function to find nearest hotels (dummy data for now)
# # def get_nearest_hotels(user_location):
# #     hotels = [
# #         {"name": "Hotel Sunshine", "location": (28.644800, 77.216721), "distance": 0},
# #         {"name": "City Inn", "location": (28.641800, 77.214721), "distance": 0},
# #         {"name": "Grand Palace", "location": (28.647800, 77.220721), "distance": 0}
# #     ]

# #     for hotel in hotels:
# #         hotel["distance"] = geodesic(user_location, hotel["location"]).kilometers

# #     return sorted(hotels, key=lambda x: x["distance"])

# # # Function to display map with user and hotel locations
# # def create_map(user_location, hotels):
# #     m = folium.Map(location=user_location, zoom_start=15)
# #     # Add user location marker
# #     folium.Marker(user_location, popup="Your Location", icon=folium.Icon(color="blue")).add_to(m)
# #     # Add hotel markers
# #     for hotel in hotels:
# #         folium.Marker(
# #             hotel["location"], 
# #             popup=f"{hotel['name']} ({hotel['distance']:.2f} km)", 
# #             icon=folium.Icon(color="green")
# #         ).add_to(m)
# #     return m

# # # Main App
# # st.title("Nearest Hotels Finder")
# # st.write("Find the nearest hotels based on your current location.")

# # # Get user's current location
# # user_location = get_current_location()

# # if user_location:
# #     st.success(f"Your current location: {user_location}")

# #     # Fetch and display nearest hotels
# #     hotels = get_nearest_hotels(user_location)

# #     st.header("Nearest Hotels:")
# #     for hotel in hotels:
# #         st.write(f"- **{hotel['name']}**: {hotel['distance']:.2f} km away")

# #     # Display map
# #     st.header("Map View")
# #     map_ = create_map(user_location, hotels)
# #     st_folium(map_, width=700, height=500)
# # else:
# #     st.warning("Unable to determine your location.")

# # # Footer
# # st.markdown("---")
# # st.write("Created with Streamlit | [GitHub](https://github.com) | [Contact](mailto:example@example.com)")
# -----------------------------------------------------------------
# v3
import streamlit as st
import requests
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium

# Set page title and layout
st.set_page_config(page_title="Nearest Hotels Finder App", layout="wide")

# Function to fetch user's current location using GPS
def get_current_location():
    try:
        # JavaScript to get user location
        location = st.query_params().get("location")
        if not location:
            st.write("Enable location sharing and reload the page.")
            return

        coords = [float(coord) for coord in location.split(",")]
        return (coords[0], coords[1])
    except Exception as e:
        st.error("Could not fetch location.")
        return None

# Function to find nearest hotels (dummy data for now)
def get_nearest_hotels(user_location):
    hotels = [
        {"name": "Hotel Sunshine", "location": (28.644800, 77.216721), "distance": 0},
        {"name": "City Inn", "location": (28.641800, 77.214721), "distance": 0},
        {"name": "Grand Palace", "location": (28.647800, 77.220721), "distance": 0}
    ]

    for hotel in hotels:
        hotel["distance"] = geodesic(user_location, hotel["location"]).kilometers

    return sorted(hotels, key=lambda x: x["distance"])

# Function to display map with user and hotel locations
def create_map(user_location, hotels):
    m = folium.Map(location=user_location, zoom_start=15)
    # Add user location marker
    folium.Marker(user_location, popup="Your Location", icon=folium.Icon(color="blue")).add_to(m)
    # Add hotel markers
    for hotel in hotels:
        folium.Marker(
            hotel["location"], 
            popup=f"{hotel['name']} ({hotel['distance']:.2f} km)", 
            icon=folium.Icon(color="green")
        ).add_to(m)
    return m

# Main App
st.title("Nearest Hotels Finder")
st.write("Find the nearest hotels based on your current location.")

# Get user's current location
user_location = get_current_location()

if user_location:
    st.success(f"Your current location: {user_location}")

    # Fetch and display nearest hotels
    hotels = get_nearest_hotels(user_location)

    st.header("Nearest Hotels:")
    for hotel in hotels:
        st.write(f"- **{hotel['name']}**: {hotel['distance']:.2f} km away")

    # Display map
    st.header("Map View")
    map_ = create_map(user_location, hotels)
    st_folium(map_, width=700, height=500)
else:
    st.warning("Unable to determine your location.")

# Footer
st.markdown("---")

