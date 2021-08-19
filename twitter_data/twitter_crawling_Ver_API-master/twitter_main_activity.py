import twitter_set_drugs
import twitter_crawling_Ver_API

drug_brand = twitter_set_drugs.Drugs()
main_crawling = twitter_crawling_Ver_API.Crawling()

for i in range(0, len(drug_brand.columns)):
    # params : vaccine_name, vaccine_name, start_date, end_date
    main_crawling.main_act_indi(drug_brand.brandname_lists[i], drug_brand.columns[i], "2021-07-01T00:00:00Z", "2021-07-02T00:00:00Z")
   
