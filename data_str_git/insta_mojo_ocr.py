import httplib, urllib, base64, json

###############################################

#### Update or verify the following values. ###

###############################################

# Replace the subscription_key string value with your valid subscription key.

subscription_key = '019387af67f141fab8ff516cef022450'

# Replace or verify the region.

#

# You must use the same region in your REST API call as you used to obtain your subscription keys.

# For example, if you obtained your subscription keys from the westus region, replace 

# "westcentralus" in the URI below with "westus".

#

# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using

# a free trial subscription key, you should not need to change this region.

uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {

    # Request headers.

    'Content-Type': 'application/json',

    'Ocp-Apim-Subscription-Key': subscription_key,

}

params = urllib.urlencode({

    # Request parameters. The language setting "unk" means automatically detect the language.

    'language': 'unk',

    'detectOrientation ': 'true',

})

# The URL of a JPEG image containing text.

body = "{'url':'http://www.charteredclub.com/wp-content/uploads/2013/04/PAN-CARD.jpg'}"

import ipdb;ipdb.set_trace()
try:

    # Execute the REST API call and get the response.

    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')

    conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)

    response = conn.getresponse()

    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.

    parsed = json.loads(data)

    print ("Response:")

    print (json.dumps(parsed, sort_keys=True, indent=2))

    conn.close()

except Exception as e:

    print('Error:')

    print(e)

####################################


