import os
import cv2
from tqdm import tqdm

CATEGORY = ["Fire", "NoFire"]


def resize_training_set():
    dataset = "Dataset"
    if not os.path.exists("training_dataset"):
        os.makedirs("training_dataset")
        os.makedirs("training_dataset/Fire")
        os.makedirs("training_dataset/NoFire")
    for category in CATEGORY:
        path = os.path.join(dataset, category)
        print('READING DATASET :' + category + '\n')
        for img in tqdm(os.listdir(path)):
            try:
                image = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                if image.shape[2] == 3:
                    resized_image = cv2.resize(image, (64, 64))
                    cv2.imwrite("training_dataset/" + category + "/" + img, resized_image)
            except Exception as e:
                pass


def resize_test_set():
    dataset = "Test_Dataset"
    if not os.path.exists("testing_dataset"):
        os.makedirs("testing_dataset")
        os.makedirs("testing_dataset/Fire")
        os.makedirs("testing_dataset/NoFire")
    for category in CATEGORY:
        path = os.path.join(dataset, category)
        print('READING DATASET :' + category + '\n')
        for img in tqdm(os.listdir(path)):
            try:
                image = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                if image.shape[2] == 3:
                    resized_image = cv2.resize(image, (64, 64))
                    cv2.imwrite("testing_dataset/" + category + "/" + img, resized_image)
            except Exception as e:
                pass


def blur_dataset():
    dataset = "training_dataset"
    print("BLURRING: " + dataset)
    for category in tqdm(CATEGORY):
        path = os.path.join(dataset, category)
        for img in os.listdir(path):
            try:
                image = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                blur_image = cv2.blur(image, (5, 5))
                cv2.imwrite(path + "/blur_" + img, blur_image)
            except Exception as e:
                pass


def symmetry():
    dataset = "training_dataset"
    print("REVERSE: " + dataset)
    for category in tqdm(CATEGORY):
        path = os.path.join(dataset, category)
        for img in os.listdir(path):
            try:
                image = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                fliped_image = cv2.flip(image, 1)
                cv2.imwrite(path + "/flip_" + img, fliped_image)
            except Exception as e:
                pass


def augment_data():
    blur_dataset()
    symmetry()
