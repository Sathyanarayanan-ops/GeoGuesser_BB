base_url = "https://maps.googleapis.com/maps/api/streetview"
location = "latitude,longitude"  # Replace with desired latitude and longitude
size = "640x640"  # Replace with desired image size
heading = "0"  # Replace with desired heading
pitch = "0"  # Replace with desired pitch
api_key = "YOUR_API_KEY"  # Replace with your Google API key

image_url = f"{base_url}?size={size}&location={location}&heading={heading}&pitch={pitch}&key={api_key}"
