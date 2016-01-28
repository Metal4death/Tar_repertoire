import os

def clone_repository(ma_list):
    i = 0;
    user = input("entrez le propriétaire des répertoires\n")
    while (ma_list[i]):
        clone = "git clone git@git.epitech.eu:/" + user + "/"
        clone = clone + ma_list[i]
        i = i + 1
        os.system(clone);
    return

def tar_repository(ma_list):
    tar = "tar -cf repository.tar"
    i = 0;
    while (ma_list[i]):
        tar = tar + " "
        tar = tar + ma_list[i]
        i = i + 1
    os.system(tar);
    return

def delete_repository(ma_list):
    i = 0;
    while (ma_list[i]):
        rm = "rm -rf "
        rm = rm + ma_list[i]
        os.system(rm);
        i = i + 1
    return

os.system("blih repository list > test.txt")
mon_fichier = open("test.txt", "r")
contenu = mon_fichier.read()
ma_list = contenu.split("\n")
mon_fichier.close()
clone_repository(ma_list)
tar_repository(ma_list)
delete_repository(ma_list)
os.system("rm test.txt");
