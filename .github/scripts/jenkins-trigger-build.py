#!/usr/bin/python

import sys
import time
import requests
from urllib.parse import urlparse



print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))


######## UNCOMMENT TO HELPL DEBUG HTTP REQUESTS ########

# # These two lines enable debugging at httplib level (requests->urllib3->http.client)
# # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# # The only thing missing will be the response.body which is not logged.
# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1
#
#
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

############ TRIGGER JENKINS BUILD ############
user = "coates"
password = "test123"
trigger_url = "http://20.106.205.93:8080/job/fake-server-pipeline/build"
params = {'token': 'INSECURE_TOKEN'}
auth = (user, password)
trigger_job_response = requests.get(trigger_url, auth=auth, params=params, verify=False)

queue_number = 648
queue_url = trigger_job_response.headers['Location'] # looks like: 'Location': 'http://jenkins-host:8080/queue/item/646/'
if (queue_url is None):
    status_code = trigger_job_response.status_code
    print(f"Unexpected response from Jenkins when attempting to trigger build. Status code: {status_code}. Exiting...")
    sys.exit(2)
else:
    path_strs = urlparse(queue_url).path.strip('/').split('/') # path should look like /queue/item/<queue_number>
    queue_number_index = -1
    for i in range (len(path_strs)):
        if (path_strs[i] == "item"):
            queue_number_index = i+1 # the number is after the word "item"

    if queue_number_index == -1 or queue_number_index >= len(path_strs):
        print(f"Unexpected response from Jenkins. It should return a url with /item/<queue-number> in it, "
              f"but instead we got: {path_strs}. Exiting...")
        sys.exit(2)
    else:
        queue_number = path_strs[queue_number_index]
        print(f"queue number is: {path_strs[queue_number_index]}")

if queue_number == -1:
    print(f"For some reason, failed to get queue number when trying to trigger Jenkins build. Exiting...")
    sys.exit(2)


############ GET BUILD NUMBER FROM QUEUE NUMBER (WORKS) ############
def get_job_number(queue_number):
    url = f"http://20.106.205.93:8080/queue/item/{queue_number}/api/json?token=INSECURE_TOKEN&pretty=true"
    r = requests.get(url)
    if (r.status_code != 200):
        return -1
    else:
        json_resp = r.json()
        executable = json_resp.get("executable") # the job number is in the JSON field "executubale.number"
        if (executable):
            number = executable.get("number")
            if (number):
                return number
            else:
                return -1
        else:
            return -1

start_time = time.monotonic()
job_number = -1
while (time.monotonic() - start_time < 30):
    job_number = get_job_number(queue_number)
    if job_number != -1:
        break
    print("Build triggered, waiting to see if Jenkins queue api responds...")
    time.sleep(1)

print(f"Jenkins build successfully triggerd with job number {job_number}")
sys.stdout.write(str(job_number))
sys.stdout.flush()
sys.exit(0)