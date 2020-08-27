# Import modules
import json
import requests
from colorama import Fore
import tools.SMS.randomData as randomData


# Read services file
def getServices(file="tools/SMS/services.json"):
    with open(file, "r", encoding="utf-8", errors="ignore") as services:
        return json.load(services)["services"]


# Read proxy list
def getProxys(file="tools/SMS/proxy.json"):
    with open(file, "r") as proxys:
        return json.load(proxys)["proxy"]


# Get domain by big url
def getDomain(url):
    return url.split("/")[2]


# Make for other services
def transformPhone(phone, i):
    # Pizzahut
    if i == 5:
        return (
            "+"
            + phone[0]
            + " ("
            + phone[1:4]
            + ") "
            + phone[4:7]
            + " "
            + phone[7:9]
            + " "
            + phone[9:11]
        )  # '+7 (915) 350 99 08'


# Headers for request
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": randomData.random_useragent(),
}

# Service class
# parseData, SendSMS
class Service:
    def __init__(self, service):
        self.service = service
        self.proxy = getProxys()
        self.timeout = 10

    # Parse string
    def parseData(self, phone):
        payload = None
        # Check for 'data'
        if "data" in self.service:
            dataType = "data"
            payload = self.service["data"]
        # Check for 'json'
        elif "json" in self.service:
            dataType = "data"
            payload = self.service["json"]
        # Check for 'url'
        else:
            payload = json.dumps({"url": self.service["url"]})
            dataType = "url"
        # Replace %phone%, etc.. to data
        for old, new in {
            "'": '"',
            "%phone%": phone,
            "%phone5%": transformPhone(phone, 5),
            "%name%": randomData.random_name(),
            "%email%": randomData.random_email(),
            "%password%": randomData.random_password(),
            "%token%": randomData.random_token(),
        }.items():
            if old in payload:
                payload = payload.replace(old, new)
        return json.loads(payload), dataType

    # Send message
    def sendMessage(self, phone):
        url = self.service["url"]
        payload, dataType = self.parseData(phone)

        # Add custom headers
        if "headers" in self.service:
            customHeaders = self.service["headers"]
            for key, value in json.loads(customHeaders.replace("'", '"')).items():
                headers[key] = value

        # Create suffixes
#        lor+=1
        okay = f"{Fore.GREEN}>> +{Fore.RESET}"
        error = f"{Fore.RED}>> -{Fore.RESET}"

        session = requests.Session()
        request = requests.Request("POST", url)
        request.headers = headers

        if dataType == "json":
            request.json = payload
        elif dataType == "data":
            request.data = payload
        elif dataType == "url":
            request.url = payload["url"]

        try:
            request = request.prepare()
            r = session.send(request, timeout=self.timeout, proxies=self.proxy)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
#            print(f"{Fore.RED}{error}")
             er1=1+1
        except requests.exceptions.ConnectionError:
#            print(f"{Fore.RED}{error}")
             er2=1+1
        except Exception as err:
             er3=1+1
#            print(err)
        else:
            # Check status
            if r.status_code == 200:
#                derw+=1
                print(f"{Fore.GREEN}{'Сообщение отправленно.'}")
#            elif r.status_code == 429:
#                korm+=1
#                print(f"{Fore.RED}{error}")
#            else:
#                korm+=1
#                print(f"{Fore.RED}{error}")
