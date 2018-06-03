

# Created by Sachin Dev on 01/06/18
import datetime
import uuid
import models.alerts.constants as AlertConstants
import requests

from common.database import Database
from models.items.item import Item


class Alert(object):
    def __init__(self, user_email, price_limit, item_id, last_checked=None, _id=None):
        self.user_email = user_email
        self.price_limit = price_limit
        self.item = Item.get_by_id(item_id)
        self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Alert for {} on item {} with price {}>".format(self.user_email, self.item.name, self.price_limit)

    def send(self):
        return requests.post(
            AlertConstants.URL,
            auth={"api", AlertConstants.API_KEY},
            data={
                "from": AlertConstants.FROM,
                "to": self.user_email,
                "subject": "Price list reached for {}".format(self.item.name),
                "text": "We've found a deal! (link)."
            }
        )
    @classmethod
    def find_needing_update(cls, minutes_since_last_update=AlertConstants.ALERT_TIMEOUT):
        last_updated_limit = datetime.datetime.utcnow() - datetime.timedelta(minutes=0)
        alertss= [cls(**elm) for elm in Database.find(AlertConstants.COLLECTION,
                                                    {"last_checked":
                                                            {"$lte": last_updated_limit}
                                                     })]
        print(alertss)
        return alertss

    def save_to_mongo(self):
        Database.update(AlertConstants.COLLECTION,{"_id": self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "last_checked": self.last_checked,
            "user_email": self.user_email,
            "item_id": self.item._id
        }

    def load_item_price(self):
        self.item.load_price()
        self.last_checked = datetime.datetime.utcnow()
        self.save_to_mongo()
        return self.item.price

    def send_email_if_price_reached(self):
        if self.item.price < self.price_limit:
            self.send()