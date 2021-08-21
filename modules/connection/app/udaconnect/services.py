import logging
from datetime import datetime, timedelta
from typing import Dict, List
import requests

from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema
from app.udaconnect.models import Person, Location, Connection


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

BASE_LOCATION_SVC_URL="http://udaconnect-location:5000"
BASE_PERSON_SVC_URL="http://udaconnect-person:5000"


class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5
    ) -> List[Connection]:
        """
        Finds all Person who have been within a given distance of a given Person within a date range.

        This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        smoothly for a better user experience for API consumers?
        """
        r = requests.get(BASE_PERSON_SVC_URL+"/api/persons")
        persons_list = r.json()
        print(persons_list)
        person_map: Dict[str, Person] = {person["id"]: person for person in persons_list}
        
        location_request = requests.get(BASE_LOCATION_SVC_URL+"/api/locations/connection/%s"% person_id, params= dict(
            start_date=start_date.strftime("%Y-%m-%d"), end_date=end_date.strftime("%Y-%m-%d"), meters=meters
        ))
        r = location_request
        connection_location_data = location_request.json()

        result: List[Connection] = []
        for location in connection_location_data:
            result.append(
                Connection(
                    person=person_map[location["person_id"]], location=location,
                )
            )

        return result

