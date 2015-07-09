import os, hashlib, sys, urllib2, time

''' 1 = File does not exist
    2 = Subtitle not found
'''
class utilities(object):
	def __init__(self, name):
		self.name = name
	def get_hash(self):
	    self.readsize = 64 * 1024
	    try:
		    with open(self.name, 'rb') as self.f:
		        self.size = os.path.getsize(self.name)
		        self.data = self.f.read(self.readsize)
		        self.f.seek(-self.readsize, os.SEEK_END)
		        self.data += self.f.read(self.readsize)
		    self.calHash = hashlib.md5(self.data).hexdigest()  
		    return 0
	    except IOError:
	    	return 1
	def get_subtitle(self):
		self.url = 'http://sandbox.thesubdb.com/?action=download&hash='+str(self.calHash)+'&language=en'
		self.opener = urllib2.build_opener()
		self.req = urllib2.Request(self.url)
		self.req.add_header('User-Agent', 'SubDB/1.0 (GetSubtitle/0.1; http://github.com/abhijh/getsubtitle)')
		try:
			self.subtitle = self.opener.open(self.req)
			return 0
		except (urllib2.HTTPError):
			return 2

	def write_subtitle(self):
		with open(self.name[0:-4]+'.srt','w') as self.file:
			self.file.write(self.subtitle.read())
		return 0