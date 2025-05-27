import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
USER_DB = os.getenv("USER_DB")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DB_NAME")

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
KAGGLE_URL = os.getenv("KAGGLE_URL")
DOWNLOAD_URL = os.getenv("DOWNLOAD_URL")


columns_and_types = (
    f"Заголовки таблицы и их типы - "
    "column_name       |     data_type"
    "-------------------+-------------------"
    "marketing_spend   | integer"
    "freelancer_id     | integer"
    "hourly_rate       | double precision"
    "job_success_rate  | double precision"
    "client_rating     | double precision"
    "job_duration_days | integer"
    "rehire_rate       | double precision"
    "job_completed     | integer"
    "earnings_usd      | integer"
    "job_category      | character varying"
    "platform          | character varying"
    "experience_level  | character varying"
    "client_region     | character varying"
    "payment_method    | character varying"
    "project_type      | character varying"
    "Примеры заполнения таблицы "
    "freelancer_id, job_category, platform, experience_level, client_region, payment_method, job_completed, earnings_usd, hourly_rate, job_success_rate, client_rating, job_duration_days, project_type, rehire_rate, marketing_spend"
    "1,Web Development,Fiverr,Beginner,Asia,Mobile Banking,180,1620,95.79,68.73,3.18,1,Fixed,40.19,53"
    "2,App Development,Fiverr,Beginner,Australia,Mobile Banking,218,9078,86.38,97.54,3.44,54,Fixed,36.53,486"
    "3,Web Development,Fiverr,Beginner,UK,Crypto,27,3455,85.17,86.6,4.2,46,Hourly,74.05,489"
    "4,Data Entry,PeoplePerHour,Intermediate,Asia,Bank Transfer,17,5577,14.37,79.93,4.47,41,Hourly,27.58,67"
    "5,Digital Marketing,Upwork,Expert,Asia,Crypto,245,5898,99.37,57.8,5.0,41,Hourly,69.09,489"
    "6,Customer Support,Toptal,Beginner,Europe,Crypto,280,6867,43.04,57.8,4.87,8,Fixed,43.88,290"
    "7,Web Development,Fiverr,Beginner,USA,Crypto,96,1677,20.5,52.9,4.29,32,Hourly,45.99,343"
    "8,Data Entry,Toptal,Beginner,Australia,Bank Transfer,112,6193,82.15,93.31,3.84,30,Fixed,31.59,168"
    "9,Content Writing,Toptal,Intermediate,USA,Crypto,233,8446,26.44,80.06,4.27,46,Fixed,50.11,396"
    "10,Data Entry,PeoplePerHour,Beginner,Middle East,Mobile Banking,156,6608,54.99,85.4,4.57,52,Hourly,32.76,160"
    "11,App Development,Fiverr,Beginner,Australia,Crypto,112,5322,17.16,51.03,3.24,89,Fixed,12.75,14"
    "12,Customer Support,Toptal,Intermediate,Australia,Mobile Banking,293,7931,50.09,98.5,3.82,61,Fixed,29.04,190"
    "13,Customer Support,Fiverr,Intermediate,Europe,Mobile Banking,180,9033,58.02,91.62,4.68,13,Fixed,10.45,14"
    "14,Data Entry,Freelancer,Beginner,Canada,Bank Transfer,290,3797,47.36,60.62,3.77,89,Hourly,78.48,286"
    "15,App Development,Freelancer,Beginner,UK,Crypto,245,9347,11.6,59.09,4.14,40,Hourly,77.6,362"
    "16,Data Entry,Freelancer,Intermediate,UK,Bank Transfer,149,9332,51.07,59.17,4.18,61,Hourly,37.66,411"
    "17,Customer Support,Toptal,Expert,UK,Mobile Banking,18,1657,49.55,65.21,3.37,44,Hourly,60.99,9"
    "18,Customer Support,Freelancer,Intermediate,Middle East,PayPal,279,5124,29.85,76.24,3.72,62,Hourly,34.21,56"
    "19,Graphic Design,PeoplePerHour,Expert,Asia,Crypto,75,7203,92.55,71.6,3.67,44,Hourly,56.98,198"
    "20,Data Entry,PeoplePerHour,Beginner,Canada,Bank Transfer,199,6783,44.69,64.56,3.05,48,Hourly,66.38,160"
    "21,SEO,Toptal,Beginner,USA,PayPal,15,116,87.09,80.59,3.05,74,Hourly,76.27,262"
    "22,Data Entry,Fiverr,Expert,UK,Crypto,110,8050,15.42,56.97,4.66,59,Fixed,38.01,388"
    "23,Customer Support,Upwork,Intermediate,USA,Crypto,262,7695,35.29,64.61,3.55,57,Hourly,64.83,473"
    "24,Graphic Design,Fiverr,Beginner,Canada,Bank Transfer,200,9520,21.75,68.32,4.04,11,Fixed,28.61,380"
    "25,Graphic Design,Fiverr,Expert,Middle East,PayPal,149,4208,43.8,72.8,3.6,25,Fixed,79.32,252"
    "26,Content Writing,Fiverr,Intermediate,Canada,Bank Transfer,224,9055,15.61,89.26,4.88,61,Hourly,11.8,118"
    "27,App Development,Fiverr,Expert,Europe,Crypto,178,452,46.9,59.98,3.52,46,Fixed,52.25,79"
    "28,Digital Marketing,Upwork,Intermediate,Asia,Crypto,220,7975,38.62,75.71,3.86,54,Fixed,56.17,123"
    "29,Web Development,Freelancer,Intermediate,UK,Mobile Banking,97,4216,26.21,79.62,4.75,34,Hourly,58.16,312"
    "30,Web Development,Fiverr,Intermediate,Middle East,Crypto,264,2975,66.01,52.32,4.68,84,Fixed,18.43,71"
    "..."
)
