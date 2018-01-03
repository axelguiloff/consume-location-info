import sys
import configparser
import io
from pathlib import Path
from lib.location_consumer import LocationConsumer;

# Read the configuration file
config_filepath = "config/config.ini"
if not Path(config_filepath).is_file():
	print("Please ensure config/config.ini exists")
	sys.exit()
config = configparser.ConfigParser()
config.read(config_filepath)

username = "consumer:USERCREDENTIALS.local," + config['lumada']['user']
asset_id = config['lumada']['asset_id']
topics = [("assets/" + asset_id + "/event/#", 0)]
# 	("assets/" + asset_id + "/+/#", 0),
# 	("assets/+/event/#", 0),

locationConsumer = LocationConsumer(host=config['lumada']['host'], username=username,
	password=config['lumada']['passwd'], asset_id=asset_id, topics=topics)
locationConsumer.connect()