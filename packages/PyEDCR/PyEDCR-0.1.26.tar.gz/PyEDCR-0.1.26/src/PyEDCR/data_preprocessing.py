import os
import numpy as np
import torch
import torchvision
import pandas as pd
import torch.utils.data
import pathlib
import typing

granularities = ['fine', 'coarse']

true_fine_data = np.load(r'test_fine/test_true_fine.npy')
true_coarse_data = np.load(r'test_coarse/test_true_coarse.npy')

coarse_grain_classes_not_sorted = ['Air Defense', 'BMP', 'BTR', 'Tank', 'Self Propelled Artillery', 'BMD', 'MT_LB']
fine_grain_classes_not_sorted = [
  '30N6E', 'Iskander', 'Pantsir-S1', 'Rs-24', 'BMP-1', 'BMP-2', 'BMP-T15',
  'BRDM', 'BTR-60', 'BTR-70', 'BTR-80',
  'T-14', 'T-62', 'T-64', 'T-72', 'T-80', 'T-90',
  '2S19_MSTA', 'BM-30', 'D-30', 'Tornado', 'TOS-1',
  'BMD', 'MT_LB']

fine_grain_classes = sorted(fine_grain_classes_not_sorted)
coarse_grain_classes = sorted(coarse_grain_classes_not_sorted)

category_dict = {
    'Air Defense': ['30N6E', 'Iskander', 'Pantsir-S1', 'Rs-24'],
    'BMP': ['BMP-1', 'BMP-2', 'BMP-T15'],
    'BTR': ['BRDM', 'BTR-60', 'BTR-70', 'BTR-80'],
    'Tank': ['T-14', 'T-62', 'T-64', 'T-72', 'T-80', 'T-90'],
    'Self Propelled Artillery': ['2S19_MSTA', 'BM-30', 'D-30', 'Tornado', 'TOS-1'],
    'BMD': ['BMD'],
    'MT_LB': ['MT_LB']
}

def get_fine_to_coarse() -> (dict[str, str], dict[int, int]):
    """
    Creates and returns a dictionary with fine-grain labels as keys and their corresponding coarse grain-labels
    as values, and a dictionary with fine-grain label indices as keys and their corresponding coarse-grain label
    indices as values
    """

    fine_to_coarse = {}
    fine_to_coarse_idx = {}

    for fine_grain_class_idx, fine_grain_class in enumerate(fine_grain_classes):
        for coarse_grain_class, fine_grain_class_list in category_dict.items():
            coarse_grain_class_idx = coarse_grain_classes.index(coarse_grain_class)
            if fine_grain_class in fine_grain_class_list:
                fine_to_coarse[fine_grain_class] = coarse_grain_class
                fine_to_coarse_idx[fine_grain_class_idx] = coarse_grain_class_idx
        

    return fine_to_coarse, fine_to_coarse_idx

fine_to_coarse, fine_to_course_idx = get_fine_to_coarse()
coarse_to_fine = {
    'Air Defense': ['30N6E', 'Iskander', 'Pantsir-S1', 'Rs-24'],
    'BMP': ['BMP-1', 'BMP-2', 'BMP-T15'],
    'BTR': ['BRDM', 'BTR-60', 'BTR-70', 'BTR-80'],
    'Tank': ['T-14', 'T-62', 'T-64', 'T-72', 'T-80', 'T-90'],
    'Self Propelled Artillery': ['2S19_MSTA', 'BM-30', 'D-30', 'Tornado', 'TOS-1'],
    'BMD': ['BMD'],
    'MT_LB': ['MT_LB']
}


def get_num_inconsistencies(fine_labels: typing.Union[np.array, torch.Tensor],
                            coarse_labels: typing.Union[np.array, torch.Tensor]) -> int:
    inconsistencies = 0

    if isinstance(fine_labels, torch.Tensor):
        fine_labels = np.array(fine_labels.cpu())
        coarse_labels = np.array(coarse_labels.cpu())

    for fine_prediction, coarse_prediction in zip(fine_labels, coarse_labels):
        if fine_to_course_idx[fine_prediction] != coarse_prediction:
            inconsistencies += 1

    return inconsistencies


