from lu_vp_detect import VPDetection

length_thresh = 60 # Minimum length of the line in pixels
principal_point = None # Specify a list or tuple of two coordinates
                       # First value is the x or column coordinate, Second value is the y or row coordinate
focal_length = 1500 # Specify focal length in pixels
seed = None # Or specify whatever ID you want (integer)

vpd = VPDetection(length_thresh, principal_point, focal_length, seed)

# Provide a path to the image
img = 'test.png'

# Run detection
vps = vpd.find_vps(img)
# Access the image coordinates for the vanishing points
vps_2D = vpd.vps_2D

# Display vanishing points
print(vps)
print(vps_2D)