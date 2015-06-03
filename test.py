from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
# response = urllib.urlopen('https://gtfsrt.api.translink.com.au/feed')
# feed.ParseFromString(response.read())
feed.ParseFromString(open('feed').read())
print(feed.header)
for i, entity in enumerate(feed.entity):
	# if i == 1:
	# 	print(entity)
  if entity.HasField('trip_update'):
    print entity.trip_update