def get_dataset_transforms(train_or_test: str) -> torchvision.transforms.Compose:
    """
    Returns the transforms required for the VIT for training or test datasets
    """

    resize_num = 224
    means = stds = [0.5] * 3

    return torchvision.transforms.Compose(
        ([torchvision.transforms.RandomResizedCrop(resize_num),
          torchvision.transforms.RandomHorizontalFlip()] if train_or_test == 'train' else
         [torchvision.transforms.Resize(int(resize_num / 224 * 256)),
          torchvision.transforms.CenterCrop(resize_num)]) +
        [torchvision.transforms.ToTensor(),
         torchvision.transforms.Normalize(means, stds)
         ])


class CombinedImageFolderWithName(torchvision.datasets.ImageFolder):
    """
    Subclass of torchvision.datasets for a combined coarse and fine grain models that returns an image with its filename
    """

    def __getitem__(self,
                    index: int) -> (torch.tensor, int, str):
        """
        Returns one image from the dataset

        Parameters
        ----------

        index: Index of the image in the dataset
        """

        path, y_fine_grain = self.samples[index]

        y_coarse_grain = fine_to_course_idx[y_fine_grain]

        x = self.loader(path)

        if self.transform is not None:
            x = self.transform(x)
        if self.target_transform is not None:
            y_fine_grain = self.target_transform(y_fine_grain)
        name = os.path.basename(path)
        folder_path = os.path.basename(os.path.dirname(path))

        x_identifier = f'{folder_path}/{name}'

        return x, y_fine_grain, x_identifier, y_coarse_grain


class IndividualImageFolderWithName(torchvision.datasets.ImageFolder):
    """
    Subclass of torchvision.datasets for individual coarse or fine grain models that returns an image with its filename
    """

    def __getitem__(self,
                    index: int) -> (torch.tensor, int, str):
        """
        Returns one image from the dataset

        Parameters
        ----------

        index: Index of the image in the dataset
        """

        path, y = self.samples[index]
        x = self.loader(path)

        if self.transform is not None:
            x = self.transform(x)
        if self.target_transform is not None:
            y = self.target_transform(y)

        name = os.path.basename(path)
        folder_path = os.path.basename(os.path.dirname(path))

        x_identifier = f'{folder_path}/{name}'

        return x, y, x_identifier


def get_datasets(cwd: typing.Union[str, pathlib.Path],
                 combined: bool = True) -> \
        (dict[str, typing.Union[CombinedImageFolderWithName, IndividualImageFolderWithName]], int, int):
    """
    Instantiates and returns train and test datasets

    Parameters
    ----------
        cwd: Path to the current working folder
        combined: Whether the model is combining fine and coarse grain or not
    """

    data_dir = pathlib.Path.joinpath(cwd, '.')
    datasets = {f'{train_or_test}': CombinedImageFolderWithName(root=os.path.join(data_dir, f'{train_or_test}_fine'),
                                                                transform=get_dataset_transforms(train_or_test=train_or_test))
                if combined else IndividualImageFolderWithName(root=os.path.join(data_dir, f'{train_or_test}_fine'),
                                                               transform=get_dataset_transforms(train_or_test=train_or_test))
                for train_or_test in ['train', 'test']}

    print(f"Total number of train images: {len(datasets['train'])}\n"
          f"Total number of test images: {len(datasets['test'])}")

    classes = datasets['train'].classes
    assert classes == sorted(classes) == fine_grain_classes

    num_fine_grain_classes = len(classes)
    num_coarse_grain_classes = len(coarse_grain_classes)

    return datasets, num_fine_grain_classes, num_coarse_grain_classes


def get_loaders(datasets: dict[str, typing.Union[CombinedImageFolderWithName, IndividualImageFolderWithName]],
                batch_size: int) -> dict[str, torch.utils.data.DataLoader]:
    """
    Instantiates and returns train and test torch data loaders

    Parameters
    ----------
        datasets: Train and test datasets to use with the loaders
        batch_size
    """

    return {train_or_test: torch.utils.data.DataLoader(
        dataset=datasets[train_or_test],
        batch_size=batch_size,
        shuffle=train_or_test == 'train')
        for train_or_test in ['train', 'test']}
