import twitter

# Crie um aplicativo no twitter https://developer.twitter.com/en/apps
# Após o cadastro da aplicação acesse a aba Keys and Tokens e obtenha as chaves
#   - Consumer Key
#   - Consumer Secret
#   - Access Token 
#   - Access Token Secret

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

api = twitter.Api(consumer_key=consumer_key,
  consumer_secret=consumer_secret,
  access_token_key=access_token,
  access_token_secret=access_token_secret)

for twitte in api.GetHomeTimeline():
  print(twitte.text)

