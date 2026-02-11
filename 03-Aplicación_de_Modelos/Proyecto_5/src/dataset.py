import os
import re
from typing import List, Tuple, Optional
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from utils import constants

CLASS_ORDER = ["glass", "paper", "cardboard", "plastic", "metal", "trash"]

def _prefix_from_filename(fname: str) -> str:
    m = re.match(r"^[A-Za-z]+", fname)
    return m.group(0).lower() if m else ""

def image_path(root: str, fname: str) -> str:
    folder = _prefix_from_filename(fname)
    return os.path.join(root, folder, fname)

def parse_index_file(path: str) -> List[Tuple[str, int]]:
    entries: List[Tuple[str, int]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            fname = parts[0]
            label = int(parts[1]) - 1
            entries.append((fname, label))
    return entries

def get_transforms() -> Tuple[transforms.Compose, transforms.Compose]:
    size = (constants.DIM1, constants.DIM2)
    train_t = transforms.Compose([
        transforms.Resize(size),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(0.1, 0.1, 0.1, 0.05),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    val_t = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return train_t, val_t

class WasteDataset(Dataset):
    def __init__(self, root: str, index_file: str, transform: Optional[transforms.Compose] = None):
        self.root = root
        self.items = parse_index_file(index_file)
        self.transform = transform

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, idx: int):
        fname, label = self.items[idx]
        path = image_path(self.root, fname)
        img = Image.open(path).convert("RGB")
        if self.transform:
            img = self.transform(img)
        return img, label

def create_dataloaders(dataset_root: str, docs_dir: str, batch_size: int = 32, num_workers: int = 0):
    train_t, val_t = get_transforms()
    train_idx = os.path.join(docs_dir, "one-indexed-files-notrash_train.txt")
    val_idx = os.path.join(docs_dir, "one-indexed-files-notrash_val.txt")
    test_idx = os.path.join(docs_dir, "one-indexed-files-notrash_test.txt")
    train_ds = WasteDataset(dataset_root, train_idx, transform=train_t)
    val_ds = WasteDataset(dataset_root, val_idx, transform=val_t)
    test_ds = WasteDataset(dataset_root, test_idx, transform=val_t)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    return train_loader, val_loader, test_loader
