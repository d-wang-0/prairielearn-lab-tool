import requests, os, datetime, json

CONFIG_FILE = "config.json"

TWO_HOURS: float = datetime.timedelta(hours=2).total_seconds()

MIN_COL_WIDTH = 10

# Fancy colours
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# "open": bool
# "points": int
# "user_id": int
# "user_uid": str (cwl@ubc.ca)
# "user_name": str
# "user_role": str
# "max_points": int
# "score_perc": int
# "start_date": str
# "assessment_id": int
# "highest_score": bool
# "time_remaining": str
# "assessment_name": str
# "assessment_label": str
# "assessment_title": str
# "duration_seconds": float
# "assessment_number": str
# "assessment_instance_id": int
# "assessment_instance_number": int
# "assessment_set_abbreviation": str

def highlight(text: str) -> str:
    return bcolors.BOLD +bcolors.HEADER + text + bcolors.ENDC

def time_difference(start_time: str) -> float:
    date_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S-%f')
    difference = (datetime.datetime.now() - date_time).total_seconds()

    return difference


def highlight_search(text: str, search: str) -> str:
    if len(search) > 0 and search.lower() in text.lower():
        return highlight(text)
    else:
        return text

def display_data_cols(data: any, search: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    opened = []
    closed = []
    max_len = MIN_COL_WIDTH
    for instance in data:
        # Go through all instances
        start_date = instance["start_date"]
        difference = time_difference(start_date)
        
        # Only consider if started < 2 hours ago
        if (difference < TWO_HOURS):
            name = instance["user_name"]
            max_len=max(max_len,len(name))
            # Add name to appropriate list
            if instance["open"]:
                opened.append(name)
            else:
                closed.append(name)
    # Sort alphabetically
    opened.sort()
    closed.sort()
    # Print in two columns
    print("Open".ljust(max_len+1," ") + "Closed\n")
    for i in range(max(len(opened),len(closed))):
        if i < len(opened):
            name = opened[i]
            name = name.ljust(max_len+1," ")
            # Change colour if contains search term
            name = highlight_search(name, search)
            print(name, end="")
        else:
            print(" "*(max_len+1), end = "")
        if i < len(closed):
            name = closed[i]
            name = highlight_search(name, search)
            print(name)
        else:
            print("")


def main():
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
            URL = "https://ca.prairielearn.org/pl/api/v1/course_instances/1678/assessments/"+str(config["assessment_id"]) +"/assessment_instances?private_token="+config["token"] 
    except EnvironmentError:
        print(CONFIG_FILE + " not found")
        return
    while True:
        search = input("Search: ")
        r = requests.get(URL)
        if r.status_code == 200:
            data = r.json()
            display_data_cols(data, search)
            print(datetime.datetime.now())
        elif r.status_code == 401:
            print("Invalid token")
        else:
            print("ERROR" + str(r.status_code))

if __name__ == '__main__':
    main()