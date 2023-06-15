import datetime, math, time
from KalturaClient import *
from KalturaClient.Plugins.Core import *

def main():
    client = get_client()

    with open("delete_category.txt", mode="r", encoding="utf-8") as entry_list:
        category_id_list = entry_list.read().splitlines()

        move_entries_to_parent_category = KalturaNullableBoolean.FALSE_VALUE

        for category_id in category_id_list:
            delete_entry(client, category_id, move_entries_to_parent_category)

def delete_entry(client, category_id, move_entries_to_parent_category):
    try:
        result = client.category.delete(category_id, move_entries_to_parent_category);
        print(category_id,"deleted");

    except Exception as e:
        print(category_id,"not found")

def get_client():
    config = KalturaConfiguration()
    config.serviceUrl = "https://admin.kaltura.com/"
    client = KalturaClient(config)

    ks = client.session.start(
      "[KALTURA_API_KEY]",
      None,
      KalturaSessionType.ADMIN,
      [PID],
      432000,
	"appID:delete-cat"
      )
    client.setKs(ks)

    return client

main()
