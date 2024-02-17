import streamlit as st
from io import StringIO
import geojson as gj

def upload_polygons() -> dict:
    st.header("Upload a geojson file")
    st.write("Click next when file is successfully uploaded")

    uploaded_file = st.file_uploader("Upload GeoJSON file")

    if uploaded_file is not None:
        # To read file as bytes:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        geojson = gj.loads(string_data)

        # check the type is feature collection
        if geojson['type'] != 'FeatureCollection':
            st.error("Please upload a GeoJSON Feature Collection")
            return None
        
        # check the features are polygons
        for feature in geojson['features']:
            if feature['geometry']['type'] != 'Polygon':
                st.error("Please upload a GeoJSON Feature Collection containing only Polygons")
                return None
            
        # check the features have a name property
        for feature in geojson['features']:
            if 'name' not in feature['properties']:
                st.error("Please upload a GeoJSON Feature Collection containing features with a 'name' property")
                return None
            
        # filter so we only have name property
        geojson['features'] = [
            {
                'type': 'Feature',
                'properties': {
                    'name': feature['properties']['name']
                },
                'geometry': feature['geometry']
            } for feature in geojson['features']
        ]

        # return
        return geojson