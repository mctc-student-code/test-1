import requests 

key = 'ef91173b22c5b1d7dfd312d644f3d9aa'

# Docs at https://www.flickr.com/services/api/explore/flickr.photos.search
# Search for egg pictures, modify to search for whatever tag you want

item = 'egg'

flickerSearchURL = 'https://api.flickr.com/services/rest/'

params = {
    'method': 'flickr.photos.search',
    'api_key': key,
    'text': item,
    'format': 'json',
    'nojsoncallback': '1',
    'sort': 'relevance'
}


# Search flickr for egg pictures
flickrResponse = requests.get(flickerSearchURL, params=params)
# get json back
flickrResponseJson = flickrResponse.json()

# Get first json object ('photos') which contains another json object ('photo') which is an json array; each
# element represents one photo. Take element 0

firstResponsePhoto = flickrResponseJson['photos']['photo'][0]
print(firstResponsePhoto)  #Just checking we get the JSON we expect

# deal with this in the following way. 

# Extract the secret, server, id and farm; which you need to construct another URL to request a specific photo
# https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg

secret = firstResponsePhoto['secret']
photo_id = firstResponsePhoto['id']
server = firstResponsePhoto['server']
farm = firstResponsePhoto['farm']

# TODO add error handing

fetchPhotoURL = f'https://farm{farm}.staticflickr.com/{server}/{photo_id}_{secret}_m.jpg' 
print(fetchPhotoURL)   # Again, just checking

photo_response = requests.get(fetchPhotoURL)

filename = 'egg.jpeg'

with open(filename, 'wb') as f:
    for chunk in photo_response.iter_content():
        f.write(chunk)

print('Photo saved to ' + filename)