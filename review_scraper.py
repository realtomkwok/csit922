import csv
from datetime import datetime
from google_play_scraper import Sort, reviews


# Retrieve data from Play Store using Scraper
def review_scraper(app_id, app_name, lang, country, sort, count, filter_score_with):
    result, continuation_token = reviews(
        app_id,
        lang=lang,  # defaults to 'en'
        country=country,  # defaults to 'us'
        sort=sort,  # defaults to Sort.NEWEST
        count=count,  # defaults to 100
        filter_score_with=filter_score_with  # defaults to None(means all score)
    )

    # Export data to the CSV file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    csv_file_name = f'./data/{app_name}-reviews_{timestamp}.csv'

    field_names = ['reviewId', 'userName', 'userImage', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion',
                   'at', 'replyContent', 'repliedAt', 'appVersion']

    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)

        writer.writeheader()

        for row in result:
            writer.writerow(row)


review_scraper(
    app_id='com.twitter.android',
    app_name='twitter',
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=30000,
    filter_score_with=None
)

review_scraper(
    app_id='com.instagram.barcelona',
    app_name='threads',
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=30000,
    filter_score_with=None
)

# review_scraper(
#     app_id='org.joinmastodon.android',
#     app_name='mastodon',
#     lang='en',
#     country='us',
#     sort=Sort.NEWEST,
#     count=10000,
#     filter_score_with=None
# )
