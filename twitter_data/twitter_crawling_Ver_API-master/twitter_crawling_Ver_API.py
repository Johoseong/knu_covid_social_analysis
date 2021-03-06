import requests
import json
import time
import emoji
import ast
import re

class Crawling:
    bearer_token = ""
    search_url = ""
    query_params = {}

    def __init__(self):
        # To set your environment variables in your terminal run the following line:
        # export 'BEARER_TOKEN'='<your_bearer_token>'
        self.bearer_token = "AAAAAAAAAAAAAAAAAAAAAMjyOwEAAAAAYm8zDZ9NMtvCd4K%2FTckEVsozHCA%3Daj3fsQ8Pgmka7tfdzLkeTFcY8jtvZW0hhDps7UFVnsiU1aJhnv"
        self.search_url = "https://api.twitter.com/2/tweets/search/all"
        self.search_url_from_id = "https://api.twitter.com/2/users/"

        # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
        # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
        self.query_params = {'query': '', 'tweet.fields': 'created_at,lang,author_id',
                              'start_time': '2016-01-01T00:00:00Z', 'end_time': '2021-01-01T00:00:00Z', 'max_results': '500'}
        self.query_params_id = {'tweet.fields': 'created_at,lang,author_id,geo', 'start_time': '2016-01-01T00:00:00Z', 'end_time': '2021-01-01T00:00:00Z',
                                'max_results': '100'}

        # expansions=author_id&tweet.fields=created_at,author_id,conversation_id,public_metrics,context_annotations&user.fields=username&max_results=5

    def create_headers(self):
        headers = {"Authorization": "Bearer {}".format(self.bearer_token)}
        return headers

    def connect_to_endpoint(self, headers):
        response = requests.request("GET", self.search_url, headers=headers, params=self.query_params)
        # print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def main_act_indi(self, brand_list, drug_name, start_time, end_time):
        self.query_params['start_time'] = start_time
        self.query_params['end_time'] = end_time
        self.query_params['tweet.fields'] = "lang,created_at,author_id"
        self.query_params['expansions'] = "geo.place_id"
        self.query_params['place.fields'] = "country"
        # main activity
        fw = open(drug_name + " " + self.query_params['start_time'][0:10] + "~" + self.query_params['end_time'][
                                                                                  0:10] + ".json", "w", encoding="UTF8") # illegal multibyte sequence ?????? -> UTF8 ???????????? ??????
        for brand_name in brand_list:
            self.query_params['query'] = brand_name
            print(self.query_params)
            self.crawling_part(fw)

    ''' start crawling 
     parameter : ????????? ????????? ?????? json ?????? ?????? '''
    def crawling_part(self, fw):
        headers = self.create_headers()

        # crawling ??? json_response??? twit ????????? ?????? 
        json_response = self.connect_to_endpoint(headers)
        ## twit text ?????? ?????? '/" ?????? ??? json?????? ?????? ?????? -> ????????????
        for i in range(0, len(json_response['data'])):
            json_response['data'][i]['text'] = json_response['data'][i]['text'].replace("'", "").replace('"', "")

        # ????????????/?????????,????????? ?????? (???????????? ?????? ?????? ??? -> encoding ?????? ??????)
        json_response = str(json_response)
        json_response = emoji.get_emoji_regexp().sub(r'', json_response)
        json_response = re.sub(r'[^ 0-9???-??????-???A-Za-z.,"\':;_\-@(){}\[\]]', '', json_response)
        json_response = ast.literal_eval(json_response)

        # json ??????
        data = json.dumps(json_response, indent=4, sort_keys=True)
        data = data.encode('utf-8')
        # ?????? ?????? ?????? decode
        data = data.decode('unicode_escape', 'replace')

        fw.write(data)
        try:
            self.query_params['next_token'] = json_response['meta']['next_token']
        except Exception as e:
            print(self.query_params['query'] + " done")
            self.query_params['next_token'] = "DUMMY"
            del self.query_params['next_token']
            # print(e)
            time.sleep(3)
            return
        time.sleep(3)
        self.crawling_part(fw)
