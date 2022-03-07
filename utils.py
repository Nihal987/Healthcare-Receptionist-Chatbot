import re

def extract_value(response):
    '''
    Function to parse the <proto.marshal.collections.maps.MapComposite> response object returned
    by DialogFlow
    I wrote this function because I could not find a method to extract the values from this kind of object in
    Google's documentation
    '''
    text_to_parse = str(response.query_result) #converting the response to a string
    
    d = dict() # Dictionary to hold the parameters in key value pairs
    key_pattern = "key: \"(.*?)\"" # Starting pattern of each key to be extracted
    value_pattern = "string_value: \"(.*?)\"" # Starting pattern of each value to be extracted

    while text_to_parse:
        key = re.search(key_pattern, text_to_parse)
        
        if key is None: # If no key is found that we means we have extracted all the attributes, then break
            break
        key = key.group(1) # To extract the string value of the key
        value = re.search(value_pattern, text_to_parse).group(1)
        d[key] = value
        text_to_parse = text_to_parse[text_to_parse.find(value)+len(value):]
    
    return d