# Exercise 3 - Fast food
# @author: Ramin Aryaei
#-----------------------------------------------------------------
   #gheymat ha
pizza      = 50000
sandevich  = 35000
sibzamini  = 30000
nooshidani = 5000
#-----------------------------------------------------------------
num_pizza      = int(input('Chand ta pizza? '))
num_sandevich  = int(input('Chand ta sandevich? '))
num_sibzamini  = int(input('Chand ta sibzamini? '))
num_nooshidani = int(input('Chand ta nooshidani? '))
#-----------------------------------------------------------------
   #jame sefaresh ha Bedoone maliat
num_pizza      *= pizza        #gheymat har pizza
num_sandevich  *= sandevich    #gheymat har sandevich
num_sibzamini  *= sibzamini    #gheymat har sibzamini
num_nooshidani *= nooshidani   #gheymat har nooshidani

price = num_pizza + num_sandevich + num_sibzamini + num_nooshidani
#-----------------------------------------------------------------
   #arzeshe_afzoode
arzeshe_afzoode = price // 10
#-----------------------------------------------------------------
   #jam sefaresh ha + arzeshe_afzoode
finalPrice = price + arzeshe_afzoode
#-----------------------------------------------------------------
print(f'\n    Please pay {finalPrice} Toman.')