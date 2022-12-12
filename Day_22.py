import requests

            # pixaby to text images 

# api_url = 'https://pixabay.com/api/?key=31981145-dfcf3fe72dcf0896657f5c709&q=blue+flowers&per_page=150'
# res = requests.get(api_url)
# data_sjon = res.json()
# hits = data_sjon.get('hits')
# for hit in hits :
#     images = hit.get('webformatURL')
#     file = open('c:/Users/hp/Desktop/python_practice/Day_22/ima_list.txt','a+')
#     file.writelines(images+'\n')
#     file.close()
#     # print(images)

# print(hits[0])

day22 = open('c:/Users/hp/Desktop/python_practice/Day_22/ima_list.txt','r+')
images = day22.readlines()
day22.close()
image_list = []
for img in images:
    single_image = img.strip('\n')
    image_list.append(single_image)
    # print(single_image)

# print(image_list[0])
res = requests.get(image_list[149])
with open('c:/Users/hp/Desktop/python_practice/Day_22/img1.jpg','wb') as file:
    file.write(res.content)