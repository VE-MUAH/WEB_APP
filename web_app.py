# import streamlit as st
# import geopandas as gpd
# from streamlit_folium import st_folium
# import folium
# from folium.plugins import Geocoder, MiniMap, Fullscreen, Draw
# import pandas as pd

# # Streamlit page configuration
# st.set_page_config(page_title="Geospatial Web App: Shapefile Upload, Visualization, and Geoprocessing")
# st.title("Shapefile Upload, Visualization, and Geoprocessing")

# # # World data paths
# data_path = r"world_population (1).csv"
# data_json_path = r"world.geojson"

# # Load world data
# world_data = pd.read_csv(data_path)
# world_json = gpd.read_file(data_json_path)

# # Select a country
# st.write("## Select a country that your shapefile falls within.")
# countries = [""] + list(world_data["Country/Territory"].unique())
# selected_country = st.selectbox("Select a country:", countries)

# if selected_country:
#     # Filter the selected country's geometry
#     filtered_country = world_json[world_json["name"] == selected_country]

#     if filtered_country.empty:
#         st.error("Selected country geometry not found in the dataset.")
#         st.stop()

#     # Ensure valid geometries
#     filtered_country = filtered_country[filtered_country.is_valid]
#     centroid = filtered_country.to_crs(epsg=4326).centroid.iloc[0]

#     # centroid = filtered_country.geometry.centroid.to_crs(epsg=4326).iloc[0]

#     # Extract population and capital data
#     country_data = world_data[world_data["Country/Territory"] == selected_country].squeeze()

#     # Initialize map
#     m = folium.Map(location=[centroid.y, centroid.x], zoom_start=5)
#     folium.GeoJson(filtered_country.to_crs(epsg=4326), name="Country Boundary").add_to(m)

#     folium.Marker(
#         location=[centroid.y, centroid.x],
#         popup=f"Capital: {country_data['Capital']}",
#         icon=folium.Icon(color="green", icon="cloud")
#     ).add_to(m)

#     Geocoder().add_to(m)
#     Fullscreen().add_to(m)
#     MiniMap(position="bottomright").add_to(m)
#     Draw(export=True).add_to(m)

#     st.write(f"### Map of {selected_country}")
#     map_output = st_folium(m, width=700, height=500)

#     # Shapefile upload
#     st.write("## Upload your shapefile")
#     uploaded_files = st.file_uploader(
#         "Upload Shapefile components (.shp, .shx, .dbf, .prj)", type=["shp", "shx",'dbf', "prj"], accept_multiple_files=True
#     )

#     if uploaded_files:
#         # Validate uploaded files
#         uploaded_file_dict = {file.name.split('.')[-1]: file for file in uploaded_files}

        





#         required_extensions = ['shp', 'shx','dbf', 'prj']

#         if all(ext in uploaded_file_dict for ext in required_extensions):
#             with st.spinner("Processing shapefile..."):
#                 shapefile_gdf = gpd.read_file(uploaded_file_dict['shp'])

#                 if shapefile_gdf.crs is None or shapefile_gdf.crs.to_epsg() != 4326:
#                     shapefile_gdf = shapefile_gdf.to_crs(epsg=4326)

#                 folium.GeoJson(shapefile_gdf, name="Uploaded Shapefile").add_to(m)
#                 st.success("Shapefile uploaded and visualized successfully!")
#                 map_output = st_folium(m, width=700, height=500)

#                 # Geoprocessing: Buffer
#                 st.write("## Geoprocessing: Buffering")
#                 buffer_distance = st.number_input("Enter buffer distance (meters):", min_value=0, value=10000)

#                 if st.button("Apply Buffer"):
#                     with st.spinner("Applying buffer..."):
#                         metric_gdf = shapefile_gdf.to_crs(epsg=3857)
#                         buffered_gdf = metric_gdf.buffer(buffer_distance).to_crs(epsg=4326)
#                         folium.GeoJson(buffered_gdf, name="Buffered Geometry").add_to(m)
#                         map_output = st_folium(m, width=700, height=500)

#                 # Geoprocessing: Clip
#                 st.write("## Geoprocessing: Clipping")
#                 if st.button("Clip to Country Boundary"):
#                     with st.spinner("Clipping shapefile..."):
#                         clipped_gdf = gpd.overlay(shapefile_gdf, filtered_country, how='intersection')
#                         folium.GeoJson(clipped_gdf, name="Clipped Geometry").add_to(m)
#                         map_output = st_folium(m, width=700, height=500)
#         else:
#             st.error("Please upload all required shapefile components: .shp, .shx, .dbf, .prj")










import streamlit as st
import geopandas as gpd
from streamlit_folium import st_folium
import folium
from folium.plugins import Geocoder, MiniMap, Fullscreen, Draw
import pandas as pd
import tempfile
import os

