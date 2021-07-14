# twitter_crawling_Ver_API

## API Usage
***
### main_act_id(self, author_id_info, start_time, end_time)
#### input_values
author_id_info : (str) author's id ex) "1061602142"   
start_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2016-01-01T00:00:00Z"   
end_time : (str) YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) ex) "2017-01-01T00:00:00Z"   

#### ex) main_act_id("1061602142", "2016-01-01T00:00:00Z", "2016-01-08T00:00:00Z")
#### output file name : 1061602142 2016-01-01~2016-01-08.txt
#### output data : 
~~~
{
    "data": [
        {
            "author_id": "1061602142",
            "created_at": "2016-01-03T03:39:44.000Z",
            "id": "683492913888768000",
            "lang": "en",
            "text": "Sometimes we end up in places we don't expect for reasons that aren't clear.   Tonight was one of those."
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-01T16:04:23.000Z",
            "id": "682955538561372164",
            "lang": "en",
            "text": "Station 84 run after shift from hell....... I feel better now.  Just finished a 6.32mi run with #EaseInto5K https://t.co/I3JRbxn63V"
        }
    ],
    "meta": {
        "newest_id": "683492913888768000",
        "oldest_id": "682955538561372164",
        "result_count": 2
    }
}
~~~
***
### main_act_months(self, brand_list, drug_name, start_year, end_year)
#### input_values
brand_list : (list) Keywords ex) ['Baclofen', 'Baclospas', 'Balgifen']   
drug_name : (str) output naming ex) Baclofen   
start_time : (int) ex) 2016
end_time : (int) ex) 2017

