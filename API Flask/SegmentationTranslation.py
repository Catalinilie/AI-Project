from Augustus_IA import *
import os


def findPostId():
    files = os.listdir('Augustus_IA')
    id = 1
    for file_ in files:
        if 'AugustusOutputPrelucrat' in file_ and '.json' in file_:
            id += 1
    return id


def segmentation_and_translation(path, id_):
    RunAugustus.runaugustus(path)
    prelucrareAugustusOutputgenerareJSON.prelucrare(id_)

