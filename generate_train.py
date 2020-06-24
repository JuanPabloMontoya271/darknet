import os

image_files = []
train_files = []
test_files = []
os.chdir(os.path.join("data", "obj"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/obj/" + filename)
os.chdir("..")
train_files = image_files[:int(len(image_files)*.7)]
test_files = image_files[:int(len(image_files)*.7)]
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
# with open("test.txt", "w") as outfile:
#     for image in test_files:
#         outfile.write(image)
#         outfile.write("\n")
#     outfile.close()    
os.chdir("..")