#### ex) main_act_months(brandname_lists, columns, 2016, 2016)
#### output file name : Baclofen 2016-01-01&#126;2016-02-01.txt &#126; Baclofen 2016-12-01&#126;2017-01-01.txt
#### output data : 
~~~
{
    "data": [
        {
            "author_id": "2180907432",
            "created_at": "2016-01-31T20:51:35.000Z",
            "id": "693899449903480837",
            "lang": "de",
            "text": "Order  Baclofen 25 mg Online https://t.co/Nyv5Dfv3Nt #medical #blog #health"
        },
        {
            "author_id": "3313950829",
            "created_at": "2016-01-31T10:21:36.000Z",
            "id": "693740909217841152",
            "lang": "en",
            "text": "I took all 15 doses. They taste better than Tecfidera and way better than baclofen. Hopefully my extended dose will have BIG results."
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-31T04:06:31.000Z",
            "id": "693646514791567361",
            "lang": "en",
            "text": "Buy Low Price Baclofen 10 mg https://t.co/xJ9eOGf0Es #medical #blog #health"
        },
        {
            "author_id": "2435783624",
            "created_at": "2016-01-30T16:45:15.000Z",
            "id": "693475071550189568",
            "lang": "en",
            "text": "Are you considering using Baclofen to treat your alcoholism? Does it work? Get the facts:  https://t.co/ukazm8kv0T"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-30T08:06:21.000Z",
            "id": "693344484273307648",
            "lang": "en",
            "text": "Buy Baclofen online - Buy Cheap Baclofen Online No Prescription In Uk https://t.co/T2CEi5Fv5x #medical #blog #health"
        },
        {
            "author_id": "148361239",
            "created_at": "2016-01-29T19:36:12.000Z",
            "id": "693155701179486210",
            "lang": "en",
            "text": "@spooniespeak hi! I love heat and have multiple heat pads. Naproxen and celecoxib good, as is baclofen. Also like acupuncture #SpoonieSpeak"
        },
        {
            "author_id": "189271659",
            "created_at": "2016-01-29T16:25:11.000Z",
            "id": "693107632886976512",
            "lang": "nl",
            "text": "@gewoonBar dank je, baclofen dipt m'n zuurstof momenteel onder 94 dus zuurstof en extra controle vanacht bij t slapen"
        },
        {
            "author_id": "476533276",
            "created_at": "2016-01-29T10:53:44.000Z",
            "id": "693024220649955328",
            "lang": "en",
            "text": "Baclofen buy https://t.co/aFzPqssLTq https://t.co/pThS9eBLN9"
        },
        {
            "author_id": "503226685",
            "created_at": "2016-01-29T09:26:09.000Z",
            "id": "693002178487779328",
            "lang": "en",
            "text": "#Moutarjam: Baclofen buy https://t.co/5Y8hNSvTO1"
        },
        {
            "author_id": "23938222",
            "created_at": "2016-01-29T09:03:20.000Z",
            "id": "692996435818725376",
            "lang": "en",
            "text": "Baclofen buy https://t.co/NPYO6rw5kw https://t.co/T2MCWYG3bg"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-29T05:08:04.000Z",
            "id": "692937230525059072",
            "lang": "en",
            "text": "It's serious &lt;a href=\" https://t.co/2CmTUeb39h... https://t.co/uFEK2c6yvR"
        },
        {
            "author_id": "85883677",
            "created_at": "2016-01-28T10:57:40.000Z",
            "id": "692662824083021824",
            "lang": "en",
            "text": "My wife has a clinic appointmt at West Mids Rehab Centre today to refill her intrathecal baclofen pump.Another marvelous free NHS service"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-28T09:08:06.000Z",
            "id": "692635248677400580",
            "lang": "en",
            "text": "Cool site goodluck :) &lt;a href=\" https://t.co/sDW3SFfBH6... https://t.co/1E5Z5mtkvo"
        },
        {
            "author_id": "14237061",
            "created_at": "2016-01-27T22:00:15.000Z",
            "id": "692467179078467586",
            "lang": "en",
            "text": "No alcohol for a while for me. #baclofen #mswarrior"
        },
        {
            "author_id": "60572859",
            "created_at": "2016-01-27T19:24:37.000Z",
            "id": "692428013888262144",
            "lang": "en",
            "text": "Anticraving Effect of Baclofen in Alcohol-Dependent Patients\nhttps://t.co/0qZKIMtlpi\n\nhttps://t.co/PqYAtwDGaj"
        },
        {
            "author_id": "2447421230",
            "created_at": "2016-01-27T09:42:02.000Z",
            "id": "692281400297332736",
            "lang": "in",
            "text": "Injeksi intratekal baclofen dapat diberikan 3-6 bulan paska stroke pasien dengan spastisitas."
        },
        {
            "author_id": "2298577784",
            "created_at": "2016-01-27T07:00:01.000Z",
            "id": "692240627166232578",
            "lang": "ja",
            "text": "Multiple sclerosis\u306fCNS\u306b\u5bfe\u3059\u308b\u81ea\u5df1\u6297\u4f53\u306b\u3088\u308b\u8131\u9ac4\u75be\u60a3\u3002CSF\u306eIgG\u304c\u5897\u52a0\u3002\u6cbb\u7642\u306f\u03b2-interferon, \u514d\u75ab\u6291\u5236\u3001natalizumab\u3002\u75d9\u7e2e\u306b\u306fbaclofen\u3002"
        },
        {
            "author_id": "28780888",
            "created_at": "2016-01-27T04:03:01.000Z",
            "id": "692196085117407232",
            "lang": "en",
            "text": "@0211339090Tony thanks Tony. Good to hear from you. We did use Baclofen and it helped then we ran out!"
        },
        {
            "author_id": "3296518669",
            "created_at": "2016-01-27T03:18:05.000Z",
            "id": "692184777114415104",
            "lang": "en",
            "text": "fractures are not uncommon with severe spasm. If he is still getting occasional spasms try baclofen https://t.co/GEb9DwrmbK"
        },
        {
            "author_id": "230287288",
            "created_at": "2016-01-26T18:45:07.000Z",
            "id": "692055682065915904",
            "lang": "en",
            "text": "10 nights on #baclofen for my #narcolepsy Check it out on https://t.co/xkU7rbQvVy"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-26T16:08:05.000Z",
            "id": "692016164407357440",
            "lang": "en",
            "text": "How much does the job pay? &lt;a href=\" https://t.co/EoWW4oHANT... https://t.co/ZGdBTk4fNw"
        },
        {
            "author_id": "186899860",
            "created_at": "2016-01-26T08:42:05.000Z",
            "id": "691903923712626688",
            "lang": "de",
            "text": "Baclofen: Pille gegen Alkoholismus k\u00f6nnte bald zugelassen werden https://t.co/my36mfDqrX"
        },
        {
            "author_id": "191092262",
            "created_at": "2016-01-26T08:41:20.000Z",
            "id": "691903738420797443",
            "lang": "de",
            "text": "Baclofen: Pille gegen Alkoholismus k\u00f6nnte bald zugelassen werden https://t.co/d7KFcDrIpe"
        },
        {
            "author_id": "28759646",
            "created_at": "2016-01-26T04:50:41.000Z",
            "id": "691845690012647425",
            "lang": "en",
            "text": "@trevor_prather @FlintSnow I love me some Baclofen!!"
        },
        {
            "author_id": "408159990",
            "created_at": "2016-01-26T04:49:31.000Z",
            "id": "691845398449786880",
            "lang": "en",
            "text": "@hdtorch @FlintSnow Baclofen take me away! \ud83d\ude02"
        },
        {
            "author_id": "186899860",
            "created_at": "2016-01-26T04:12:53.000Z",
            "id": "691836179004678144",
            "lang": "de",
            "text": "Baclofen: Pille gegen Alkoholismus k\u00f6nnte bald zugelassen werden - Tabletten sollen in Zukunft bei der Entw\u00f6hnung\u2026 https://t.co/ijEdDLaZPq"
        },
        {
            "author_id": "1510260955",
            "created_at": "2016-01-26T03:38:41.000Z",
            "id": "691827572238368770",
            "lang": "en",
            "text": "Baclofen Topical Treatment https://t.co/4eN3aVPvJY"
        },
        {
            "author_id": "191092262",
            "created_at": "2016-01-26T00:10:11.000Z",
            "id": "691775103072362496",
            "lang": "de",
            "text": "Baclofen: Pille gegen Alkoholismus k\u00f6nnte bald zugelassen werden https://t.co/3sQObM9f8o"
        },
        {
            "author_id": "186899860",
            "created_at": "2016-01-26T00:10:10.000Z",
            "id": "691775096759947265",
            "lang": "de",
            "text": "Baclofen: Pille gegen Alkoholismus k\u00f6nnte bald zugelassen werden https://t.co/PhT52AXm1X"
        },
        {
            "author_id": "186899860",
            "created_at": "2016-01-25T19:21:06.000Z",
            "id": "691702350675742721",
            "lang": "de",
            "text": "DE | Baclofen: Pille gegen Alkoholismus k\u00f6nnte bald zugelassen werden \u00a0-\u00a0Tabletten sollen in Zukunft bei der\u2026 https://t.co/muXHl2Uqc6"
        },
        {
            "author_id": "1061602142",
            "created_at": "2016-01-25T16:10:38.000Z",
            "id": "691654419742658560",
            "lang": "en",
            "text": "What if addiction isn't a spiritual or moral calamity to be overcome....but a chronic illness we don't understand. #baclofen_study #RadioLab"
        },
        {
            "author_id": "217504935",
            "created_at": "2016-01-25T15:41:31.000Z",
            "id": "691647089906884608",
            "lang": "en",
            "text": "Baclofen (Baclofen Tablets) - updated on RxList:  https://t.co/WFSdzckmSO"
        },
        {
            "author_id": "2812903633",
            "created_at": "2016-01-25T14:18:18.000Z",
            "id": "691626149445677056",
            "lang": "ja",
            "text": "\u30a2\u30cb\u30e1\u95a2\u9023\uff1aVery Good Site &amp;lt;a href=&amp;quot; https://t.co/AZtqOBw9AR &amp;quot;&amp;g...https://t.co/ySOucpEh9L"
        },
        {
            "author_id": "186899860",
            "created_at": "2016-01-25T12:49:02.000Z",
            "id": "691603685256925184",
            "lang": "de",
            "text": "SNewsroom | DE -  Baclofen: Pille gegen Alkoholismus k\u00f6nnte bald zugelassen werden - Tabletten sollen in Zukunft\u2026 https://t.co/0w07he3hcK"
        },
        {
            "author_id": "2812903633",
            "created_at": "2016-01-25T12:13:07.000Z",
            "id": "691594644740710400",
            "lang": "ja",
            "text": "\u30a2\u30cb\u30e1\u95a2\u9023\uff1aI&amp;#039;m a housewife &amp;lt;a href=&amp;quot; https://t.co/YnCqI4cuQN ...https://t.co/ySOucpEh9L"
        },
        {
            "author_id": "2815137306",
            "created_at": "2016-01-25T10:19:26.000Z",
            "id": "691566035976220672",
            "lang": "de",
            "text": "Wie wirkt #Baclofen gegen #Alkoholsucht? Ein Miniprojekt von @jannosen und mir.  https://t.co/ChQeA9aoVe"
        },
        {
            "author_id": "3008951023",
            "created_at": "2016-01-25T10:16:39.000Z",
            "id": "691565335774756864",
            "lang": "en",
            "text": "@BrensonRain I have been on it since August. It sucks! He had me on Tizanidine, Baclofen and then this. The other 2 had nasty effects!"
        },
        {
            "author_id": "624961399",
            "created_at": "2016-01-25T10:09:34.000Z",
            "id": "691563553904549888",
            "lang": "de",
            "text": "RT @WELT_Wissen: So wirkt #Baclofen, die Pille gegen #Alkoholsucht. https://t.co/shs4FWL9OL https://t.co/tO1KtskIz3"
        },
        {
            "author_id": "52711521",
            "created_at": "2016-01-25T09:39:32.000Z",
            "id": "691555996347555840",
            "lang": "de",
            "text": "So wirkt #Baclofen, die Pille gegen #Alkoholsucht. https://t.co/shs4FWL9OL https://t.co/tO1KtskIz3"
        },
        {
            "author_id": "1227877484",
            "created_at": "2016-01-25T09:34:49.000Z",
            "id": "691554807480479744",
            "lang": "de",
            "text": "RT @N24: Baclofen - \nEine Pille gegen Alkoholsucht - funktioniert das wirklich? https://t.co/io1L6CTJha"
        },
        {
            "author_id": "2647287926",
            "created_at": "2016-01-25T09:28:20.000Z",
            "id": "691553176810569729",
            "lang": "de",
            "text": "RT @N24: Baclofen - \nEine Pille gegen Alkoholsucht - funktioniert das wirklich? https://t.co/io1L6CTJha"
        },
        {
            "author_id": "3437653049",
            "created_at": "2016-01-25T09:11:35.000Z",
            "id": "691548963661615104",
            "lang": "de",
            "text": "Baclofen - \nEine Pille gegen Alkoholsucht - funktioniert das wirklich? : https://t.co/hCAZO84j45"
        },
        {
            "author_id": "15738602",
            "created_at": "2016-01-25T08:57:17.000Z",
            "id": "691545363921125376",
            "lang": "de",
            "text": "Baclofen - \nEine Pille gegen Alkoholsucht - funktioniert das wirklich? https://t.co/io1L6CTJha"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-25T03:08:04.000Z",
            "id": "691457480774148096",
            "lang": "en",
            "text": "I can't hear you very well &lt;a href=\" https://t.co/S2hwP2fU5H... https://t.co/ttqubbvr63"
        },
        {
            "author_id": "2812903633",
            "created_at": "2016-01-25T02:26:18.000Z",
            "id": "691446967910604800",
            "lang": "ja",
            "text": "\u30a2\u30cb\u30e1\u95a2\u9023\uff1aAbout a year &amp;lt;a href=&amp;quot; https://t.co/N6gW5t6CVP &amp;quot...https://t.co/ySOucpEh9L"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-24T18:08:08.000Z",
            "id": "691321601279684608",
            "lang": "en",
            "text": "Not in at the moment &lt;a href=\" https://t.co/WqdJBEfTXe... https://t.co/cVi6q4CyQp"
        },
        {
            "author_id": "2180234989",
            "created_at": "2016-01-24T17:49:01.000Z",
            "id": "691316790190817280",
            "lang": "en",
            "text": "How do stop with baclofen after using it for withd\u2026 https://t.co/YfrwXxnYci"
        },
        {
            "author_id": "4025056282",
            "created_at": "2016-01-24T17:38:54.000Z",
            "id": "691314242956464128",
            "lang": "en",
            "text": "How do stop with baclofen after using it for withdrawal? https://t.co/ITK7AnNDcG"
        },
        {
            "author_id": "2344962830",
            "created_at": "2016-01-24T17:37:29.000Z",
            "id": "691313886579048449",
            "lang": "en",
            "text": "How do stop with baclofen after using it for withdrawal? via /r/Nootropics https://t.co/auqI5zyGnW"
        },
        {
            "author_id": "3299571025",
            "created_at": "2016-01-24T10:01:03.000Z",
            "id": "691199024687247360",
            "lang": "en",
            "text": "https://t.co/XJpLSTLvgp #iAsk #SPINAX #TABLETS #10.0MG #\"WEIDAR\" #(BACLOFEN) SPINAX TABLETS 10.0MG \"WEIDAR\" (BAC..."
        },
        {
            "author_id": "45743699",
            "created_at": "2016-01-24T07:24:44.000Z",
            "id": "691159685966237696",
            "lang": "en",
            "text": "I liked a @YouTube video from @jhasselberger https://t.co/XzeOTavTzP Baclofen Pump Refill Day"
        },
        {
            "author_id": "150360638",
            "created_at": "2016-01-24T04:44:37.000Z",
            "id": "691119389605785600",
            "lang": "en",
            "text": "I liked a @YouTube video from @jhasselberger https://t.co/AAKqYDGUEI Baclofen Pump Refill Day"
        },
        {
            "author_id": "57112574",
            "created_at": "2016-01-24T02:57:44.000Z",
            "id": "691092492683448320",
            "lang": "en",
            "text": "Baclofen Pump Refill Day https://t.co/N9pkwAlE24"
        },
        {
            "author_id": "57112574",
            "created_at": "2016-01-24T02:13:39.000Z",
            "id": "691081395553308672",
            "lang": "en",
            "text": "I liked a @YouTube video from @jhasselberger https://t.co/w09IfWOAHr Baclofen Pump Refill Day"
        },
        {
            "author_id": "57112574",
            "created_at": "2016-01-24T02:12:12.000Z",
            "id": "691081030619496448",
            "lang": "en",
            "text": "Baclofen Pump Refill Day https://t.co/OitGGUSryi"
        },
        {
            "author_id": "176171870",
            "created_at": "2016-01-23T16:12:45.000Z",
            "id": "690930176646123520",
            "lang": "en",
            "text": "@Novartis hi I'd like to know if your company in Ecuador sells Baclofen 10mg. My daughter needs it and I can't find it. Help please"
        },
        {
            "author_id": "20778698",
            "created_at": "2016-01-23T15:52:48.000Z",
            "id": "690925155527331840",
            "lang": "en",
            "text": "@JamieLSigler What meds are you on? I take Gabbapentin and Baclofen. Thank you."
        },
        {
            "author_id": "20778698",
            "created_at": "2016-01-23T15:49:23.000Z",
            "id": "690924293610442753",
            "lang": "en",
            "text": "@JamieLSigler What meds are you on? I'm taking Gabbapentin and Baclofen."
        },
        {
            "author_id": "1674188378",
            "created_at": "2016-01-23T14:00:20.000Z",
            "id": "690896851315343360",
            "lang": "en",
            "text": "Which medication will require monitoring for EPS?\nA. Metoclopramide\nB. Erythromycin\nC. Clarithromycin\nD. Baclofen"
        },
        {
            "author_id": "2304897223",
            "created_at": "2016-01-23T10:06:53.000Z",
            "id": "690838104156991488",
            "lang": "de",
            "text": "#Beruf Baclofen: So soll die Pille gegen die Alkoholsucht wirken: Tabletten sollen in Zukunft bei de... https://t.co/otkhYVQjvh #Karriere"
        },
        {
            "author_id": "976272432",
            "created_at": "2016-01-23T09:53:12.000Z",
            "id": "690834659568148480",
            "lang": "en",
            "text": "Baclofen not doing its job lately.... #MSsucksweek"
        },
        {
            "author_id": "176171870",
            "created_at": "2016-01-23T03:43:09.000Z",
            "id": "690741531951644672",
            "lang": "en",
            "text": "Would u RT please? I urgently need to get baclofen 10mg 4 my daughter. If any of u have info. Let me know please. Thanks"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-22T21:03:49.000Z",
            "id": "690641036658499584",
            "lang": "en",
            "text": "Order Baclofen 10 mg Low Price - How to Purchase Lioresal Fast Delivery https://t.co/UvF0qMiugn #medical #blog #health"
        },
        {
            "author_id": "3148891795",
            "created_at": "2016-01-22T15:34:48.000Z",
            "id": "690558237809094656",
            "lang": "en",
            "text": "Baclofen prevents the elevated plus maze behaviour and bdnf expression during naloxone precipitated morphine w... https://t.co/1eTd4lVMRC"
        },
        {
            "author_id": "258334052",
            "created_at": "2016-01-22T09:52:14.000Z",
            "id": "690472026440605696",
            "lang": "en",
            "text": "ordering online Baclofen without rx in UK | cheap price Baclofen: discount Baclofen in Denver , Colo. [/b]; how to\u2026"
        },
        {
            "author_id": "308910538",
            "created_at": "2016-01-22T06:17:43.000Z",
            "id": "690418044837957632",
            "lang": "es",
            "text": "Carbamazepina es la mejor terapia inicial para una \"Neuralgia del Trig\u00e9mino\". Fenito\u00edna, Baclofen y Gabapentina pueden ser efectivos."
        },
        {
            "author_id": "2585016915",
            "created_at": "2016-01-22T03:11:25.000Z",
            "id": "690371160719167488",
            "lang": "en",
            "text": "@PondMichael @stevenbuechler @cbcdocs @DianesDigitals   been using new research coming out of France using BACLOFEN for the same purpose."
        },
        {
            "author_id": "2585016915",
            "created_at": "2016-01-22T02:57:35.000Z",
            "id": "690367677878116354",
            "lang": "en",
            "text": "Lately we have been using new research coming out of France using BACLOFEN for the same purpose."
        },
        {
            "author_id": "184683785",
            "created_at": "2016-01-21T22:20:01.000Z",
            "id": "690297823980433408",
            "lang": "en",
            "text": "damn this baclofen got me feelin wooooozy"
        },
        {
            "author_id": "369916085",
            "created_at": "2016-01-21T21:14:35.000Z",
            "id": "690281358443155456",
            "lang": "en",
            "text": "@VioletOctober Okay, other than that the only other thing i have to bring is baclofen and skelaxin... and those are just muscle relaxers. :P"
        },
        {
            "author_id": "4151058453",
            "created_at": "2016-01-21T19:02:55.000Z",
            "id": "690248222326046721",
            "lang": "es",
            "text": "@LaHojillaenTV camarada ayudame a conseguir el medicamento Lioresal de 10mg en tableta.(Baclofen) soy docente y estoy en silla.04167411458"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T18:18:55.000Z",
            "id": "690237151418540032",
            "lang": "en",
            "text": "Symptoms of baclofen withdrawal? fever, increased muscle tone, seizure. Can mimic NMS. history is key #toxthurs"
        },
        {
            "author_id": "3988692013",
            "created_at": "2016-01-21T18:14:11.000Z",
            "id": "690235961897148416",
            "lang": "en",
            "text": "I\u2019m on Baclofen. What should I watch out for? @UMassTox"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T18:13:58.000Z",
            "id": "690235906830254080",
            "lang": "en",
            "text": "UMassTox: How much is bad? &gt;200mg of baclofen is likely to cause delirium, coma. https://t.co/X0yb27Rrmn #toxthurs"
        },
        {
            "author_id": "4208246833",
            "created_at": "2016-01-21T18:13:16.000Z",
            "id": "690235728626712576",
            "lang": "en",
            "text": "baclofen oral : Uses, Side Effects, Interactions, Pictures, Warnings &amp; Dosing - WebMD https://t.co/pGuIte5vWC from WebMD"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T18:11:03.000Z",
            "id": "690235170612469760",
            "lang": "en",
            "text": "RT @kavitababu: How does baclofen cause seizures in overdose? @UMassTox"
        },
        {
            "author_id": "29513018",
            "created_at": "2016-01-21T18:10:51.000Z",
            "id": "690235121526534145",
            "lang": "en",
            "text": "How does baclofen cause seizures in overdose? @UMassTox"
        },
        {
            "author_id": "4680471900",
            "created_at": "2016-01-21T18:08:27.000Z",
            "id": "690234518813343744",
            "lang": "en",
            "text": "Ohhh. Baclofen lesson on @UMassTox Yay. I\u2019m on that."
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T18:06:24.000Z",
            "id": "690234002326818816",
            "lang": "en",
            "text": "How does baclofen work? GABA-B agonism, lipophilic, targets UMN in spinal cord, brainstem #toxthurs"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T18:03:56.000Z",
            "id": "690233381368532994",
            "lang": "en",
            "text": "Baclofen withdrawal from pump error: empty pump (missed refill), catheter migration #toxthurs"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T18:02:18.000Z",
            "id": "690232968170831872",
            "lang": "en",
            "text": "Baclofen commonly seen in intrathecal pumps. How do you get toxic from pumps? #toxthurs"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T17:59:49.000Z",
            "id": "690232344251371520",
            "lang": "en",
            "text": "Baclofen: skeletal muscle relaxant. GABA-B agonist. used in cerebral palsy, MS to treat spasticity #toxthurs"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T17:58:47.000Z",
            "id": "690232085374746624",
            "lang": "en",
            "text": "Dr. Hart. talking baclofen toxicity. #toxthurs"
        },
        {
            "author_id": "348168716",
            "created_at": "2016-01-21T17:24:03.000Z",
            "id": "690223345225306112",
            "lang": "en",
            "text": "Sedation, bradycardia- clonidine, GHB, baclofen #toxthurs"
        },
        {
            "author_id": "403589120",
            "created_at": "2016-01-21T14:10:04.000Z",
            "id": "690174526819139584",
            "lang": "en",
            "text": "@amyallantdf @artsyfart66 @chipcoffey I take baclofen , a muscle relaxer, non habit forming, had to get a script but well worth it.  peace"
        },
        {
            "author_id": "1477289432",
            "created_at": "2016-01-21T12:00:54.000Z",
            "id": "690142018870329344",
            "lang": "nl",
            "text": "Hikken: baclofen (3dd5 mg elke 3 dg ophogen), combineren met procineticum en ev PPI ; MM4 15"
        },
        {
            "author_id": "2435783624",
            "created_at": "2016-01-21T11:50:14.000Z",
            "id": "690139335144927232",
            "lang": "en",
            "text": "Are you considering using Baclofen to treat your alcoholism? Does it work? Get the facts:  https://t.co/ukazm8kv0T"
        },
        {
            "author_id": "385197941",
            "created_at": "2016-01-20T23:27:04.000Z",
            "id": "689952312668876803",
            "lang": "en",
            "text": "Baclofen is OK"
        },
        {
            "author_id": "3366330970",
            "created_at": "2016-01-20T22:54:25.000Z",
            "id": "689944097000439808",
            "lang": "en",
            "text": "Baclofen: highly underrated https://t.co/OrZ8V2Srsi"
        },
        {
            "author_id": "21977758",
            "created_at": "2016-01-20T20:59:21.000Z",
            "id": "689915138019827713",
            "lang": "en",
            "text": "Uptight and emo like our boy Kylo Ren\nRelax those muscles with some Baclofen\n\n(what do you mean I never use my MScPT?)"
        },
        {
            "author_id": "319269434",
            "created_at": "2016-01-20T20:15:58.000Z",
            "id": "689904218254229505",
            "lang": "en",
            "text": "@dpnewkirk1 We are a pair then. I'm alive taling tramadol,baclofen,and norco. I have fibromialgia and rhuematoid athritus. Wite more doc."
        },
        {
            "author_id": "17300548",
            "created_at": "2016-01-20T18:57:43.000Z",
            "id": "689884527401893888",
            "lang": "en",
            "text": "Sopranos actress Jamie-Lynn Sigler reveals she has been living with multiple sclerosis: https://t.co/jopetqY1Up -- Dr. put me on: Baclofen"
        },
        {
            "author_id": "4246354816",
            "created_at": "2016-01-20T16:20:56.000Z",
            "id": "689845072477712384",
            "lang": "en",
            "text": "@mstrooper08 Sharing what's working 4 me We're all different but all probably have similar deficiencies in diet Magnesium replaces Baclofen"
        },
        {
            "author_id": "759957720",
            "created_at": "2016-01-20T09:12:03.000Z",
            "id": "689737141446832128",
            "lang": "en",
            "text": "Effect of Intrathecal Baclofen on Delayed-Onset Paroxysmal Dystonia due to Compression Injury Resul... https://t.co/KLKLG0C1UE #Neurology"
        },
        {
            "author_id": "4209816358",
            "created_at": "2016-01-20T06:10:28.000Z",
            "id": "689691442801876992",
            "lang": "en",
            "text": "Where to Buy Baclofen (Lioresal) 10, 25\u00a0mg https://t.co/wN8eHtNvhe"
        },
        {
            "author_id": "3366330970",
            "created_at": "2016-01-20T00:36:24.000Z",
            "id": "689607373095309312",
            "lang": "en",
            "text": "Equivalent doses for baclofen and phenibut? https://t.co/23d5nFC8Vj"
        },
        {
            "author_id": "2789910212",
            "created_at": "2016-01-19T21:46:05.000Z",
            "id": "689564508616978432",
            "lang": "en",
            "text": "Effect of Intrathecal Baclofen on Delayed-Onset Paroxysmal Dystonia due to Compression Injury Resulting From\u2026 https://t.co/m7hJLDQTue"
        },
        {
            "author_id": "198027806",
            "created_at": "2016-01-19T19:40:43.000Z",
            "id": "689532961121767425",
            "lang": "en",
            "text": "Some #AlcoholUseDisorder meds are on-label, others off-label:\n\u2022Naltrexone\n\u2022Acamprosate\n\u2022Disulfiram (compounded)\n\u2022Topiramate\n\u2022Baclofen"
        },
        {
            "author_id": "1106321251",
            "created_at": "2016-01-19T18:35:41.000Z",
            "id": "689516596847624192",
            "lang": "en",
            "text": "@michaelcombra @FlGl14 Flexiril never did anything except make me feel lousy. Ask about Baclofen, trick is finding therapeutic dose"
        },
        {
            "author_id": "16644642",
            "created_at": "2016-01-19T15:19:55.000Z",
            "id": "689467328606535680",
            "lang": "en",
            "text": "Needing to remind myself to breathe sucks. Asleep or awake, I have to stop all the time and remember to breathe! #SideEffects &lt;/3 Baclofen!"
        },
        {
            "author_id": "214012838",
            "created_at": "2016-01-19T03:54:48.000Z",
            "id": "689294912148402177",
            "lang": "es",
            "text": "lasortan\namlodipine\nbotolinium\nbaclofen\ntrombocil"
        },
        {
            "author_id": "16644642",
            "created_at": "2016-01-19T01:54:40.000Z",
            "id": "689264682436292608",
            "lang": "en",
            "text": "Home from #dialysis, feeling woozy. I need to learn if Baclofen dialyzes out or not. At least I can walk today. Yesterday I couldn't."
        },
        {
            "author_id": "477107039",
            "created_at": "2016-01-19T00:24:00.000Z",
            "id": "689241864617103360",
            "lang": "en",
            "text": "@MustStopMS. Not at all, tried baclofen &amp; zanaflex, but couldn't get dosages right. We then tried valium &amp; it works wonderfully 4 me #ChatMS"
        },
        {
            "author_id": "66107790",
            "created_at": "2016-01-18T19:34:35.000Z",
            "id": "689169030599561216",
            "lang": "en",
            "text": "RT @baclofenews: Latests studies on #baclofen for #alcoholism and other addictions. Timeline constantly updated https://t.co/EWxbizN2yE #ba\u2026"
        },
        {
            "author_id": "3740927421",
            "created_at": "2016-01-18T14:17:21.000Z",
            "id": "689089195873316866",
            "lang": "de",
            "text": "Forum Post: imybp188 - order baclofen https://t.co/vpNfy9x6qz"
        },
        {
            "author_id": "3299571025",
            "created_at": "2016-01-18T11:33:07.000Z",
            "id": "689047865428062209",
            "lang": "zh",
            "text": "https://t.co/uovo5xJLPS #iAsk #\u6210\u4efd #\u85e5\u54c1 #\u5291\u91cf #\u526f\u4f5c\u7528 #\u91ab\u7642 BAFEN 10MG TABLETS (BACLOFEN)\u88e1\u9762\u6709\u4ec0\u9ebc\u6210\u4efd\uff1f"
        },
        {
            "author_id": "3740927421",
            "created_at": "2016-01-18T02:17:16.000Z",
            "id": "688907980843143168",
            "lang": "da",
            "text": "Forum Post: h0h8xmyk - baclofen https://t.co/wgJlc0HMYJ"
        },
        {
            "author_id": "6199172",
            "created_at": "2016-01-17T14:16:55.000Z",
            "id": "688726696762195968",
            "lang": "nl",
            "text": "@peetje33 k zit ondertussen op mengsel van paracetamol en baclofen... Net iets straffer @Las_Ania"
        },
        {
            "author_id": "2463117790",
            "created_at": "2016-01-17T13:01:18.000Z",
            "id": "688707667095846914",
            "lang": "en",
            "text": "Can baclofen be used in #pregnancy? Find the answer at https://t.co/5THxrQjw4I"
        },
        {
            "author_id": "191193002",
            "created_at": "2016-01-17T12:55:09.000Z",
            "id": "688706121402609664",
            "lang": "nl",
            "text": "@User2244 @valk1955 En dan te bedenken dat moeder het met anderhalf pilletje baclofen af kan. Ze hebben eens een keer de dosis verhoogd.."
        },
        {
            "author_id": "93655018",
            "created_at": "2016-01-17T07:04:12.000Z",
            "id": "688617803834769408",
            "lang": "en",
            "text": "@FreddyInSpace I drank a bunch and took my baclofen. Now I'm just blaring early-2000s emo-punk and pretending I'm 20 again."
        },
        {
            "author_id": "2556994153",
            "created_at": "2016-01-17T02:14:10.000Z",
            "id": "688544811738075136",
            "lang": "en",
            "text": "RT @NCSBNLearnExt: #PharmFri: Skeletal Muscle Relaxants: Intrathecal baclofen therapy helps control symptoms of spasticity caused by MS."
        },
        {
            "author_id": "127487450",
            "created_at": "2016-01-16T13:33:31.000Z",
            "id": "688353388136935424",
            "lang": "de",
            "text": "Neue Adresse: https://t.co/uRfbLT2AWB"
        },
        {
            "author_id": "2907005745",
            "created_at": "2016-01-16T11:17:56.000Z",
            "id": "688319265955561472",
            "lang": "es",
            "text": "#Pharmaceutical baclofen : Lioresal Intrathecal : https://t.co/eSCC4VuxIi #MRX #Surveys #MarketResearchReports #Forecasts #Marketing"
        },
        {
            "author_id": "1476744038",
            "created_at": "2016-01-16T10:45:31.000Z",
            "id": "688311111679082496",
            "lang": "und",
            "text": "https://t.co/CRY9hIz9qd"
        },
        {
            "author_id": "1679781306",
            "created_at": "2016-01-16T06:10:31.000Z",
            "id": "688241902672453632",
            "lang": "no",
            "text": "@ambersibla @afentra @Slivmeister flexeril, soma, skelakin, baclofen?"
        },
        {
            "author_id": "3299571025",
            "created_at": "2016-01-16T05:46:42.000Z",
            "id": "688235911562137602",
            "lang": "zh",
            "text": "https://t.co/62p0N0xlLl #iAsk #\u85e5\u54c1 #\u9023\u7e8c\u8655\u65b9\u7b8b #\u91ab\u7642 #\u5065\u4fdd #\u85e5\u5c40 BEFON TABLETS 10MG \"M.S.\" (BACLOFEN)\u6c92\u6709\u9023\u7e8c\u8655\u65b9\u7b8b\u53ef\u4ee5\u76f4\u63a5..."
        },
        {
            "author_id": "3299571025",
            "created_at": "2016-01-16T04:58:00.000Z",
            "id": "688223653486411776",
            "lang": "ja",
            "text": "https://t.co/6rRPlH4XJe #iAsk #\"BACONE #TABLETS #10MG #\"\"H.S.\"\" #(BACLOFEN)(\u92c1\u7b94/\u81a0\u7b94)\" \"BACONE TABLETS 10MG \"\"H.S.\"..."
        },
        {
            "author_id": "34966436",
            "created_at": "2016-01-16T04:30:24.000Z",
            "id": "688216709933608961",
            "lang": "en",
            "text": "Hearing that baclofen might be a true cure for alcoholism. I wish it had by there for my cousin..."
        },
        {
            "author_id": "161807962",
            "created_at": "2016-01-15T23:54:15.000Z",
            "id": "688147213378138117",
            "lang": "en",
            "text": "Who need some baclofen"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-15T22:39:21.000Z",
            "id": "688128363144187904",
            "lang": "en",
            "text": "Baclofen 25mg buy - Where Can I Buy Lioresal  Online https://t.co/P6IMJb9ITd #medical #blog #health"
        },
        {
            "author_id": "2258812233",
            "created_at": "2016-01-15T22:04:51.000Z",
            "id": "688119683342405632",
            "lang": "en",
            "text": "RT @NCSBNLearnExt: #PharmFri: Skeletal Muscle Relaxants: Intrathecal baclofen therapy helps control symptoms of spasticity caused by MS."
        },
        {
            "author_id": "3366330970",
            "created_at": "2016-01-15T17:41:22.000Z",
            "id": "688053375083147266",
            "lang": "fi",
            "text": "Best combination : Lyrica + Mdma or Baclofen + MDMA or Baclofen + Lyrica + MDMA https://t.co/RFW3NIDZcc"
        },
        {
            "author_id": "86339112",
            "created_at": "2016-01-15T17:04:35.000Z",
            "id": "688044117427896322",
            "lang": "en",
            "text": "#PharmFri: Skeletal Muscle Relaxants: Intrathecal baclofen therapy helps control symptoms of spasticity caused by MS."
        },
        {
            "author_id": "100727289",
            "created_at": "2016-01-15T07:43:42.000Z",
            "id": "687902967614312448",
            "lang": "nl",
            "text": "@Sophiedelietje ik ben de Baclofen aan het afbouwen tot De Grote BotoxDag en guess what... Ik slaap veel beter \\o/."
        },
        {
            "author_id": "3131199549",
            "created_at": "2016-01-15T02:53:48.000Z",
            "id": "687830010057605120",
            "lang": "en",
            "text": "I'm considering ODing on baclofen when I get home from working nightshift"
        },
        {
            "author_id": "213756902",
            "created_at": "2016-01-14T20:29:04.000Z",
            "id": "687733189645844484",
            "lang": "en",
            "text": "Ugghhh morphine and Baclofen just don't seem to be helping this pain from my neck injections. I just hope it goes away soon.."
        },
        {
            "author_id": "1137505464",
            "created_at": "2016-01-14T19:14:23.000Z",
            "id": "687714394810142720",
            "lang": "en",
            "text": "Pt1: On chronic #opioid tx, also takes #benzodiazepines &amp; Baclofen for #anxiety &amp; #muscle spasms. Has CKD stage 3, DM 2 #projectecho"
        },
        {
            "author_id": "20263645",
            "created_at": "2016-01-14T11:34:06.000Z",
            "id": "687598561345859584",
            "lang": "nl",
            "text": "Baclofen, codeine en veel wiet. Afkicken van Lyrica is behalve de hel ook een prima alibi voor misbruik van medicatie. #HowToChillInHell"
        },
        {
            "author_id": "2983200407",
            "created_at": "2016-01-13T13:38:06.000Z",
            "id": "687267379785629697",
            "lang": "cy",
            "text": "#Pharmaceuticals baclofen : Baclofen : https://t.co/xMcnUC01SO #MRX #Surveys #Statistics #MarketResearchReports #Forecast #Marketing"
        },
        {
            "author_id": "3315536376",
            "created_at": "2016-01-13T13:10:39.000Z",
            "id": "687260469225062401",
            "lang": "en",
            "text": "\ud83d\udc8a GPAT - P'cology \ud83d\udc8a\n\nWhich of the following is GABA B antagonist: \n\nA) bicuculin\nB) saclofen\nC) muscimol\nD) baclofen"
        },
        {
            "author_id": "1163813676",
            "created_at": "2016-01-13T10:45:13.000Z",
            "id": "687223871733403648",
            "lang": "en",
            "text": "Effect of (low-dose) #baclofen on alcohol cue-induced #craving. #fMRI study by Benegal et al. #alcoholism #relapse https://t.co/mHcmL6WGqA"
        },
        {
            "author_id": "3813301874",
            "created_at": "2016-01-13T08:42:28.000Z",
            "id": "687192978138370048",
            "lang": "cy",
            "text": "Baclofen https://t.co/keUUGWNWCP via @sharethis"
        },
        {
            "author_id": "394215646",
            "created_at": "2016-01-12T22:46:36.000Z",
            "id": "687043023776165889",
            "lang": "en",
            "text": "RT @wikisext: sext: i carelessly strengthen my wrists while you carelessly take 40-80 mg of baclofen (lioresal) every day"
        },
        {
            "author_id": "453070195",
            "created_at": "2016-01-12T12:39:48.000Z",
            "id": "686890317061160960",
            "lang": "sv",
            "text": "Intressant p\u00e5 Kunskapskanalen om Baclofen mot alkoholberoende. Enl min erf (begr\u00e4nsad) hj\u00e4lper det inte alla. https://t.co/8c6QTCyl28"
        },
        {
            "author_id": "1476744038",
            "created_at": "2016-01-11T17:33:06.000Z",
            "id": "686601744294481920",
            "lang": "und",
            "text": "https://t.co/cWDITTjoHq https://t.co/EhABxt0UOR"
        },
        {
            "author_id": "2254421724",
            "created_at": "2016-01-11T16:15:09.000Z",
            "id": "686582127173894144",
            "lang": "und",
            "text": "V 22 65 (Baclofen 10 mg) https://t.co/EHTRYGT1DU"
        },
        {
            "author_id": "3299571025",
            "created_at": "2016-01-11T14:48:19.000Z",
            "id": "686560275084886016",
            "lang": "zh",
            "text": "https://t.co/HNYXKSy8S8 #iAsk #\u526f\u4f5c\u7528 #\u85e5\u54c1 #\u5291\u91cf #\u6210\u4efd #\u91ab\u7642 \u4f7f\u7528SPINAX TABLETS 10.0MG \"WEIDAR\" (BACLOFEN) (\u92c1\u7b94/\u81a0\u7b94)\u6703\u6709..."
        },
        {
            "author_id": "4680471900",
            "created_at": "2016-01-11T14:38:57.000Z",
            "id": "686557917294641154",
            "lang": "en",
            "text": "If I go without Baclofen I\u2019ll be in agony. I\u2019ve already chosen antibiotics over antivirals. I spoiled boy too much on weekend. My fault."
        },
        {
            "author_id": "75793726",
            "created_at": "2016-01-11T09:23:05.000Z",
            "id": "686478427273228288",
            "lang": "en",
            "text": "@GYeulett might be a long night lol 20mg baclofen, 20mg lortabs, 2mg klonopin and 10mg ambien... Still standing."
        },
        {
            "author_id": "3129454192",
            "created_at": "2016-01-11T01:58:56.000Z",
            "id": "686366651902771200",
            "lang": "en",
            "text": "@EveryFinnishNo  baclofen chimneypots interanimations insolently wiggliest \u2191 https://t.co/NRI1MQu5o7"
        },
        {
            "author_id": "518316093",
            "created_at": "2016-01-10T15:58:32.000Z",
            "id": "686215556400193536",
            "lang": "en",
            "text": "@mysteriousfact Rather meet ur physician and get prescribed tab baclofen."
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-10T15:07:40.000Z",
            "id": "686202755954917376",
            "lang": "en",
            "text": "Purchase  Baclofen 10 mg https://t.co/etsQTFunnU #medical #blog #health"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-10T14:36:32.000Z",
            "id": "686194921766793216",
            "lang": "en",
            "text": "Buy Baclofen 25mg online - Where to Buy Lioresal Free Delivery https://t.co/ar52gUEw5m #medical #blog #health"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-10T11:00:26.000Z",
            "id": "686140536118480897",
            "lang": "de",
            "text": "Therapie \u2022 Sucht kommt von Sieche und das bedeutet Krankheit https://t.co/6Wg9R2my9c"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-10T09:57:43.000Z",
            "id": "686124754554765312",
            "lang": "de",
            "text": "Therapie \u2022 Re: Alkoholkonsum mit KISS reduzieren https://t.co/4lzwhEuivs"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-10T09:57:43.000Z",
            "id": "686124753950797824",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/6UQ6VpkEx1"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-10T06:56:08.000Z",
            "id": "686079055783923712",
            "lang": "de",
            "text": "Therapie \u2022 Re: Alkoholkonsum mit KISS reduzieren https://t.co/oLss8K2Mn4"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T21:25:58.000Z",
            "id": "685935567981383684",
            "lang": "de",
            "text": "Therapie \u2022 Re: Alkoholkonsum mit KISS reduzieren https://t.co/rbCu8eiP2g"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T21:25:56.000Z",
            "id": "685935559651516416",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/Frh8skybhZ"
        },
        {
            "author_id": "1471909016",
            "created_at": "2016-01-09T20:58:01.000Z",
            "id": "685928537367408640",
            "lang": "en",
            "text": "Member ask\nI care for someone on baclofen and lyrica among a lot of other medication for CRPS.  If he takes it... https://t.co/mIeKQYDxtB"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T18:15:55.000Z",
            "id": "685887742375497729",
            "lang": "de",
            "text": "Therapie \u2022 Re: Alkoholkonsum mit KISS reduzieren https://t.co/xWOwUaP6lg"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T18:15:53.000Z",
            "id": "685887734850940928",
            "lang": "de",
            "text": "Therapie \u2022 Re: Alkoholkonsum mit KISS reduzieren https://t.co/pyMw1hYdIv"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T18:15:53.000Z",
            "id": "685887734196617216",
            "lang": "de",
            "text": "Therapie \u2022 Re: Alkoholkonsum mit KISS reduzieren https://t.co/HG9OmFhqbu"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T18:15:53.000Z",
            "id": "685887733374529536",
            "lang": "de",
            "text": "Therapie \u2022 Alkoholkonsum mit KISS reduzieren https://t.co/Hawz3oVBTZ"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T17:14:22.000Z",
            "id": "685872250923433984",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Re: Selincro-Forum gibt bekannt https://t.co/Fn7KmBcVjF"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T17:14:22.000Z",
            "id": "685872250281680897",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Re: Selincro-Forum gibt bekannt https://t.co/6Zi1mHkrnp"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T10:46:34.000Z",
            "id": "685774658382229504",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Selincro-Forum gibt bekannt https://t.co/y5cTDvm0cw"
        },
        {
            "author_id": "1163813676",
            "created_at": "2016-01-09T10:46:25.000Z",
            "id": "685774621627559936",
            "lang": "en",
            "text": "\"#Alcoholism: prescribing #baclofen, to whom? how?\" Philippe Jaury (Bacloville) @ seminar Revue LE FLYER. In French. https://t.co/QXGouxGOy7"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-09T09:49:38.000Z",
            "id": "685760332422320128",
            "lang": "de",
            "text": "International Science Articles \u2022 Re: 2016 Mann : Wirkt Acamprosat \u00fcber Calcium ? https://t.co/N87KdCkUlY"
        },
        {
            "author_id": "1032288734",
            "created_at": "2016-01-09T08:34:52.000Z",
            "id": "685741514589376512",
            "lang": "en",
            "text": "French biotech Pharnext - Alzheimer's symptomatic approach: https://t.co/El3DSuewKY. Baclofen/acamprosate combo. Ph2b planning stage."
        },
        {
            "author_id": "240039418",
            "created_at": "2016-01-08T20:11:51.000Z",
            "id": "685554528113012741",
            "lang": "en",
            "text": "TMJ and the problem with Baclofen - it causes leg pain https://t.co/4463JaCm3L #JawPain"
        },
        {
            "author_id": "1117930724",
            "created_at": "2016-01-08T20:11:33.000Z",
            "id": "685554452552675328",
            "lang": "en",
            "text": "TMJ and the problem with Baclofen - it causes leg pain https://t.co/ZZEmoS25C3 #JawPain"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-08T18:24:35.000Z",
            "id": "685527536852402176",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/4Go8ir5QHd"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-08T16:05:11.000Z",
            "id": "685492453571473408",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Pr\u00e4sentation eines revolution\u00e4ren Produkts: PEGIDA\u2122 https://t.co/AIfUJtuNes"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-08T14:50:04.000Z",
            "id": "685473550808039424",
            "lang": "de",
            "text": "International Science Articles \u2022 2016 Mann : Wirkt Acamprosat \u00fcber Calcium ? https://t.co/WXrGVSbPQB"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-08T12:24:45.000Z",
            "id": "685436978054217729",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/pYFwuap4i2"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-08T12:24:44.000Z",
            "id": "685436977399869440",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/7aXGPzYB5H"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-08T11:23:03.000Z",
            "id": "685421453379006465",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/g1VFhX3xui"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-08T10:17:04.000Z",
            "id": "685404847265452032",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/ANFFdMihZc"
        },
        {
            "author_id": "2180234989",
            "created_at": "2016-01-08T00:41:43.000Z",
            "id": "685260054921146368",
            "lang": "en",
            "text": "Testing out Baclofen for the first time \u2014 any rec\u2026 https://t.co/uxZm01icvQ"
        },
        {
            "author_id": "2344962830",
            "created_at": "2016-01-08T00:01:40.000Z",
            "id": "685249975417180160",
            "lang": "en",
            "text": "Testing out Baclofen for the first time -- any recommendations? via /r/Nootropics https://t.co/5CivFFLQaW"
        },
        {
            "author_id": "4025056282",
            "created_at": "2016-01-07T23:29:44.000Z",
            "id": "685241941336940548",
            "lang": "en",
            "text": "Testing out Baclofen for the first time -- any recommendations? https://t.co/e24MXZyWHH"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-07T18:40:34.000Z",
            "id": "685169170707804160",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/Fy1VYKaSOe"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-07T18:37:07.000Z",
            "id": "685168301354385408",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/YyG6wV50w9"
        },
        {
            "author_id": "2647139192",
            "created_at": "2016-01-07T17:54:07.000Z",
            "id": "685157479265615875",
            "lang": "en",
            "text": "sext: i carelessly strengthen my wrists while you carelessly take 40-80 mg of baclofen (lioresal) every day"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-07T13:09:49.000Z",
            "id": "685085933650186241",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/hJhls3c0PY"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-07T12:02:48.000Z",
            "id": "685069066860642305",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/zj0qPi2cAT"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-07T07:52:03.000Z",
            "id": "685005964119019520",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/hCOkci7hDL"
        },
        {
            "author_id": "123700394",
            "created_at": "2016-01-07T01:31:24.000Z",
            "id": "684910171286564864",
            "lang": "en",
            "text": "I had blood work done last month @LindsMRoach because of my baclofen. I've been taking it over a decade now. #CPChatNow"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T18:27:21.000Z",
            "id": "684803455987355649",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/lxoXGldMa8"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T16:10:58.000Z",
            "id": "684769135008550912",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Chemsex \u2013 besser, h\u00f6her, weiter, l\u00e4nger https://t.co/ql1xie9PWU"
        },
        {
            "author_id": "3022845860",
            "created_at": "2016-01-06T15:42:48.000Z",
            "id": "684762046953435136",
            "lang": "zh",
            "text": "https://t.co/PGCPamzjXy #iAsk #\u6210\u4efd #\u85e5\u54c1 #\u5291\u91cf #\u526f\u4f5c\u7528 #\u91ab\u7642 BACLOFEN TABLETS 5MG\"JOHNSON\"\u88e1\u9762\u6709\u4ec0\u9ebc\u6210\u4efd\uff1f"
        },
        {
            "author_id": "836692002",
            "created_at": "2016-01-06T15:23:40.000Z",
            "id": "684757232148451328",
            "lang": "es",
            "text": "@FundacionBADAN buenos dias estoy buscando baclofen de 10mg tienen disponible? Gracias de antemano"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T13:40:46.000Z",
            "id": "684731334733000704",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/q6K15h1fLU"
        },
        {
            "author_id": "3240571529",
            "created_at": "2016-01-06T11:56:11.000Z",
            "id": "684705015458574337",
            "lang": "en",
            "text": "RT @baclofenews: Obsrv Study 316 pts: Low-Dose #Baclofen &amp; #Topiramate as effective as #Acamprosate in the management of #alcoholism. https\u2026"
        },
        {
            "author_id": "1163813676",
            "created_at": "2016-01-06T10:45:47.000Z",
            "id": "684687297929998336",
            "lang": "en",
            "text": "Obsrv Study 316 pts: Low-Dose #Baclofen &amp; #Topiramate as effective as #Acamprosate in the management of #alcoholism. https://t.co/2xFJgOlUdf"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T09:33:20.000Z",
            "id": "684669065089122304",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/Za5DTJzk9l"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T09:33:20.000Z",
            "id": "684669064460038144",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/WOQwB3OSNT"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T09:33:20.000Z",
            "id": "684669063847653376",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/4Uog1H3Rem"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T09:33:19.000Z",
            "id": "684669063239495680",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/qTjd9Vuqkx"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T09:33:18.000Z",
            "id": "684669059275878401",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/7ZuD428BCy"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T08:33:18.000Z",
            "id": "684653959387168768",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/LexnjXSCCr"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-06T08:13:33.000Z",
            "id": "684648987190800384",
            "lang": "en",
            "text": "Baclofen 10mg order no rx. Can I Purchase Lioresal  Online https://t.co/oSa1CO0Ouy #medical #blog #health"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T06:30:39.000Z",
            "id": "684623092065419264",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/ciR4THwIef"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T06:30:39.000Z",
            "id": "684623091306225664",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/At81RXFVNs"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-06T06:30:37.000Z",
            "id": "684623082607218689",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/D0xjL9BJVV"
        },
        {
            "author_id": "258334052",
            "created_at": "2016-01-06T02:59:18.000Z",
            "id": "684569903286890496",
            "lang": "en",
            "text": "lowest prices Baclofen credit card no prescription | purchase Baclofen: where can i buy Baclofen no prescription\u2026"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-05T19:18:44.000Z",
            "id": "684453998217269248",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/mfqeg8xwPG"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-05T17:13:05.000Z",
            "id": "684422377942478849",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/MgnW2dzpeh"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-05T14:08:09.000Z",
            "id": "684375838700081152",
            "lang": "en",
            "text": "I came here to work &lt;a href=\" https://t.co/VM3PRAcz6z \"&gt;generic ba... https://t.co/rYqoutcDzt"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-05T12:46:34.000Z",
            "id": "684355308425228288",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/R5AfLF6xYK"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-05T11:45:15.000Z",
            "id": "684339876150534144",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/pZqCAw4MId"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-05T11:43:52.000Z",
            "id": "684339527054397441",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/LQPYE2ZFGC"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-05T07:49:10.000Z",
            "id": "684280465201741824",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/ILPXCE35v0"
        },
        {
            "author_id": "95924248",
            "created_at": "2016-01-04T19:06:44.000Z",
            "id": "684088591467831297",
            "lang": "en",
            "text": "RT @AllisonDaurio: RadioLab's podcast inspired by Baclofen's effect on alcoholism cc @MehdiFarokhnia\nhttps://t.co/fCvgOMWli7"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T18:02:22.000Z",
            "id": "684072394449883137",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/AjbV5oJjP3"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T16:57:21.000Z",
            "id": "684056029450104832",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/rzTIceA4dp"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T14:45:17.000Z",
            "id": "684022794699575296",
            "lang": "de",
            "text": "Baclofen und Alkoholabh\u00e4ngigkeit \u2022 Re: S3-Leitlinie \u201cScreening, Diagn., Behandl. alkoholbez\u2026 https://t.co/2lTXq3VrsG"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-04T11:45:48.000Z",
            "id": "683977627326115840",
            "lang": "en",
            "text": "Baclofen 25mg buy online. How to Order Lioresal  Online https://t.co/7vLJsx4q2M #medical #blog #health"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T07:29:43.000Z",
            "id": "683913181459275776",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/4ujdRlv1Vn"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T07:29:43.000Z",
            "id": "683913180670758917",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/nPmVUn3csq"
        },
        {
            "author_id": "3333435313",
            "created_at": "2016-01-04T06:59:10.000Z",
            "id": "683905490976256000",
            "lang": "en",
            "text": "#StiffPersonSyndrome body pain; screaming all day; 42-2mgs-Ativan, 27-10mgs-Valium, 12-10mgs-Baclofen #stemcell help https://t.co/G78KE8FakO"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T06:14:36.000Z",
            "id": "683894278410600448",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/noWh9f2IPX"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T05:25:44.000Z",
            "id": "683881977842274304",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/6GHgAsiuCA"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T05:25:43.000Z",
            "id": "683881976835645441",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/APMQs0ezj5"
        },
        {
            "author_id": "274656839",
            "created_at": "2016-01-04T03:12:15.000Z",
            "id": "683848386861228032",
            "lang": "en",
            "text": "@LilyCrue I've tried meds with side effect of sleepiness and still nothing - I'm already on morphine and Baclofen - both not helping sleep!"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T02:32:12.000Z",
            "id": "683838309139877888",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/nOZOz0qWql"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-04T01:36:36.000Z",
            "id": "683824315897364480",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/5g51Iy09X4"
        },
        {
            "author_id": "1052681628",
            "created_at": "2016-01-03T22:11:15.000Z",
            "id": "683772636577558528",
            "lang": "en",
            "text": "@obgynkenobi thanks.  May take baclofen a bit earlier...I think I'm just a bit overtired"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T19:02:58.000Z",
            "id": "683725255299477505",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/bbo34RMVPL"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T19:02:58.000Z",
            "id": "683725254578049024",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/70D77fBYmx"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T18:03:51.000Z",
            "id": "683710376744206336",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/ylkSPhq4Gp"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T17:05:38.000Z",
            "id": "683695729039306752",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Re: Muskelschmerzen? https://t.co/PzA6S9I9tM"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T16:08:16.000Z",
            "id": "683681289912881152",
            "lang": "de",
            "text": "Nebenwirkungen \u2022 Muskelschmerzen? https://t.co/imv9dXHCyQ"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T12:15:08.000Z",
            "id": "683622621448159233",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Re: Selincro-Forum erstellt Leitfaden ohne Selincro https://t.co/puKhzKUWmS"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T09:25:50.000Z",
            "id": "683580014789586944",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/qdvaXcFLaF"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T09:25:50.000Z",
            "id": "683580013984243712",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/k83kFqjNzf"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T09:25:48.000Z",
            "id": "683580005692092416",
            "lang": "de",
            "text": "Medienberichte Baclofen \u2022 Re: Baclad und Baclofen in der Trokkenpresse https://t.co/8a20QRpLRU"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T07:28:44.000Z",
            "id": "683550546930888704",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Re: Selincro-Forum erstellt Leitfaden ohne Selincro https://t.co/RnE8rW2hJo"
        },
        {
            "author_id": "3114650311",
            "created_at": "2016-01-03T07:05:57.000Z",
            "id": "683544810192375809",
            "lang": "und",
            "text": "https://t.co/IDIV37Il8S"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T05:31:01.000Z",
            "id": "683520922993737728",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/XY2GuADoSx"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-03T05:30:58.000Z",
            "id": "683520910683406336",
            "lang": "de",
            "text": "Medienberichte Baclofen \u2022 Re: Baclad und Baclofen in der Trokkenpresse https://t.co/aUEdNwEbyR"
        },
        {
            "author_id": "3114650311",
            "created_at": "2016-01-03T02:21:27.000Z",
            "id": "683473214698164224",
            "lang": "und",
            "text": "https://t.co/yaFeJpDCZG"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-03T01:08:04.000Z",
            "id": "683454747584499712",
            "lang": "en",
            "text": "I'm on holiday &lt;a href=\" https://t.co/kNu6zlU9yn \"&gt;bac... https://t.co/yiHtRpJb2m"
        },
        {
            "author_id": "117443647",
            "created_at": "2016-01-03T01:08:03.000Z",
            "id": "683454742870138880",
            "lang": "en",
            "text": "I can't get through at the moment &lt;a href=\" https://t.co/jL0yt9yU8R... https://t.co/kwxFIvho0R"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T19:14:42.000Z",
            "id": "683365819359838208",
            "lang": "de",
            "text": "Medienberichte Baclofen \u2022 Re: Baclad und Baclofen in der Trokkenpresse https://t.co/PYAKb8r9Nj"
        },
        {
            "author_id": "1052681628",
            "created_at": "2016-01-02T18:41:27.000Z",
            "id": "683357452209917953",
            "lang": "en",
            "text": "@MSj_MSpartytime bless you. Yes I take baclofen. Sadly gabapentin doesn't help.  I'm trying pregabalin. But no joy yet.   Thank you though"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T14:16:50.000Z",
            "id": "683290860604264448",
            "lang": "de",
            "text": "Medienberichte Baclofen \u2022 Re: Baclad und Baclofen in der Trokkenpresse https://t.co/I38w3nrD5m"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T14:16:50.000Z",
            "id": "683290859987693568",
            "lang": "de",
            "text": "Medienberichte Baclofen \u2022 Re: Baclad und Baclofen in der Trokkenpresse https://t.co/XvN65L7kkQ"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T10:21:47.000Z",
            "id": "683231705847693312",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/t1KygEk51B"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T10:21:46.000Z",
            "id": "683231705055014912",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/MnCpKFCa0A"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T09:23:33.000Z",
            "id": "683217051968761856",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/3uSPOphbCv"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T09:23:33.000Z",
            "id": "683217051444490240",
            "lang": "de",
            "text": "Erfolgsgeschichten \u2022 Re: Erfolgsgeschichten https://t.co/7qGQKFn4qh"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T06:32:27.000Z",
            "id": "683173995127156736",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Re: Selincro-Forum erstellt Leitfaden ohne Selincro https://t.co/QMoz4IRjJk"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-02T06:32:26.000Z",
            "id": "683173987426373632",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/Xk6q8yD1ZU"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-01T18:17:35.000Z",
            "id": "682989059501850624",
            "lang": "de",
            "text": "Neues aus der Anstalt \u2022 Selincro-Forum erstellt Leitfaden ohne Selincro https://t.co/23HG2W1f4W"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-01T16:19:18.000Z",
            "id": "682959292706766848",
            "lang": "de",
            "text": "Erfolgsgeschichten \u2022 Re: Erfolgsgeschichten https://t.co/kmU8Jv41wN"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-01T15:22:48.000Z",
            "id": "682945071226949632",
            "lang": "de",
            "text": "Erfolgsgeschichten \u2022 Nicht nur Baclofen sondern auch... https://t.co/Tqmp0JPUJw"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-01T14:27:09.000Z",
            "id": "682931067733585920",
            "lang": "de",
            "text": "Langzeiterfahrung Baclofen \u2022 Nicht nur Baclofen sondern auch... https://t.co/tCP08rmmpL"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-01T10:37:26.000Z",
            "id": "682873256534261760",
            "lang": "de",
            "text": "Erfahrungsberichte Alkohol und Baclofen \u2022 Re: Jettes Weg https://t.co/3YhptRnUJr"
        },
        {
            "author_id": "1477854085",
            "created_at": "2016-01-01T02:07:52.000Z",
            "id": "682745019971842048",
            "lang": "de",
            "text": "Langzeiterfahrung Baclofen \u2022 Re: Hochdosierungsprojekt https://t.co/zClkf3pQFi"
        },
        {
            "author_id": "83480353",
            "created_at": "2016-01-01T00:17:47.000Z",
            "id": "682717319404064768",
            "lang": "cy",
            "text": "Baclofen Pump - 5 Month Pumpdate: https://t.co/YRnFWJkFO6 via @YouTube"
        },
        {
            "author_id": "3299571025",
            "created_at": "2016-01-01T00:10:35.000Z",
            "id": "682715506181193728",
            "lang": "fr",
            "text": "https://t.co/5A55URWq8Y #iAsk #BACTON #TABLETS #10MG #\"S.C.\"(BACLOFEN) #\u5b78\u540d\u85e5 BACTON TABLETS 10MG \"S.C.\"(BACLOFEN)..."
        }
    ],
    "meta": {
        "newest_id": "693899449903480837",
        "oldest_id": "682715506181193728",
        "result_count": 254
    }
}{
    "data": [
        {
            "author_id": "3299571025",
            "created_at": "2016-01-21T17:39:40.000Z",
            "id": "690227274373685248",
            "lang": "ja",
            "text": "https://t.co/3ymqTSCF35 #iAsk #\u85e5\u54c1 #\u91ab\u7642 #\u6210\u85e5 #\u61f7\u5b55 #\u5b55\u5a66 \u61f7\u5b55\u53ef\u4ee5\u4f7f\u7528BACLOSPAS TABLETS 5MG\u55ce\uff1f"
        }
    ],
    "meta": {
        "newest_id": "690227274373685248",
        "oldest_id": "690227274373685248",
        "result_count": 1
    }
}{
    "meta": {
        "result_count": 0
    }
}{
    "meta": {
        "result_count": 0
    }
}{
    "meta": {
        "result_count": 0
    }
}{
    "data": [
        {
            "author_id": "45868485",
            "created_at": "2016-01-30T19:35:34.000Z",
            "id": "693517931225939970",
            "lang": "es",
            "text": "@wettel si ella tomaba Lioresal que la ayudaba con esos espasmos... pero ya no se consigue.... y ha logrado sobreponerse"
        },
        {
            "author_id": "258334052",
            "created_at": "2016-01-30T02:18:29.000Z",
            "id": "693256942140178432",
            "lang": "en",
            "text": "Lioresal | Orders ,Next Day No Prescription In Australia | Order Online Cheap Lioresal: Wholesale Lioresal Without\u2026"
        },
        {
            "author_id": "580407385",
            "created_at": "2016-01-29T14:43:37.000Z",
            "id": "693082074073448448",
            "lang": "es",
            "text": "@FundacionBADAN \u00bfTendr\u00e1n alguna presentaci\u00f3n de Baclofeno 10mg (Lioresal)? Para espasticidad por ACV"
        },
        {
            "author_id": "1700275219",
            "created_at": "2016-01-28T08:01:59.000Z",
            "id": "692618609336528897",
            "lang": "en",
            "text": "Lioresal Label: We've got six Polar Plunges around the state that help raise funds for and awaren-USess of Lio... https://t.co/ny8RiijUML"
        },
        {
            "author_id": "1178947488",
            "created_at": "2016-01-28T02:08:28.000Z",
            "id": "692529645804220416",
            "lang": "es",
            "text": "@ConElMazoDando la ni\u00f1a aleiber de 5 a\u00f1os esta complicada al parecer morir\u00e1 sin la medicamentos lioresal o baclofeno por favor ayudalos"
        },
        {
            "author_id": "581063862",
            "created_at": "2016-01-27T16:32:07.000Z",
            "id": "692384602946736128",
            "lang": "es",
            "text": "@LocatelVzla_ATC Buenas tardes, donde consigo Baclofeno o Lioresal de 10 o 25mg"
        },
        {
            "author_id": "2889357604",
            "created_at": "2016-01-26T18:36:49.000Z",
            "id": "692053595592769536",
            "lang": "es",
            "text": "RT @FARMAXIMA: #Urgente #medicamento  lioresal o baclofeno para su ayuda x favor x el 04144603470 04169467608 04124452846"
        },
        {
            "author_id": "2889357604",
            "created_at": "2016-01-26T18:22:01.000Z",
            "id": "692049870732001280",
            "lang": "es",
            "text": "RT @MariaDeJesusCG1: Soy Asdrubal Gonzalez, desesperadamente solicito: LIORESAL o BACLOFENO. Mi hija puede morir sin este medicamento. 0414\u2026"
        },
        {
            "author_id": "39766665",
            "created_at": "2016-01-26T17:10:09.000Z",
            "id": "692031786776444928",
            "lang": "es",
            "text": "@joseolivaresm #CrisisHumanitariaEnVenezuela no hay aprovel, arav\u00e1, daflon, valpron, benicar, olmetec, lioresal, madopar. Nos est\u00e1n matando"
        },
        {
            "author_id": "1329693092",
            "created_at": "2016-01-24T23:38:26.000Z",
            "id": "691404725888118785",
            "lang": "es",
            "text": "#ServicioP\u00fablico RILUTEK 50 MG y LIORESAL 10MG. Paciente en estado delicado. Agradecida"
        },
        {
            "author_id": "176171870",
            "created_at": "2016-01-24T17:34:54.000Z",
            "id": "691313238055743488",
            "lang": "es",
            "text": "@fybeca tienen lioresal o baclofeno? Alguna forma de que empiece ayuden a conseguirlo? Tengo la receta. Es para mi nena con PCI"
        },
        {
            "author_id": "176171870",
            "created_at": "2016-01-24T17:26:22.000Z",
            "id": "691311088659533824",
            "lang": "en",
            "text": "@Pharma_Data i need to buy lioresal. can I buy it online since I'm from Ecuador? I need it urgently  4 my daughter they don't sell it here"
        },
        {
            "author_id": "176171870",
            "created_at": "2016-01-23T03:42:06.000Z",
            "id": "690741269686030336",
            "lang": "es",
            "text": "Me ayudan con RT? Necesito pastillas Baclofeno o lioresal de 10mg URG. Si alguien tiene info por favor avisenme"
        },
        {
            "author_id": "2983200407",
            "created_at": "2016-01-23T01:07:28.000Z",
            "id": "690702356044988417",
            "lang": "et",
            "text": "#Pharmaceuticals LIORESAL 10 : Tablet : 10mg : Novartis Pharma AG, Switzerland : https://t.co/UtRNDTvRPs #MarketResearch #Statistics"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-22T21:03:49.000Z",
            "id": "690641036658499584",
            "lang": "en",
            "text": "Order Baclofen 10 mg Low Price - How to Purchase Lioresal Fast Delivery https://t.co/UvF0qMiugn #medical #blog #health"
        },
        {
            "author_id": "538243508",
            "created_at": "2016-01-22T17:52:32.000Z",
            "id": "690592897666658304",
            "lang": "in",
            "text": "Forum Pompe Lioresal https://t.co/EjRTiUqleq"
        },
        {
            "author_id": "1223435814",
            "created_at": "2016-01-21T23:09:19.000Z",
            "id": "690310233147711488",
            "lang": "es",
            "text": "URGENTE RT. se necesita BACLOFENO o LIORESAL en cualquier presentacion para ni\u00f1a d 5 a\u00f1os.Telf.0414-4603470. 0416-9467608. ASDRUBAL GONZALEZ"
        },
        {
            "author_id": "4151058453",
            "created_at": "2016-01-21T19:02:55.000Z",
            "id": "690248222326046721",
            "lang": "es",
            "text": "@LaHojillaenTV camarada ayudame a conseguir el medicamento Lioresal de 10mg en tableta.(Baclofen) soy docente y estoy en silla.04167411458"
        },
        {
            "author_id": "287813303",
            "created_at": "2016-01-21T15:31:46.000Z",
            "id": "690195087846940672",
            "lang": "es",
            "text": "RT @nicolasgreige: LIORESAL o BACLOFENO URGENTE!!!..para ni\u00f1a 5 a\u00f1os recluida en el HCM d Aragua.Llamar al 04144603470 04169467608 04124452\u2026"
        },
        {
            "author_id": "287813303",
            "created_at": "2016-01-21T15:31:35.000Z",
            "id": "690195041323728896",
            "lang": "es",
            "text": "RT @mary2012f: @FLaPastillita Urgente  lioresal o baclofeno.en la presentaci\u00f3n q sea d los Ml q sea, la ni\u00f1a puede morir sin esta medicina.\u2026"
        },
        {
            "author_id": "287813303",
            "created_at": "2016-01-21T15:31:29.000Z",
            "id": "690195013276405760",
            "lang": "es",
            "text": "RT @Ascensaojose: (MARACAY) Amigos soy Asdrubal Gonzales,  les solicito Urgente  lioresal o baclofeno. Comunicarse 04144603470 04169467608 \u2026"
        },
        {
            "author_id": "318456073",
            "created_at": "2016-01-21T14:52:00.000Z",
            "id": "690185080019533826",
            "lang": "es",
            "text": "RT @Ascensaojose: (MARACAY) Amigos soy Asdrubal Gonzales,  les solicito Urgente  lioresal o baclofeno. Comunicarse 04144603470 04169467608 \u2026"
        },
        {
            "author_id": "105516888",
            "created_at": "2016-01-20T15:20:22.000Z",
            "id": "689829828082679808",
            "lang": "es",
            "text": "RT @Ascensaojose: (MARACAY) Amigos soy Asdrubal Gonzales,  les solicito Urgente  lioresal o baclofeno. Comunicarse 04144603470 04169467608 \u2026"
        },
        {
            "author_id": "120296332",
            "created_at": "2016-01-20T13:57:52.000Z",
            "id": "689809068316323840",
            "lang": "es",
            "text": "(MARACAY) Amigos soy Asdrubal Gonzales,  les solicito Urgente  lioresal o baclofeno. Comunicarse 04144603470 04169467608 04124452846 Urgent"
        },
        {
            "author_id": "429286081",
            "created_at": "2016-01-20T13:34:40.000Z",
            "id": "689803230566584320",
            "lang": "es",
            "text": "@FLaPastillita Urgente  lioresal o baclofeno.en la presentaci\u00f3n q sea d los Ml q sea, la ni\u00f1a puede morir sin esta medicina. 04144603470"
        },
        {
            "author_id": "429286081",
            "created_at": "2016-01-20T13:32:33.000Z",
            "id": "689802695448907776",
            "lang": "es",
            "text": "@FundacionBADAN Urgente  lioresal o baclofeno.en la presentaci\u00f3n q sea d los Ml q sea, la ni\u00f1a puede morir sin este medicina. 04144603470"
        },
        {
            "author_id": "4209816358",
            "created_at": "2016-01-20T06:10:28.000Z",
            "id": "689691442801876992",
            "lang": "en",
            "text": "Where to Buy Baclofen (Lioresal) 10, 25\u00a0mg https://t.co/wN8eHtNvhe"
        },
        {
            "author_id": "190285554",
            "created_at": "2016-01-20T02:47:58.000Z",
            "id": "689640482939478016",
            "lang": "es",
            "text": "Urgente  lioresal o baclofeno matar bacteria t\u00e9tano.Aleiber d 5 a\u00f1os recluida HCM d Aragua04144603470 04169467608 04124452846"
        },
        {
            "author_id": "233025737",
            "created_at": "2016-01-19T21:36:10.000Z",
            "id": "689562016172904448",
            "lang": "es",
            "text": "LIORESAL o BACLOFENO URGENTE!!!..para ni\u00f1a 5 a\u00f1os recluida en el HCM d Aragua.Llamar al 04144603470 04169467608 04124452846\nURGENTE..!"
        },
        {
            "author_id": "197422765",
            "created_at": "2016-01-18T00:38:24.000Z",
            "id": "688883098164027393",
            "lang": "es",
            "text": "RT @Lakers2808Maria: URGENTE lioresal o baclofeno en la presentaci\u00f3n q sea llama:  04144603470 04169467608 04124452846 salva una vida d una\u2026"
        },
        {
            "author_id": "2983200407",
            "created_at": "2016-01-17T14:54:28.000Z",
            "id": "688736148122914817",
            "lang": "et",
            "text": "#Pharmaceuticals LIORESAL 25 : Tablet : 25mg : Novartis Pharma AG, Switzerland : https://t.co/60SqnhLX7i #MarketResearch #Statistics"
        },
        {
            "author_id": "2907005745",
            "created_at": "2016-01-16T11:17:56.000Z",
            "id": "688319265955561472",
            "lang": "es",
            "text": "#Pharmaceutical baclofen : Lioresal Intrathecal : https://t.co/eSCC4VuxIi #MRX #Surveys #MarketResearchReports #Forecasts #Marketing"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-15T22:39:21.000Z",
            "id": "688128363144187904",
            "lang": "en",
            "text": "Baclofen 25mg buy - Where Can I Buy Lioresal  Online https://t.co/P6IMJb9ITd #medical #blog #health"
        },
        {
            "author_id": "29235177",
            "created_at": "2016-01-14T02:12:10.000Z",
            "id": "687457144749322240",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado #serviciopublico @LuisChat\u2026"
        },
        {
            "author_id": "107228890",
            "created_at": "2016-01-14T02:05:10.000Z",
            "id": "687455386069266433",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado #serviciopublico @LuisChat\u2026"
        },
        {
            "author_id": "2491601004",
            "created_at": "2016-01-13T21:46:11.000Z",
            "id": "687390210150297601",
            "lang": "es",
            "text": "RT @ariadnerv: @Akiztapp @Donatumed @DonaMed_VE Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral! (\u2026"
        },
        {
            "author_id": "150665250",
            "created_at": "2016-01-13T21:38:00.000Z",
            "id": "687388148217843712",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "358357002",
            "created_at": "2016-01-13T21:29:48.000Z",
            "id": "687386085949845504",
            "lang": "es",
            "text": "RT @ariadnerv: @Akiztapp @Donatumed @DonaMed_VE Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral! (\u2026"
        },
        {
            "author_id": "2801700121",
            "created_at": "2016-01-13T21:25:11.000Z",
            "id": "687384924287037440",
            "lang": "es",
            "text": "RT @Akiztapp: @ariadnerv @Donatumed @DonaMed_VE no disponib Lioresal en nuestras farmacias afiliadas"
        },
        {
            "author_id": "274658489",
            "created_at": "2016-01-13T21:23:57.000Z",
            "id": "687384614160220161",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado #serviciopublico @LuisChat\u2026"
        },
        {
            "author_id": "48755280",
            "created_at": "2016-01-13T21:22:41.000Z",
            "id": "687384293891543044",
            "lang": "es",
            "text": "RT @ariadnerv: @Akiztapp @Donatumed @DonaMed_VE Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral! (\u2026"
        },
        {
            "author_id": "1944979663",
            "created_at": "2016-01-13T21:21:22.000Z",
            "id": "687383962889662465",
            "lang": "es",
            "text": "RT @ariadnerv: @Akiztapp @Donatumed @DonaMed_VE Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral! (\u2026"
        },
        {
            "author_id": "1944979663",
            "created_at": "2016-01-13T21:21:15.000Z",
            "id": "687383935442141185",
            "lang": "es",
            "text": "@ariadnerv @Donatumed @DonaMed_VE no disponib Lioresal en nuestras farmacias afiliadas"
        },
        {
            "author_id": "2265346234",
            "created_at": "2016-01-13T20:57:15.000Z",
            "id": "687377894029537284",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "1329685160",
            "created_at": "2016-01-13T20:35:01.000Z",
            "id": "687372297968160769",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "146153597",
            "created_at": "2016-01-13T20:24:33.000Z",
            "id": "687369663655886848",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "29146092",
            "created_at": "2016-01-13T20:23:55.000Z",
            "id": "687369505232785408",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "729237948",
            "created_at": "2016-01-13T20:09:28.000Z",
            "id": "687365870197338114",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "177228977",
            "created_at": "2016-01-13T20:07:58.000Z",
            "id": "687365492890308614",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "598621305",
            "created_at": "2016-01-13T20:06:22.000Z",
            "id": "687365087817023488",
            "lang": "es",
            "text": "RT @martinezantia: \"@ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi herm\u2026"
        },
        {
            "author_id": "116958579",
            "created_at": "2016-01-13T19:57:57.000Z",
            "id": "687362972939894784",
            "lang": "es",
            "text": "RT @martinezantia: \"@ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi herm\u2026"
        },
        {
            "author_id": "141034266",
            "created_at": "2016-01-13T19:55:37.000Z",
            "id": "687362382713229316",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado #serviciopublico @LuisChat\u2026"
        },
        {
            "author_id": "1377548004",
            "created_at": "2016-01-13T19:54:29.000Z",
            "id": "687362096544235520",
            "lang": "es",
            "text": "RT @martinezantia: \"@ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi herm\u2026"
        },
        {
            "author_id": "151689431",
            "created_at": "2016-01-13T19:52:29.000Z",
            "id": "687361594146291712",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "131989124",
            "created_at": "2016-01-13T19:52:13.000Z",
            "id": "687361527020695554",
            "lang": "es",
            "text": "\"@ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor"
        },
        {
            "author_id": "4094799465",
            "created_at": "2016-01-13T19:51:07.000Z",
            "id": "687361252595789826",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado #serviciopublico @LuisChat\u2026"
        },
        {
            "author_id": "380042629",
            "created_at": "2016-01-13T19:48:09.000Z",
            "id": "687360505799917568",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "23383698",
            "created_at": "2016-01-13T19:48:05.000Z",
            "id": "687360488632659968",
            "lang": "es",
            "text": "@Akiztapp @Donatumed @DonaMed_VE Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral! (Se puede pagar)"
        },
        {
            "author_id": "218898502",
            "created_at": "2016-01-13T19:46:58.000Z",
            "id": "687360204925702144",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado #serviciopublico @LuisChat\u2026"
        },
        {
            "author_id": "94893640",
            "created_at": "2016-01-13T19:44:42.000Z",
            "id": "687359635578318848",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "63810438",
            "created_at": "2016-01-13T19:36:04.000Z",
            "id": "687357464157753344",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "517785662",
            "created_at": "2016-01-13T19:34:58.000Z",
            "id": "687357184880029697",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "28406605",
            "created_at": "2016-01-13T19:33:19.000Z",
            "id": "687356772844204032",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "126294991",
            "created_at": "2016-01-13T19:32:49.000Z",
            "id": "687356644083105792",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "323511233",
            "created_at": "2016-01-13T19:31:34.000Z",
            "id": "687356332886851587",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "175953733",
            "created_at": "2016-01-13T19:31:04.000Z",
            "id": "687356205715603456",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "230519818",
            "created_at": "2016-01-13T19:29:51.000Z",
            "id": "687355901142020096",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "139087428",
            "created_at": "2016-01-13T19:29:07.000Z",
            "id": "687355714499645440",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "44972100",
            "created_at": "2016-01-13T19:28:58.000Z",
            "id": "687355678382518273",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "382641507",
            "created_at": "2016-01-13T19:27:57.000Z",
            "id": "687355422559322112",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "109770017",
            "created_at": "2016-01-13T19:27:41.000Z",
            "id": "687355355546923008",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT\u2026"
        },
        {
            "author_id": "289590628",
            "created_at": "2016-01-13T19:27:12.000Z",
            "id": "687355233429811201",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "188934723",
            "created_at": "2016-01-13T19:23:54.000Z",
            "id": "687354402584293380",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "2419546362",
            "created_at": "2016-01-13T19:23:28.000Z",
            "id": "687354293473677313",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "107918350",
            "created_at": "2016-01-13T19:21:39.000Z",
            "id": "687353835191451648",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "48167275",
            "created_at": "2016-01-13T19:17:02.000Z",
            "id": "687352675445436416",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "17087514",
            "created_at": "2016-01-13T19:16:48.000Z",
            "id": "687352615559139328",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "221788661",
            "created_at": "2016-01-13T19:16:24.000Z",
            "id": "687352513046142976",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "29146092",
            "created_at": "2016-01-13T19:16:05.000Z",
            "id": "687352436772737025",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "258527879",
            "created_at": "2016-01-13T19:15:41.000Z",
            "id": "687352335245389824",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "134182485",
            "created_at": "2016-01-13T19:15:13.000Z",
            "id": "687352217788125185",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "126332323",
            "created_at": "2016-01-13T19:15:03.000Z",
            "id": "687352173756289024",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "23383698",
            "created_at": "2016-01-13T19:10:31.000Z",
            "id": "687351033673158656",
            "lang": "es",
            "text": "Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado #serviciopublico @LuisChataing porfa Rt \ud83d\ude4f\ud83c\udffb"
        },
        {
            "author_id": "202868430",
            "created_at": "2016-01-13T19:10:29.000Z",
            "id": "687351024126980096",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "23559248",
            "created_at": "2016-01-13T19:09:59.000Z",
            "id": "687350897702236160",
            "lang": "es",
            "text": "RT @ariadnerv: Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "23383698",
            "created_at": "2016-01-13T19:09:33.000Z",
            "id": "687350790248370176",
            "lang": "es",
            "text": "Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado por favor Rt!! @CATERINAV"
        },
        {
            "author_id": "23383698",
            "created_at": "2016-01-13T19:09:09.000Z",
            "id": "687350690256154625",
            "lang": "es",
            "text": "Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para mi hermano con trauma cerebral delicado, por favor Rt!! @MelanioBar"
        },
        {
            "author_id": "23383698",
            "created_at": "2016-01-13T19:08:21.000Z",
            "id": "687350486740156416",
            "lang": "es",
            "text": "Se requiere LIORESAL comp 10 mg y RITALIN comp 10 mg para paciente con trauma cerebral delicado, es mi hermano! Por favor RT @ElNacionalWeb"
        },
        {
            "author_id": "409362399",
            "created_at": "2016-01-13T16:21:18.000Z",
            "id": "687308447826722816",
            "lang": "es",
            "text": "URGENTE lioresal o baclofeno en la presentaci\u00f3n q sea llama:  04144603470 04169467608 04124452846 salva una vida d una ni\u00f1a 5anos en el HCM"
        },
        {
            "author_id": "394215646",
            "created_at": "2016-01-12T22:46:36.000Z",
            "id": "687043023776165889",
            "lang": "en",
            "text": "RT @wikisext: sext: i carelessly strengthen my wrists while you carelessly take 40-80 mg of baclofen (lioresal) every day"
        },
        {
            "author_id": "67814612",
            "created_at": "2016-01-12T15:43:05.000Z",
            "id": "686936445261623296",
            "lang": "es",
            "text": "@TaniaGRM PARA MI SOBRINO DE 3 A\u00d1OS DE EDAD CON PARALISIS CEREBRAL NECESITO LIORESAL DE 10MG MI CEL 04245159501"
        },
        {
            "author_id": "67814612",
            "created_at": "2016-01-12T15:42:42.000Z",
            "id": "686936348532600832",
            "lang": "es",
            "text": "@TaniaGRM PARA MI SOBRINO DE 3 A\u00d1OS DE EDAD CON PARALISIS CEREBRAL NECESITO LIORESAL DE 10MG MI CEL 04245159501 DIOS TE SIGA BENDICIENDO"
        },
        {
            "author_id": "67814612",
            "created_at": "2016-01-12T15:34:49.000Z",
            "id": "686934364962295809",
            "lang": "es",
            "text": "@TaniaGRM saludos coraz\u00f3n me puedas ayudar mi sobrino de 3 a\u00f1os tiene Paralisis cerebral necesita lioresal de 10mg https://t.co/5JhuydygKL"
        },
        {
            "author_id": "1119302575",
            "created_at": "2016-01-11T16:01:48.000Z",
            "id": "686578764554342400",
            "lang": "es",
            "text": "Lioresal o baclofeno para ni\u00f1a en HC de Mcy grave por t\u00e9tano se requiere urgente."
        },
        {
            "author_id": "1400893268",
            "created_at": "2016-01-11T14:11:11.000Z",
            "id": "686550930377076737",
            "lang": "es",
            "text": "RT @FundacionBADAN: Buen d\u00eda @enfunbe BACLOFENO 10MG/20ML AMP LIORESAL INTRATE disponible en algunas sucursales, saludos"
        },
        {
            "author_id": "168492310",
            "created_at": "2016-01-11T14:08:38.000Z",
            "id": "686550288539463680",
            "lang": "es",
            "text": "Buen d\u00eda @enfunbe BACLOFENO 10MG/20ML AMP LIORESAL INTRATE disponible en algunas sucursales, saludos"
        },
        {
            "author_id": "2228600343",
            "created_at": "2016-01-10T16:10:43.000Z",
            "id": "686218622210064385",
            "lang": "es",
            "text": "Urgente LIORESAL o BACLOFENO. Paciente de 5 a\u00f1os HCM Maracay. CTC 04144603470 04169467608 04124452846"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-10T14:36:32.000Z",
            "id": "686194921766793216",
            "lang": "en",
            "text": "Buy Baclofen 25mg online - Where to Buy Lioresal Free Delivery https://t.co/ar52gUEw5m #medical #blog #health"
        },
        {
            "author_id": "317796197",
            "created_at": "2016-01-09T01:18:35.000Z",
            "id": "685631722281693184",
            "lang": "es",
            "text": "RT @RafaRyes: #ServicioP\u00fablico ni\u00f1a con tetano Maracay Urgente medicamento BACROFENO o LIORESAL 04169467608 04124442846  @Elangeologo @gilb\u2026"
        },
        {
            "author_id": "123777126",
            "created_at": "2016-01-08T21:19:22.000Z",
            "id": "685571521511841792",
            "lang": "es",
            "text": "@trafficLARA alguien q tenga Urgente  lioresal o baclofeno...urgente!!!."
        },
        {
            "author_id": "151296071",
            "created_at": "2016-01-08T20:25:33.000Z",
            "id": "685557976971800577",
            "lang": "es",
            "text": "@FundacionBADAN @lisdelvalle25 tendran lioresal"
        },
        {
            "author_id": "2647139192",
            "created_at": "2016-01-07T17:54:07.000Z",
            "id": "685157479265615875",
            "lang": "en",
            "text": "sext: i carelessly strengthen my wrists while you carelessly take 40-80 mg of baclofen (lioresal) every day"
        },
        {
            "author_id": "1180496797",
            "created_at": "2016-01-07T03:31:51.000Z",
            "id": "684940483999576065",
            "lang": "es",
            "text": "Esta ni\u00f1a solicita con urgencia: Lioresal o Baclofeno por favor comuniquese al 04144603470 04169467608 o 04124452846 por favor."
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-06T08:13:33.000Z",
            "id": "684648987190800384",
            "lang": "en",
            "text": "Baclofen 10mg order no rx. Can I Purchase Lioresal  Online https://t.co/oSa1CO0Ouy #medical #blog #health"
        },
        {
            "author_id": "1276371930",
            "created_at": "2016-01-05T19:55:03.000Z",
            "id": "684463137651843073",
            "lang": "es",
            "text": "@LocatelVzla_ATC  necedito con urgencia lioresal o baclofeno   o su componente activo de 25 mg, gracias"
        },
        {
            "author_id": "188023841",
            "created_at": "2016-01-04T11:46:46.000Z",
            "id": "683977871526854656",
            "lang": "es",
            "text": "@noticierovv  @novartis @TelevenTV  urgente lioresal (baclofeno) 10mg su ayuda por favor mas de 2 meses buscando 04269923024"
        },
        {
            "author_id": "2180907432",
            "created_at": "2016-01-04T11:45:48.000Z",
            "id": "683977627326115840",
            "lang": "en",
            "text": "Baclofen 25mg buy online. How to Order Lioresal  Online https://t.co/7vLJsx4q2M #medical #blog #health"
        },
        {
            "author_id": "188023841",
            "created_at": "2016-01-04T11:39:21.000Z",
            "id": "683976001542578177",
            "lang": "es",
            "text": "@Maby80 @danicabello11 @vwinstonv urgente lioresal (baclofeno) 10 mg 04269923024 mas de 2 meses busc\u00e1ndolo"
        },
        {
            "author_id": "188023841",
            "created_at": "2016-01-04T11:38:03.000Z",
            "id": "683975675984887809",
            "lang": "es",
            "text": "@ConElMazoDando @NicolasMaduro @ConCiliaFlores urgente lioresal (baclofeno) 10mg su ayuda por favor mas de 2 meses buscando 04269923024"
        }
    ],
    "meta": {
        "newest_id": "693517931225939970",
        "oldest_id": "683975675984887809",
        "result_count": 109
    }
}{
    "meta": {
        "result_count": 0
    }
}
~~~
