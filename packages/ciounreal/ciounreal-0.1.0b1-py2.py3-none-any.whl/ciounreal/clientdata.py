from ciocore import data as coredata

def fetch_projects():
    return coredata.data()["projects"]

def fetch_instance_types():

    result = []
    hardware = coredata.data().get("instance_types")
    for category in hardware.categories:
        for entry in category["content"]:
            if not (entry["operating_system"] == "windows" and entry.get("gpu")):
                continue
            result.append(entry["description"])
    return result