from bs4 import BeautifulSoup
import requests
import json
class Reciepe:

    def __init__(self):
        self.url = ''
    
    def soup_value(self):
        
        source=requests.get(self.url).text
        soup= BeautifulSoup(source,"html.parser")
        return soup


    def recipe_scrpper(self):
        self.url = 'https://www.yummly.com/recipes?q=pork+dumpling&taste-pref-appended=true'
        text_finder = self.soup_value()
        parent = text_finder.find('div',{'class':'recipe-card'})
        child = parent.find('a',{'class':'link-overlay'})
        new_child = 'https://www.yummly.com'+child['href']
        return new_child
    
    def info_scrapper(self):
        new_url = self.recipe_scrpper()
        self.url = new_url
        text_finder = self.soup_value()
        new_info = text_finder.find_all('script',type='application/ld+json')
       
        # basic_info = text_finder.find('script',type='application/ld+json').string
        return new_info
        # data = json.loads(new_info)
        # # print(data)
        # return data

    def recepe_info(self):
        recep_text = self.info_scrapper()
        data = json.loads(recep_text[1].string)
        new_data = data['itemListElement'][2]
        recipeIngredient = new_data['recipeIngredient']
        receipe_steps=[]
        recipeInstructions = new_data['recipeInstructions']
        for i in range(len(recipeInstructions)):
            step = 'Step'+str(i+1)
            arr =[step,recipeInstructions[i]['text']]
            receipe_steps.append(arr)
        print(receipe_steps,recipeIngredient)
    
    def nutrients_info(self):
        recep_text = self.info_scrapper()
        data = json.loads(recep_text[0].string)
        new_data = data
        ingredients = new_data['recipeIngredient']
        nutrions = new_data['nutrition']
        calories = nutrions['calories']
        carbohydrate = nutrions['carbohydrateContent']
        cholesterol = nutrions['cholesterolContent']
        fat = nutrions['fatContent']
        fiber = nutrions['fiberContent']
        protein = nutrions['proteinContent']
        sugar = nutrions['sugarContent']
        print(calories,carbohydrate,cholesterol,fat,fiber,protein,sugar,ingredients)


       

enc = Reciepe().nutrients_info()