import subprocess 

#### test 
# return_code = subprocess.call("echo Hello World", shell=True) 
# a = subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()
# print(a)
#####

time = "00:10:43"
pic = "test" + '.jpg'
video = 'How.I.Met.Your.Mother.-.1x02.-.Purple.Giraffe.rmvb'
create_pic = 'ffmpeg -ss ' + time + ' -i ' + video + ' -vframes 1 -q:v 2 ' + pic
upload_imgur = '/Users/wangzhixiang/.nvm/versions/node/v11.2.0/bin/imgur-upload ' + pic 

subprocess.Popen(create_pic, shell=True, stdout=subprocess.PIPE).stdout.read()
link = subprocess.Popen(upload_imgur, shell=True, stdout=subprocess.PIPE).stdout.read()

link = str(link).lstrip("b'").rstrip("\\n'")
print(link)
