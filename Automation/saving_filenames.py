""" Automation """

with open("C://users/cathx/repos/argoverse-api/argo_train/train.txt", "w") as f:
    for p, d, files in os.walk('C://users/cathx/repos/argoverse-api/argo_train/image_2/'):
        for file in files:
            f.write(str(file[:-4]) + '\n')
