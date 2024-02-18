#   Copyright ETH 2018 - 2023 Zürich, Scientific IT Services
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
#   
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from .attribute import AttrHolder
from .definitions import (
    get_method_for_entity,
    get_fetchoption_for_entity,
)
from .openbis_object import OpenBisObject
from .utils import VERBOSE


class Person(OpenBisObject):
    """managing openBIS persons"""

    def __init__(self, openbis_obj, data=None, **kwargs):
        self.__dict__["openbis"] = openbis_obj
        self.__dict__["a"] = AttrHolder(openbis_obj, "person")

        if data is not None:
            self.a(data)
            self.__dict__["data"] = data

        if kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def __dir__(self):
        """all the available methods and attributes that should be displayed
        when using the autocompletion feature (TAB) in Jupyter
        """
        return [
            "permId",
            "userId",
            "firstName",
            "lastName",
            "email",
            "registrator",
            "registrationDate",
            "space",
            "get_roles()",
            "assign_role(role, space)",
            "revoke_role(role)",
        ]

    def get_roles(self, **search_args):
        """Get all roles that are assigned to this person.
        Provide additional search arguments to refine your search.

        Usage::
            person.get_roles()
            person.get_roles(space='TEST_SPACE')
        """
        roles = self.openbis.get_role_assignments(person=self, **search_args)
        aa = roles.df


        method_name = get_method_for_entity('authorizationGroup', "search")
        fetchopts = {
            "@type": "as.dto.authorizationgroup.fetchoptions.AuthorizationGroupFetchOptions",
            "roleAssignments": {
                "@type": "as.dto.roleassignment.fetchoptions.RoleAssignmentFetchOptions",
            }
        }
        for option in ["space", "project", "user", "authorizationGroup", "registrator"]:
            fetchopts['roleAssignments'][option] = get_fetchoption_for_entity(option)
        search_criteria = {
            "@type": "as.dto.authorizationgroup.search.AuthorizationGroupSearchCriteria",
            "criteria": {
                "criteria": [
                    {
                        "fieldName": "userId",
                        "fieldType": "ATTRIBUTE",
                        "fieldValue": {
                            "value": self.userId,
                            "@type": "as.dto.common.search.StringEqualToValue",
                        },
                        "@type": "as.dto.person.search.UserIdSearchCriteria",
                    }
                ],
                "@type": "as.dto.person.search.PersonSearchCriteria",
                "operator": "AND",
            }
        }

        request = {
            "method": method_name,
            "params": [self.openbis.token, search_criteria, fetchopts],
        }
        response = self.openbis._post_request(self.openbis.as_v3, request)
        if len(response["objects"]) > 0:
            l = list(map(lambda x: x["roleAssignments"], response["objects"]))
            def flatten_concatenation(matrix):
                flat_list = []
                for row in matrix:
                    flat_list += row
                return flat_list


            roles.response["objects"] += flatten_concatenation(l)
            roles._clear_df()
        return roles

    def assign_role(self, role, **kwargs):
        try:
            self.openbis.assign_role(role=role, person=self, **kwargs)
            if VERBOSE:
                print(f"Role {role} successfully assigned to person {self.userId}")
        except ValueError as e:
            if "exists" in str(e):
                if VERBOSE:
                    print(f"Role {role} already assigned to person {self.userId}")
            else:
                raise ValueError(str(e))

    def revoke_role(self, role, space=None, project=None, reason="no reason specified"):
        """Revoke a role from this person."""

        techId = None
        if isinstance(role, int):
            techId = role
        else:
            query = {"role": role}
            if space is None:
                query["space"] = ""
            else:
                if isinstance(space, str):
                    query["space"] = space.upper()
                else:
                    query["space"] = space.code.upper()

            if project is None:
                query["project"] = ""
            else:
                if isinstance(project, str):
                    query["project"] = project.upper()
                else:
                    query["project"] = project.code.upper()

            # build a query string for dataframe
            querystr = " & ".join(f'{key} == "{value}"' for key, value in query.items())
            roles = self.get_roles().df
            if len(roles) == 0:
                if VERBOSE:
                    print(
                        f"Role {role} has already been revoked from person {self.code}"
                    )
                return
            techId = roles.query(querystr)["techId"].values[0]

        # finally delete the role assignment
        ra = self.openbis.get_role_assignment(techId)
        ra.delete(reason)
        if VERBOSE:
            print(f"Role {role} successfully revoked from person {self.code}")
        return

    def __str__(self):
        return f'{self.get("firstName")} {self.get("lastName")}'

    def delete(self, reason):
        raise ValueError("Persons cannot be deleted")

    def save(self):
        if self.is_new:
            request = self._new_attrs()
            resp = self.openbis._post_request(self.openbis.as_v3, request)
            if VERBOSE:
                print("Person successfully created.")
            new_person_data = self.openbis.get_person(resp[0]["permId"], only_data=True)
            self._set_data(new_person_data)
            return self

        else:
            request = self._up_attrs()
            self.openbis._post_request(self.openbis.as_v3, request)
            if VERBOSE:
                print("Person successfully updated.")
            new_person_data = self.openbis.get_person(self.permId, only_data=True)
            self._set_data(new_person_data)
