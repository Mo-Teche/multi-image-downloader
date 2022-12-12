from requests import get

with open('c:/Users/hp/Desktop/python_practice/Day_22/ima_list.txt','r+') as file:
    read_img_url = file.readlines()

i=0
for img_url in read_img_url:
    img_without_n = img_url.strip('\n')
    res = get(img_without_n)
    with open(f'c:/Users/hp/Desktop/python_practice/Day_22/all_images/{i}img.jpg','wb') as download_img:
        download_img.write(res.content)
        i+=1
        # print(img_without_n)
