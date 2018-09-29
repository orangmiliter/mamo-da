# mamo-da
  mamo'da adalah alat bantu untuk memudahkan kita dalam bersosial media twitter khususnya, mamoda menyediakan fitur sederhana seperti, merespon twitter dari tagar, auto retweet, auto like, auto follow, melihat info user dari #hastag atau keyword tertentu, dan sentimen analisis. 
# Instalasi
# Debian / Ubuntu
  $sudo apt install python-pip  
  $sudo pip install textblob  
  $sudo python -m pip install matplotlib  
  $sudo apt install python-tweepy python-tk 

# Run
  Tambahkan API key anda di file keys.py  
  
keys = dict(  
    consumer_key = 'xxxxxxxxxxxxx',  
    consumer_secret = 'xxxxxxxxxxxxxxxxxxxxx',  
    access_token = 'xxxxxxxxxxx-xxxxxxxxxxxxx',  
    access_token_secret = 'xxxxxxxxxxxxxxxxxx',  
)  

  $python mamoda.py  

# screenshot
![alt text](https://github.com/orangmiliter/mamo-da/blob/master/screenshot/ss.png)
