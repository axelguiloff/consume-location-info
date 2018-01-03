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


asset_id = config['lumada']['asset_id']
topics = [("assets/" + asset_id + "/state/#", 0)]
# 	("assets/" + asset_id + "/+/#", 0),
# 	("assets/+/event/#", 0),

locationConsumer = LocationConsumer(config=config, topics=topics)
locationConsumer.connect()