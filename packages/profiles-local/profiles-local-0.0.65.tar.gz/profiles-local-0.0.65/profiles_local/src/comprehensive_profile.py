import json
from typing import Dict

from circles_local_aws_s3_storage_python import StorageConstants
from circles_local_aws_s3_storage_python.CirclesStorage import circles_storage
from database_mysql_local.to_sql_interface import Point
from email_address_local.email_address import EmailAddressesLocal
from gender_local.src.gender import Gender
from group_profile_remote.group_profile import GroupProfilesRemote
from language_local.lang_code import LangCode
from location_local.locations_local_crud import LocationsLocal
from logger_local.MetaLogger import MetaLogger
from operational_hours_local.src.operational_hours import OperationalHours
from profile_profile_local.src.profile_profile import ProfileProfile
from profile_reaction_local.src.profile_reaction import ProfileReactions
from reaction_local.src.reaction import Reaction

from .constants_profiles_local import PROFILE_LOCAL_PYTHON_LOGGER_CODE
from .profiles_local import ProfilesLocal


class ComprehensiveProfilesLocal(metaclass=MetaLogger, object=PROFILE_LOCAL_PYTHON_LOGGER_CODE):
    def __init__(self):
        self.location_local = LocationsLocal()
        self.profiles_local = ProfilesLocal()
        self.storage = circles_storage()
        self.gender = Gender()
        self.profile_profile = ProfileProfile()
        self.group_profiles_remote = GroupProfilesRemote()
        self.email_addresses_local = EmailAddressesLocal()
        self.operational_hours = OperationalHours()
        self.reaction = Reaction()

    def insert(self, profile_json: str, lang_code: LangCode) -> int:
        """Returns the profile_id of the inserted profile"""

        data = json.loads(profile_json)
        profile_id = location_id = None

        if "location" in data:
            location_entry: Dict[str, any] = data["location"]
            location_data: Dict[str, any] = {
                "coordinate": Point(longitude=location_entry["coordinate"].get("latitude"),
                                    latitude=location_entry["coordinate"].get("longitude")),
                "address_local_language": location_entry.get("address_local_language"),
                "address_english": location_entry.get("address_english"),
                "postal_code": location_entry.get("postal_code"),
                "plus_code": location_entry.get("plus_code"),
                "neighborhood": location_entry.get("neighborhood"),
                "county": location_entry.get("county"),
                "region": location_entry.get("region"),
                "state": location_entry.get("state"),
                "country": location_entry.get("country")
            }
            location_id = self.location_local.insert(data=location_data, lang_code=lang_code, is_approved=False)

        # Insert person to db
        if 'person' in data:
            # TODO person_entry -> person_dict
            person_entry: Dict[str, any] = data['person']

            # TODO I would expect the 1st thing we do with person_dict is "person: PersonLocal(person_dict)". Can we do this approach on all entities?

            # TODO: I prefer we use "person.getGender()"
            gender_id = self.gender.get_gender_id_by_title(person_entry.get('gender'))
            person_data: Dict[str, any] = {
                'last_coordinate': person_entry.get('last_coordinate'),
            }
            # TODO: Why do we need gender_id and person_data?
            # Person class has errors - TODO Let's fix them
            '''
            person_dto = PersonDto(
                gender_id, person_data.get('last_coordinate'),
                person_data.get('location_id'))

            # TODO We prefer PersonsLocal.insert(person) which updates both person_table and person_ml_table
            person_id = PersonsLocal.insert(person_dto)
            PersonsLocal.insert_person_ml(
                person_id,
                lang_code,
                person_data.get('first_name'),
                person_data.get('last_name'))
            '''

        # Insert profile to db
        if 'profile' in data and 'person_id' in data.get("person", {}):
            profile_entry: Dict[str, any] = data['profile']
            profile_json: Dict[str, any] = {
                'name': profile_entry.get('name'),
                'name_approved': profile_entry.get('name_approved'),
                'lang_code': profile_entry.get('lang_code'),
                'user_id': profile_entry.get('user_id'),
                'is_main': profile_entry.get('is_main'),
                'visibility_id': profile_entry.get('visibility_id'),
                'is_approved': profile_entry.get('is_approved'),
                'profile_type_id': profile_entry.get('profile_type_id'),
                # preferred_lang_code the current preferred language of the user in the specific profile.
                # Default: english
                'preferred_lang_code': profile_entry.get('preferred_lang_code', LangCode.ENGLISH.value),
                'experience_years_min': profile_entry.get('experience_years_min'),
                'main_phone_id': profile_entry.get('main_phone_id'),
                'is_rip': profile_entry.get('is_rip'),
                'gender_id': profile_entry.get('gender_id'),
                'stars': profile_entry.get('stars'),
                'last_dialog_workflow_state_id': profile_entry.get('last_dialog_workflow_state_id'),
                "about": profile_entry.get('about')
            }
            profile_id = self.profiles_local.insert(profile_json=profile_json,
                                                    person_id=data["person"]['person_id'])

        # insert profile_profile to db
        if 'profile_profile' in data:
            profile_profile_entry: Dict[str, any] = data['profile_profile']
            for i in profile_profile_entry:
                profile_profile_part_entry: Dict[str, any] = profile_profile_entry[i]
                profile_profile_data: Dict[str, any] = {
                    'profile_id': profile_profile_part_entry.get('profile_id'),
                    'relationship_type_id': profile_profile_part_entry.get('relationship_type_id'),
                    'job_title': profile_profile_part_entry.get('job_title', None)
                }
                profile_profile_id = self.profile_profile.insert_profile_profile(
                    profile_id1=profile_profile_data['profile_id'], profile_id2=profile_id,
                    relationship_type_id=profile_profile_data['relationship_type_id'],
                    job_title=profile_profile_data['job_title'])
                self.logger.info(object={"profile_profile_id": profile_profile_id})

        # insert group to db
        # TODO: uncomment section
        # if 'group' in keys:
        # group_entry: Dict[str, any] = data['group']
        # group_data: Dict[str, any] = {
        #     'title': group_entry.get('title'),
        #     'lang_code': group_entry.get('lang_code'),
        #     'parent_group_id': group_entry.get('parent_group_id'),
        #     'is_interest': group_entry.get('is_interest'),
        #     'image': group_entry.get('image', None),
        # }
        # group_id = GroupsRemote().create_group(group_data)

        # insert group_profile to db
        if 'group_profile' in data:
            group_profile_entry: Dict[str, any] = data['group_profile']
            group_profile_data: Dict[str, any] = {
                'group_id': group_profile_entry.get('group_id'),
                'relationship_type_id': group_profile_entry.get('relationship_type_id'),
            }
            group_profile_id = self.group_profiles_remote.create(
                group_id=group_profile_data['group_id'],
                relationship_type_id=group_profile_data['relationship_type_id'])
            self.logger.info(object={"group_profile_id": group_profile_id})

        # insert email to db
        if 'email' in data:
            email_entry: Dict[str, any] = data['email']
            email_address_data: Dict[str, any] = {
                'email_address': email_entry.get('email_address'),
                'lang_code': (email_entry.get('lang_code')),
                'name': email_entry.get('name'),
            }
            email_address_id = self.email_addresses_local.insert(
                email_address_data['email_address'], LangCode[email_address_data['lang_code']],
                email_address_data['name'])
            self.logger.info(object={"email_address_id ": email_address_id})

        # Insert storage to db
        if "storage" in data:
            storage_data = {
                "path": data["storage"].get("path"),
                "filename": data["storage"].get("filename"),
                "region": data["storage"].get("region"),
                "url": data["storage"].get("url"),
                "file_extension": data["storage"].get("file_extension"),
                "file_type": data["storage"].get("file_type")
            }
            if storage_data["file_type"] == "Profile Image":
                self.storage.save_image_in_storage_by_url(image_url=storage_data["url"],
                                                          local_filename=storage_data["filename"],
                                                          profile_id=profile_id,
                                                          entity_type_id=StorageConstants.PROFILE_IMAGE),

        # Insert reaction to db
        if "reaction" in data:
            reaction_json = {
                "value": data["reaction"].get("value"),
                "image": data["reaction"].get("image"),
                "title": data["reaction"].get("title"),
                "description": data["reaction"].get("description"),
            }
            # TODO Reaction is not only on profile_id, user can react on anything i.e. news, group, event ...
            #  We should provide a generic approach.
            #   remove profile_id parameter from reaction-local insert method
            # TODO: fix typing
            # TODO: Reaction -> ReactionsLocal
            reaction_id = self.reaction.insert(reaction_json, profile_id, lang_code)
            # Insert profile-reactions to db
            ProfileReactions.insert(reaction_id, profile_id)

        # Insert operational hours to db
        if "operational_hours" in data:
            operational_hours_list_of_dicts = OperationalHours.create_hours_array(
                data["operational_hours"])
            self.operational_hours.insert(profile_id, location_id, operational_hours_list_of_dicts)

        return profile_id
