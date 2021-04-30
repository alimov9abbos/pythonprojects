from pprint import pprint
import requests
import json

url_template = 'https://ws-public.interpol.int/notices/v1/red?&resultPerPage=20&page={page_number}'
# I want to traverse through pages 1-x
# All of the Json objects will be stored in a list.
json_list = []
for page_number in range(1, 8):
    # then change up the url format to fit the page, with the right page number
    url = url_template.format(page_number=page_number)
    # send a get request to each page
    resp = requests.get(url)
    # This is the whole json data for that page
    data = resp.json()
    # Now I want something more specific which is held by the key embedded further into the dictionary key notices
    # each object now has the json of all the notices on that page
    results = data['_embedded']['notices']
    # Now I want to traverse the list of notices
    for notice in results:
        # the notice's own page will be at the key _links
        links = notice['_links']
        # the page's json will be at key self at href
        page_link = links['self']['href']
        # And I want a deeper request for the individual notice json
        response = requests.get(page_link)
        #
        person_data = response.json()
        json_list.append(person_data)

# I will write all the jsons into one json file called notices.json
with open("notices.json", "w") as outfile:
    for item in json_list:
        json.dump(item, outfile)
        # make a new line to make it look better and more readable
        outfile.write("\n")
