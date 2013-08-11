import urllib2
import os

def Download(url, out_folder):
    """Downloads the image which has the URL url to the folder out_folder."""
    
    filename = "2.png"
    
    outpath = os.path.join(out_folder, filename)
    
    if url.lower().startswith("http"):
        
        urlretrieve(url, outpath)
    else:
        
        urlretrieve(urlparse.urlunparse(parsed), outpath)
