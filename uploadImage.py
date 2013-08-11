import flickrapi
api_key = '6c7e4a6b845e110f2463517ed7150f4d'
api_secret='537f90a411930a06'
api_token='--your-token--'
flickr = flickrapi.FlickrAPI(api_key, api_secret, token=api_token)
def rec_cb(wid, context, x, y, selection, info,  time):
    filename= selection.data[7:-2]
    flickr.upload(filename=filename, is_public=0)