# Streamlit page configuration
st.set_page_config(page_title="Geospatial Web App: Shapefile Upload, Visualization, and Geoprocessing")
st.title("Shapefile Upload, Visualization, and Geoprocessing")

# World data paths
data_path = r"world_population (1).csv"
data_json_path = r"world.geojson"

# Load world data
world_data = pd.read_csv(data_path)
world_json = gpd.read_file(data_json_path)

# Select a country
st.write("## Select a country that your shapefile falls within.")
countries = [""] + list(world_data["Country/Territory"].unique())
selected_country = st.selectbox("Select a country:", countries)

if selected_country:
    # Filter the selected country's geometry
    filtered_country = world_json[world_json["name"] == selected_country]

    if filtered_country.empty:
        st.error("Selected country geometry not found in the dataset.")
        st.stop()

    # Ensure valid geometries
    filtered_country = filtered_country[filtered_country.is_valid]
    centroid = filtered_country.centroid.to_crs(epsg=4326).iloc[0]


    

    # Extract population and capital data
    country_data = world_data[world_data["Country/Territory"] == selected_country].squeeze()

    # Initialize map
    m = folium.Map(location=[centroid.y, centroid.x], zoom_start=5)
    folium.GeoJson(filtered_country.to_crs(epsg=4326), name="Country Boundary").add_to(m)

    folium.Marker(
        location=[centroid.y, centroid.x],
        popup=f"Capital: {country_data['Capital']}",
        icon=folium.Icon(color="green", icon="cloud")
    ).add_to(m)

    Geocoder().add_to(m)
    Fullscreen().add_to(m)
    MiniMap(position="bottomright").add_to(m)
    Draw(export=True).add_to(m)

    st.write(f"### Map of {selected_country}")
    map_output = st_folium(m, width=700, height=500)

    # Shapefile upload
    st.write("## Upload your shapefile")
    uploaded_files = st.file_uploader(
        "Upload Shapefile components (.shp, .shx, .dbf, .prj)", type=["shp", "shx", "dbf", "prj"], accept_multiple_files=True
    )

    if uploaded_files:
        # Validate uploaded files
        uploaded_file_dict = {file.name.split('.')[-1]: file for file in uploaded_files}

        required_extensions = ['shp', 'shx', 'dbf', 'prj']
        if all(ext in uploaded_file_dict for ext in required_extensions):
            with st.spinner("Processing shapefile..."):
                try:
                    # Create a temporary directory
                    with tempfile.TemporaryDirectory() as tmpdirname:
                        file_paths = {}

                        # Save uploaded files to temp directory
                        for ext, file in uploaded_file_dict.items():
                            file_path = os.path.join(tmpdirname, file.name)
                            file_paths[ext] = file_path
                            with open(file_path, "wb") as f:
                                f.write(file.getbuffer())

                        # Read the shapefile
                        shapefile_gdf = gpd.read_file(file_paths['shp'], driver="ESRI Shapefile")

                        # Reproject to EPSG:4326 if necessary
                        if shapefile_gdf.crs is None or shapefile_gdf.crs.to_epsg() != 4326:
                            shapefile_gdf = shapefile_gdf.to_crs(epsg=4326)

                        # Add to map
                        folium.GeoJson(shapefile_gdf, name="Uploaded Shapefile").add_to(m)
                        st.success("Shapefile uploaded and visualized successfully!")
                        map_output = st_folium(m, width=700, height=500)

                        # Geoprocessing: Buffer
                        st.write("## Geoprocessing: Buffering")
                        buffer_distance = st.number_input("Enter buffer distance (meters):", min_value=0, value=10000)

                        if st.button("Apply Buffer"):
                            with st.spinner("Applying buffer..."):
                                metric_gdf = shapefile_gdf.to_crs(epsg=3857)
                                buffered_gdf = metric_gdf.buffer(buffer_distance).to_crs(epsg=4326)
                                folium.GeoJson(buffered_gdf, name="Buffered Geometry").add_to(m)
                                map_output = st_folium(m, width=700, height=500)

                        # Geoprocessing: Clip
                        st.write("## Geoprocessing: Clipping")
                        if st.button("Clip to Country Boundary"):
                            with st.spinner("Clipping shapefile..."):
                                clipped_gdf = gpd.overlay(shapefile_gdf, filtered_country, how='intersection')
                                folium.GeoJson(clipped_gdf, name="Clipped Geometry").add_to(m)
                                map_output = st_folium(m, width=700, height=500)

                except Exception as e:
                    st.error(f"Error processing shapefile: {e}")

        else:
            st.error("Please upload all required shapefile components: .shp, .shx, .dbf, .prj")
