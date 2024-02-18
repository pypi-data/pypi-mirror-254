"""
Common functions for the API
"""
import json

URL = "https://api.api-onepiece.com/v2/"
ENDPOINTS = {
    "episodes": ["id", "count", "title", "saga_id", "arc_id", "arc_title", "saga_title"],
    "movies": ["id", "count", "title"],
    "tomes": ["id", "count", "title"],
    "chapters": ["id", "count", "title", "tome_id"],
    "arcs": ["id", "count", "title", "saga_id"],
    "sagas": ["id", "count", "title"],
    "hakis": ["id", "count", "name", "roman_name", "characters_id"],
    "characters": ["id", "count", "name", "job", "bounty", "status", "size", "crew_id", "fruit_id"],
    "dials": ["id", "count", "name", "type"],
    "luffy/gears": ["id", "count", "title"],
    "luffy/techniques": ["id", "count", "name", "translation", "gear_id"],
    "locates": ["id", "count", "name", "sea", "affiliation"],
    "fruits": ["id", "count", "type"],
    "swords": ["id", "count", "name", "type", "state"],
    "boats": ["id", "count", "name", "type", "crew_id", "captain_id"],
    "crews": ["id", "count", "name", "status", "yonko"],
}

STRING_SEARCHES = ["name", "job", "bounty", "status", "size",
                   "type", "roman_name", "sea", "affiliation", "title"]
ID_SEARCHES = ["saga_id", "arc_id", "characters_id",
                "gear_id", "tome_id", "fruit_id", "crew_id", "crew_id", "captain_id"]
NO_RESOURCE_SEARCHES = ["count", "yonko"]

AUTHORIZED_LANGS = ['fr', 'en']


def check_params(endpoint, search=None, resource=None):
    """
    Check if the parameters are valid for the API

    :param endpoint: The endpoint to check
    :param search: The search to check
    :param resource: The resource to check

    See ENDPOINTS in common.py for more information

    This function is supposed to be used only by build_url

    :return: None if the parameters are valid
    :raises ValueError: If the parameters are not valid
    """
    endpoint_no_lang = endpoint.split('/')[0]
    if endpoint_no_lang not in ENDPOINTS:
        raise ValueError(f"Unknown API endpoint '{endpoint_no_lang}', authorized endpoints are {[key for key in ENDPOINTS]}")
    if search is not None and search not in ENDPOINTS[endpoint_no_lang]:
        raise ValueError(f"Unknown search '{search}' for endpoint '{endpoint_no_lang}', authorized searches are {[key for key in ENDPOINTS[endpoint_no_lang]]}")
    if search is not None and search not in NO_RESOURCE_SEARCHES and resource is None:
        raise ValueError("Resource is required for this search")
    if search in [NO_RESOURCE_SEARCHES] and resource is not None:
        raise ValueError("Resource is not required for this search")
    if resource is not None and "id" in search and not isinstance(resource, int):
        raise ValueError("Resource must be an integer for this search")


def build_url(endpoint, search=None, resource=None):
    """
    Build the url for the API

    :param endpoint: The endpoint to build the url for
    :param search: The search to build the url for
    :param resource: The resource to build the url for

    See ENDPOINTS in common.py for more information

    :return: The url for the API
    """
    check_params(endpoint, search, resource)
    if search is not None:
        if resource is not None:
            resource = convert_resource(resource)
            return adding_search(endpoint, search, resource)
        return f"{URL}{endpoint}/{search}"
    return f"{URL}{endpoint}"


def adding_search(endpoint, search, resource=None):
    """
    Add the search to the url

    See https://api-onepiece.com/documentation for more information about URL

    This functions is supposed to be used only by build_url

    :param endpoint: The endpoint to add the search to
    :param search: The search to add
    :param resource: The resource to add

    :return: The url with the search added
    """
    # there are some exceptions to the rule because of the API
    if search in STRING_SEARCHES:
        return f"{URL}{endpoint}/search/?{search}={resource}"

    if search in ID_SEARCHES:
        return f"{URL}{endpoint}/{search[:-3]}/{resource}/"

    return f"{URL}{endpoint}/{resource}"


def convert_resource(resource):
    """
    Convert the resource to a valid url for exceptions

    This function is supposed to be used only by build_url

    :param resource: The resource to convert
    :return: The converted resource
    """
    if isinstance(resource, int):
        return resource
    # If the character name contains a slash, we only want the first part
    if ' / ' in resource:
        resource = resource.split(" / ")[0]
    return resource.replace(" ", "%20")


def pretty_print(data):
    """
    Pretty print the data
    """
    def convert_to_dict(obj):
        return obj.__dict__

    json_string = json.dumps(
        data,
        indent=4,
        ensure_ascii=False,
        default=convert_to_dict).encode("utf8").decode()
    return json_string
