import folium
from folium.plugins import HeatMap, FastMarkerCluster
import pandas as pd
from folium import LayerControl, FeatureGroup

# Load the CSV data for coordinates and consultant counts
coords_df = pd.read_csv('bailey_consultants.csv')

# Full consultant data
consultant_data = [
    {"Prefix": "", "Last Name": "Austin", "First Name": "Sabrina", "Primary Subject": "Math", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "662-609-0890", "Email": "SabrinaAustin.BaileyEd@gmail.com", "State": "MS", "City": "Batesville", "Tutoring": "Maybe", "Training": "Both"},
    {"Prefix": "", "Last Name": "Bennett", "First Name": "Sally", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "501-454-5093", "Email": "sallyeudybennett@gmail.com", "State": "AR", "City": "Joiner", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Blalock", "First Name": "Joanne", "Primary Subject": "SPED", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "501-605-6403", "Email": "jmblalock185@gmail.com", "State": "AR", "City": "Ward", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Bradford", "First Name": "Rhonda", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "501-472-0539", "Email": "bradford4445@gmail.com", "State": "AR", "City": "Little Rock", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Carlton", "First Name": "Angie", "Primary Subject": "Math", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "870-810-2280", "Email": "acarlton.beg@gmail.com", "State": "AR", "City": "Bono", "Tutoring": "", "Training": ""},
    {"Prefix": "Dr.", "Last Name": "Clark", "First Name": "Chelsea", "Primary Subject": "ELA (Secondary)", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "662-934-9538", "Email": "chelseaaustinclark@gmail.com", "State": "AR", "City": "Rector", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Crooks", "First Name": "Bridgette", "Primary Subject": "ELA (Elementary)", "Other Subject 1": "SPED", "Other Subject 2": "", "Mobile": "318-584-3918", "Email": "bcrooks2008@gmail.com", "State": "AR", "City": "Hot Springs", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Davis", "First Name": "Dee", "Primary Subject": "Leadership", "Other Subject 1": "ELA", "Other Subject 2": "", "Mobile": "870-489-5940", "Email": "deedavis.beg@gmail.com", "State": "AR", "City": "Pine Bluff", "Tutoring": "", "Training": "Yes Math"},
    {"Prefix": "", "Last Name": "Faught", "First Name": "Danielle", "Primary Subject": "ELA (K-5)", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "501-282-4991", "Email": "Danielle.faught@gmail.com", "State": "AR", "City": "Hot Springs", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Gibson", "First Name": "Debbie", "Primary Subject": "Math", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "501-679-1366", "Email": "gibsondebbie532@gmail.com", "State": "AR", "City": "Greenbrier", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Gotcher", "First Name": "Laura", "Primary Subject": "Math", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "", "Email": "lauraleegotcher@gmail.com", "State": "AR", "City": "Russellville", "Tutoring": "Yes", "Training": ""},
    {"Prefix": "Dr.", "Last Name": "Gotcher", "First Name": "Mark", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "479-970-1082", "Email": "mlgotcher@gmail.com", "State": "AR", "City": "Russellville", "Tutoring": "Yes", "Training": "Needs Training"},
    {"Prefix": "", "Last Name": "Guy", "First Name": "Terri", "Primary Subject": "Leadership", "Other Subject 1": "ELA", "Other Subject 2": "", "Mobile": "501-557-8749", "Email": "terriguy7007@gmail.com", "State": "AR", "City": "Mabelvale", "Tutoring": "", "Training": "Available on Mondays and Fridays"},
    {"Prefix": "", "Last Name": "Havens", "First Name": "Sarah", "Primary Subject": "ELA (Elem/Middle)", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "501-581-1456", "Email": "tshavens14@gmail.com", "State": "AR", "City": "Greenbrier", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Henry", "First Name": "Barbara", "Primary Subject": "ELA (Middle)", "Other Subject 1": "Math (Middle)", "Other Subject 2": "", "Mobile": "501-207-1415", "Email": "bhjr279@gmail.com", "State": "AR", "City": "McRae", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Howard-Moore", "First Name": "Meshunda", "Primary Subject": "Math", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "662-902-9282", "Email": "meshundahowardbeg@gmail.com", "State": "MS", "City": "Clarksdale", "Tutoring": "Yes", "Training": ""},
    {"Prefix": "", "Last Name": "Hurst", "First Name": "Sandra", "Primary Subject": "Leadership", "Other Subject 1": "Math (Middle)", "Other Subject 2": "", "Mobile": "501-259-8492", "Email": "shurst.baileyedgroup@gmail.com", "State": "AR", "City": "Little Rock", "Tutoring": "Yes", "Training": ""},
    {"Prefix": "", "Last Name": "Inman", "First Name": "Sarah", "Primary Subject": "Leadership", "Other Subject 1": "Math", "Other Subject 2": "", "Mobile": "870-489-7214", "Email": "sinman@baileyarch.com", "State": "", "City": "Hot Springs", "Tutoring": "", "Training": "Yes Math"},
    {"Prefix": "", "Last Name": "Jackson", "First Name": "Cortney", "Primary Subject": "Leadership", "Other Subject 1": "ELA", "Other Subject 2": "", "Mobile": "662-592-1608", "Email": "cjackson@baileyarch.com", "State": "MS", "City": "Clarksdale", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Jimerson", "First Name": "Kim", "Primary Subject": "ELA (Elem.)", "Other Subject 1": "Math (Elem.)", "Other Subject 2": "Pre-K", "Mobile": "501-593-3517", "Email": "kjimersonbaileycoach@gmail.com", "State": "AR", "City": " Searcy", "Tutoring": "No", "Training": "Yes Leadership"},
    {"Prefix": "Dr.", "Last Name": "Lawson", "First Name": "Jennifer", "Primary Subject": "Leadership", "Other Subject 1": "ELA", "Other Subject 2": "", "Mobile": "479-444-1400", "Email": "drlawson.baileyed@gmail.com", "State": "AR", "City": "Fayetteville", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Leuken", "First Name": "Rebecca", "Primary Subject": "SPED", "Other Subject 1": "ELA", "Other Subject 2": "Leadership", "Mobile": "501-690-4187", "Email": "rllueken1115@yahoo.com", "State": "AR", "City": "Greenbrier", "Tutoring": "", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Lindley", "First Name": "Rob", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "870-897-6387", "Email": "rlindley0316@gmail.com", "State": "AR", "City": "Rogers", "Tutoring": "Yes", "Training": "Yes ELA; Unavailable: May 5-16, June 16-20, July 7-10, Aug 13-Oct 3"},
    {"Prefix": "", "Last Name": "McCann", "First Name": "Terri", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "870-284-5485", "Email": "tdmccann84@gmail.com", "State": "AR", "City": "Harrisburg", "Tutoring": "Maybe", "Training": "Yes ELA"},
    {"Prefix": "Dr.", "Last Name": "McCullough", "First Name": "Merlina", "Primary Subject": "ELA", "Other Subject 1": "EL", "Other Subject 2": "Leadership", "Mobile": "870-656-9470", "Email": "mcculloughmerlina@gmail.com", "State": "AR", "City": "Salem", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "McDonald", "First Name": "Phyllis", "Primary Subject": "Leadership", "Other Subject 1": "ELA", "Other Subject 2": "K12 Literacy", "Mobile": "501-837-2938", "Email": "principal102002@yahoo.com", "State": "AR", "City": "Brinkley", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Mclaughlin", "First Name": "Kelly", "Primary Subject": "ELA", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "501-733-7163", "Email": "kellymc.consulting@gmail.com", "State": "AR", "City": "New Blaine", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Mitchell", "First Name": "Crystal", "Primary Subject": "Leadership", "Other Subject 1": "Math", "Other Subject 2": "", "Mobile": "501-553-3737", "Email": "crystal.a.mitchell@icloud.com", "State": "AR", "City": "Hensley", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "Dr.", "Last Name": "Nelson", "First Name": "Jennifer", "Primary Subject": "PreK", "Other Subject 1": "K12 Literacy", "Other Subject 2": "Leadership", "Mobile": "501-350-0086", "Email": "drjennifern.edconsultant@gmail.com", "State": "AR", "City": "Little Rock", "Tutoring": "Wants to sub for tutors initially", "Training": ""},
    {"Prefix": "", "Last Name": "Phillips", "First Name": "Annette", "Primary Subject": "ELA", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "870-350-1339", "Email": "web_teach@hotmail.com", "State": "AR", "City": "Green Forest", "Tutoring": "Yes", "Training": ""},
    {"Prefix": "Dr.", "Last Name": "Ray", "First Name": "Joshua", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "479-221-1670", "Email": "jray711@gmail.com", "State": "AR", "City": "Fort Smith", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Riley", "First Name": "Amy", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "479-899-1227", "Email": "", "State": "AR", "City": "", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Simpson", "First Name": "Monica Nicole", "Primary Subject": "ELA", "Other Subject 1": "Science", "Other Subject 2": "Leadership", "Mobile": "501-786-8748", "Email": "instructionalcoachmonica@gmail.com", "State": "AR", "City": "Little Rock", "Tutoring": "Yes", "Training": "Yes ELA"},
    {"Prefix": "", "Last Name": "Swanigan", "First Name": "Lindsey", "Primary Subject": "Math", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "501-215-9046", "Email": "mcdlindsey4@gmail.com", "State": "", "City": "", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Swofford", "First Name": "Kelly", "Primary Subject": "Leadership", "Other Subject 1": "Math (K-8)", "Other Subject 2": "", "Mobile": "870-654-5004", "Email": "kswofford1@gmail.com", "State": "AR", "City": "Berryville", "Tutoring": "", "Training": "Yes Leadership"},
    {"Prefix": "", "Last Name": "Torrence", "First Name": "Venus", "Primary Subject": "ELA", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "501-940-6562", "Email": "VENUS.TORRENCE@GMAIL.COM", "State": "AR", "City": "Little Rock", "Tutoring": "No", "Training": ""},
    {"Prefix": "", "Last Name": "Verkler", "First Name": "Dawn", "Primary Subject": "Math", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "501-680-9993", "Email": "ddkverkler@yahoo.com", "State": "AR", "City": "Lonoke", "Tutoring": "Yes", "Training": ""},
    {"Prefix": "", "Last Name": "White", "First Name": "Kristen", "Primary Subject": "Secondary ELA", "Other Subject 1": "ELA", "Other Subject 2": "Gifted Ed", "Mobile": "501-802-1626", "Email": "kwhiteeducon@gmail.com", "State": "AR", "City": "Hot Springs", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "White", "First Name": "Katina", "Primary Subject": "Science", "Other Subject 1": "Math", "Other Subject 2": "", "Mobile": "501-310-7960", "Email": "katinawhite35@gmail.com", "State": "AR", "City": "Little Rock",  "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Williams", "First Name": "Jerrod", "Primary Subject": "Leadership", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "501-454-0148", "Email": "jkwilliamsconsultant@gmail.com", "State": "AR", "City": "Searcy", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Wilson", "First Name": "Kirsten", "Primary Subject": "Leadership", "Other Subject 1": "ELA", "Other Subject 2": "Math/Science (Elem and MS)", "Mobile": "254-744-0941", "Email": "teachkiwi@gmail.com", "State": "AR", "City": "Greenbrier", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Wooldridge", "First Name": "Laura", "Primary Subject": "ELA K12", "Other Subject 1": "Leadership", "Other Subject 2": "", "Mobile": "870-240-3374", "Email": "laurawooldridge.beg@gmail.com", "State": "AR", "City": "Paragould", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Wright", "First Name": "Kelly", "Primary Subject": "ELA (Elementary/Middle)", "Other Subject 1": "Social Studies (Middle)", "Other Subject 2": "", "Mobile": "479-841-1722", "Email": "kellyheslepwright@gmail.com", "State": "AR", "City": "Searcy", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Wright", "First Name": "Kim", "Primary Subject": "ELA", "Other Subject 1": "Leadership", "Other Subject 2": "MTSS", "Mobile": "501-743-0799", "Email": "kwright@baileyarch.com", "State": "AR", "City": "Cabot", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "York", "First Name": "Lisa", "Primary Subject": "Leadership", "Other Subject 1": "PreK", "Other Subject 2": "", "Mobile": "501-605-7589", "Email": "lyork1964@gmail.com", "State": "AR", "City": "Austin", "Tutoring": "", "Training": ""},
    {"Prefix": "", "Last Name": "Wade", "First Name": "Cindy", "Primary Subject": "Not onboarded", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "", "Email": "", "State": "AR", "City": "Fayetteville", "Tutoring": "", "Training": "Applied/Not onboarded"},
    {"Prefix": "", "Last Name": "Swickheimer", "First Name": "Francine", "Primary Subject": "Not onboarded", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "", "Email": "", "State": "AR", "City": "Helena/West Helena", "Tutoring": "", "Training": "Applied/Not onboarded"},
    {"Prefix": "", "Last Name": "Youngblood", "First Name": "Gayla", "Primary Subject": "Not onboarded", "Other Subject 1": "", "Other Subject 2": "", "Mobile": "", "Email": "", "State": "AR", "City": "DeQueen", "Tutoring": "", "Training": "Applied/Not onboarded"}
]

# Convert consultant data to DataFrame
consultants_df = pd.DataFrame(consultant_data)

# Filter for Arkansas consultants and remove incomplete entries
consultants_df = consultants_df[(consultants_df['State'] == 'AR') & (consultants_df['City'] != '')]

# Group consultants by city
grouped = consultants_df.groupby('City')

# Create a base map centered on Arkansas with professional tiles
arkansas_map = folium.Map(location=[34.8, -92.2], zoom_start=7, tiles='CartoDB Positron')

# Create feature groups
heat_layer = FeatureGroup(name='Consultant Density', show=True)
marker_layer = FeatureGroup(name='Consultant Locations', show=True)

# Add heat map with default gradient
heat_data = [[row['Latitude'], row['Longitude'], row['Consultants']] for index, row in coords_df.iterrows()]
HeatMap(
    heat_data,
    min_opacity=0.5,
    radius=15,
    blur=10,
    max_zoom=10
).add_to(heat_layer)

# Function to create HTML table for popup with subject summary
def create_popup_html(city, group):
    # Count primary subjects
    subject_counts = group['Primary Subject'].value_counts().to_dict()
    subject_summary = ", ".join([f"{subject}: {count}" for subject, count in subject_counts.items()])
    
    # Start HTML
    html = f"""
    <div style='font-family:Arial,sans-serif; max-height:400px; overflow-y:auto;'>
        <h4>{city}</h4>
        <p><b>Consultants:</b> {len(group)}<br><b>Subjects:</b> {subject_summary}</p>
        <table style='width:100%; border-collapse:collapse; font-size:11px;'>
            <tr style='background:#2b3e50; color:white;'>
                <th style='padding:5px;'>Name</th>
                <th style='padding:5px;'>Primary Subject</th>
                <th style='padding:5px;'>Other Subjects</th>
                <th style='padding:5px;'>Mobile</th>
                <th style='padding:5px;'>Email</th>
                <th style='padding:5px;'>Tutoring</th>
                <th style='padding:5px;'>Training/Notes</th>
            </tr>
    """
    # Add consultant rows with alternating colors
    for i, (_, row) in enumerate(group.iterrows()):
        name = f"{row['Prefix']} {row['First Name']} {row['Last Name']}".strip()
        other_subjects = f"{row['Other Subject 1']}, {row['Other Subject 2']}".strip(', ')
        bg_color = '#f9f9f9' if i % 2 == 0 else '#ffffff'
        html += f"""
            <tr style='background:{bg_color};'>
                <td style='padding:5px;'>{name}</td>
                <td style='padding:5px;'>{row['Primary Subject']}</td>
                <td style='padding:5px;'>{other_subjects}</td>
                <td style='padding:5px;'>{row['Mobile']}</td>
                <td style='padding:5px;'>{row['Email']}</td>
                <td style='padding:5px;'>{row['Tutoring']}</td>
                <td style='padding:5px;'>{row['Training']}</td>
            </tr>
        """
    html += "</table></div>"
    return html

# Add markers with popups and tooltips
for city in coords_df['City']:
    city_data = grouped.get_group(city) if city in grouped.groups else None
    if city_data is not None:
        lat = coords_df[coords_df['City'] == city]['Latitude'].iloc[0]
        lon = coords_df[coords_df['City'] == city]['Longitude'].iloc[0]
        popup_html = create_popup_html(city, city_data)
        folium.CircleMarker(
            location=[lat, lon],
            radius=7,
            color='#2b3e50',
            weight=2,
            fill=True,
            fill_color='#2b3e50',
            fill_opacity=0.8,
            popup=folium.Popup(popup_html, max_width=700),
            tooltip=city
        ).add_to(marker_layer)

# Add feature groups to the map
heat_layer.add_to(arkansas_map)
marker_layer.add_to(arkansas_map)

# Add layer control
LayerControl().add_to(arkansas_map)

# Add title and logo placeholder
title_html = '''
    <div style='background:#2b3e50; color:white; padding:10px; text-align:center; font-family:Arial,sans-serif; box-shadow:0 2px 4px rgba(0,0,0,0.2);'>
        <img src='https://via.placeholder.com/50' style='float:left; margin-right:10px;' alt='Logo'>
        <h3 style='margin:0; font-size:18px;'>Bailey Consultants Heat Map (Arkansas, 2025-2026)</h3>
    </div>
'''
arkansas_map.get_root().html.add_child(folium.Element(title_html))

# Add legend
legend_html = '''
    <div style='position:fixed; bottom:10px; left:10px; background:white; padding:10px; border:1px solid #ccc; font-family:Arial,sans-serif; font-size:12px; box-shadow:0 2px 4px rgba(0,0,0,0.2);'>
        <b>Legend</b><br>
        <span style='color:#0000ff;'>■</span> Low Density (1 consultant)<br>
        <span style='color:#00ffff;'>■</span> Low-Medium<br>
        <span style='color:#ffff00;'>■</span> Medium<br>
        <span style='color:#ff9900;'>■</span> Medium-High<br>
        <span style='color:#ff0000;'>■</span> High Density (6 consultants)<br>
        <span style='color:#2b3e50;'>●</span> Consultant Location
    </div>
'''
arkansas_map.get_root().html.add_child(folium.Element(legend_html))

# Add footer
footer_html = '''
    <div style='position:fixed; bottom:10px; right:10px; font-family:Arial,sans-serif; font-size:10px; color:#666;'>
        Data Source: Bailey Consultants 2025-2026 | Generated: May 5, 2025
    </div>
'''
arkansas_map.get_root().html.add_child(folium.Element(footer_html))

# Save the map
arkansas_map.save('bailey_consultants_heatmap.html')