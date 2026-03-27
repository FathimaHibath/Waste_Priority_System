import streamlit as st
import os
from src.fill_level import estimate_fill_level
from src.predictor import predict_waste
from src.decomposition import calculate_decomposition_risk
from src.scoring import compute_priority, get_priority_label
import pandas as pd
from datetime import datetime, timedelta
# from datetime import datetime
import math


from streamlit_geolocation import streamlit_geolocation

# location = streamlit_geolocation()

# if location:
#     st.write(location["latitude"], location["longitude"])

# Schedule date for collection
def get_scheduled_date(priority_label):
    today = datetime.now().date()

    if priority_label == "Collect Immediately !":
        return today
    elif priority_label == "Schedule Collection !":
        return today + timedelta(days=1)
    else:
        return today + timedelta(days=3)


st.title("AI-Based Waste Collection Decision Support System")

WORKERS = [
    {"name": "Team A", "lat": 10.0159, "lon": 76.3419},  # Ernakulam
    {"name": "Team B", "lat": 11.2588, "lon": 75.7804},  # Kozhikode
    {"name": "Team C", "lat": 13.0827, "lon": 80.2707},  # Chennai
]

# def assign_worker(location):
#     location = location.lower()

#     for worker in WORKERS:
#         if worker["area"].lower() in location:
#             return worker["name"]

#     return "Team D"



def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def assign_nearest_worker(user_lat, user_lon):
    min_distance = float("inf")
    assigned_worker = None

    for worker in WORKERS:
        distance = calculate_distance(
            user_lat, user_lon,
            worker["lat"], worker["lon"]
        )

        if distance < min_distance:
            min_distance = distance
            assigned_worker = worker["name"]

    return assigned_worker

uploaded_file = st.file_uploader("Upload Waste Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    os.makedirs("temp", exist_ok=True)
    image_path = os.path.join("temp", uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # location = st.text_input("Enter Waste Location")   #for location acknowledgement

    


    # st.image(image_path, caption="Uploaded Image", use_column_width=True)
    st.image(image_path, caption="Uploaded Image", use_column_width=True)

    # GPS
    st.subheader(" Capture Waste Location")

    geo_data = streamlit_geolocation()

    if geo_data and geo_data["latitude"] is not None:

        latitude = geo_data["latitude"]
        longitude = geo_data["longitude"]

        st.success(f"Location Captured: {latitude}, {longitude}")

        location_df = pd.DataFrame({
            "lat": [latitude],
            "lon": [longitude]
        })

        st.map(location_df)

    else:
        st.warning("Please allow location access in browser.")
        st.stop()


    fill_level = estimate_fill_level(image_path)

    waste_probs = predict_waste(image_path)

    # if waste_probs is None:
    #     st.error("Invalid image. Please upload a proper waste image.")
    #     st.stop()

    days = st.slider("Days Since Last Collection", 0, 7, 1)

    # location = st.text_input("Enter Waste Location")    #for accessing user request

    # decomposition_risk = calculate_decomposition_risk(waste_probs, days)
    decomposition_risk = calculate_decomposition_risk(days)

    priority_score = compute_priority(fill_level, waste_probs, decomposition_risk)

    priority_label = get_priority_label(priority_score)

    st.write("Fill Level:", fill_level)
    st.write("Decomposition Risk:", decomposition_risk)
    st.write("Priority Score:", priority_score)

    st.success(f"Priority Decision: {priority_label}")

    
# # Schedule date for collection
#     def get_scheduled_date(priority_label):
#         today = datetime.now().date()

#         if priority_label == "Collect Immediately !":
#             return today
#         elif priority_label == "Schedule Collection !":
#             return today + timedelta(days=1)
#         else:
#             return today + timedelta(days=3)



    if st.button("Submit Collection Request"):

        # if location_df == "":
        #     st.warning("Please enter location before submitting request.")
        # else:
        #     scheduled_date = get_scheduled_date(priority_label)

            # new_request = {
            #     "Location": location,
            #     "Fill_Level": fill_level,
            #     "Decomposition_Risk": decomposition_risk,
            #     "Priority_Score": priority_score,
            #     "Decision": priority_label,
            #     "Scheduled_Date": scheduled_date,
            #     "Timestamp": datetime.now()
            # }
            # assigned_worker = assign_worker(location_df)
            scheduled_date = get_scheduled_date(priority_label)
            assigned_worker = assign_nearest_worker(latitude, longitude)
            

            # new_request = {
            #     "Location": location_df,
            #     "Fill_Level": fill_level,
            #     "Decomposition_Risk": decomposition_risk,
            #     "Priority_Score": priority_score,
            #     "Decision": priority_label,
            #     "Scheduled_Date": scheduled_date,
            #     "Assigned_Worker": assigned_worker,
            #     "Status": "Pending",
            #     "Timestamp": datetime.now()
            # }

            new_request = {
                "Latitude": latitude,
                "Longitude": longitude,
                "Fill_Level": fill_level,
                "Decomposition_Risk": decomposition_risk,
                "Priority_Score": priority_score,
                "Decision": priority_label,
                "Scheduled_Date": scheduled_date,
                "Assigned_Worker": assigned_worker,
                "Status": "Pending",
                "Timestamp": datetime.now()
            }

            df = pd.DataFrame([new_request])

            if not os.path.exists("requests.csv"):
                df.to_csv("requests.csv", index=False)
            else:
                df.to_csv("requests.csv", mode="a", header=False, index=False)

            st.success("Collection request submitted successfully!")
    


# Dashboard Section

st.subheader(" Pending Collection Requests")

if os.path.exists("requests.csv"):
    requests_df = pd.read_csv("requests.csv")
    requests_df = requests_df.sort_values(by="Priority_Score", ascending=False)
    st.dataframe(requests_df, use_container_width=True)
else:
    st.info("No requests submitted yet.")

