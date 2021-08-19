# twitter_crawling_Ver_API

## Module
```
pip install emoji

```

## API Usage
***
### main_act_indi(self, list, vaccine_name, start_time, end_time)
#### input_values
> list : (str) 동일한 키워드로 인식되는 키워드들 ex) "얀센", ...<br>
> drug_name : (str) 해당 list 내의 키워드 한개 ex) "얀센"<br>
> start_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2021-07-01T00:00:00Z"<br>
> end_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2021-07-02T00:00:00Z"<br>

#### ex) main_act_indi(drug_brand.brandname_lists[i], drug_brand.columns[i], "2021-07-01T00:00:00Z", "2021-07-02T00:00:00Z")
#### output file name : 얀센 2021-07-01~2021-07-02.json
#### output data : 
~~~
{
    "data": [
        {
            "author_id": "1265952319499165696",
            "created_at": "2021-07-01T23:56:33.000Z",
            "id": "1410749197561729029",
            "lang": "ko",
            "text": "델타변이가 급증하니까 얀센 1회 접종이 아니라 백신 교차접종을 위한 백신 수급이 더 중요해질듯."
        },
        {
            "author_id": "1359137486786580485",
            "created_at": "2021-07-01T23:47:06.000Z",
            "id": "1410746817818468356",
            "lang": "ko",
            "text": "RT @NCT9fx: 얀센 콘서타(치료제) 마케터 담당자가 한국에서 성인 ADHD로 치료받는 사람이 추산 대비 1프로인가 밖에 안된다고 인터뷰했쥬.. 당사자들도 증상들이 거의 개인의 노력 부족을 원인으로 치부하기 쉬워서 자책은 자책대로 하고 하소"
        },
        
. . .
~~~
***
