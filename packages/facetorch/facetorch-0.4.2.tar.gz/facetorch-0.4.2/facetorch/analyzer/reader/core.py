import copy
import torch
import torchvision
from codetiming import Timer
from facetorch.base import BaseReader
from facetorch.datastruct import ImageData
from facetorch.logger import LoggerJsonFile

logger = LoggerJsonFile().logger


class ImageReader(BaseReader):
    def __init__(
        self,
        transform: torchvision.transforms.Compose,
        device: torch.device,
        optimize_transform: bool,
    ):
        """ImageReader is a wrapper around a functionality for reading images by Torchvision.

        Args:
            transform (torchvision.transforms.Compose): Transform compose object to be applied to the image, if fix_image_size is True.
            device (torch.device): Torch device cpu or cuda object.
            optimize_transform (bool): Whether to optimize the transforms that are: resizing the image to a fixed size.

        """
        super().__init__(
            transform,
            device,
            optimize_transform,
        )

    @Timer("ImageReader.run", "{name}: {milliseconds:.2f} ms", logger=logger.debug)
    def run(self, path_image: str, fix_img_size: bool = False) -> ImageData:
        """Reads an image from a path and returns a tensor of the image with values between 0-255 and shape (batch, channels, height, width). The order of color channels is RGB. PyTorch and Torchvision are used to read the image.

        Args:
            path_image (str): Path to the image.
            fix_img_size (bool): Whether to resize the image to a fixed size. If False, the size_portrait and size_landscape are ignored. Default is False.

        Returns:
            ImageData: ImageData object with image tensor and pil Image.
        """
        data = ImageData(path_input=path_image)
        data.img = torchvision.io.read_image(
            data.path_input, mode=torchvision.io.ImageReadMode.RGB
        )
        data.img = data.img.unsqueeze(0)
        data.img = data.img.to(self.device)

        if fix_img_size:
            data.img = self.transform(data.img)

        data.tensor = data.img.type(torch.float32)
        data.img = data.img.squeeze(0).cpu()
        data.set_dims()

        return data


class TensorReader(BaseReader):
    def __init__(
        self,
        transform: torchvision.transforms.Compose,
        device: torch.device,
        optimize_transform: bool,
    ):
        """TensorReader is a wrapper around a functionality for reading tensors by Torchvision.

        Args:
            transform (torchvision.transforms.Compose): Transform compose object to be applied to the image, if fix_image_size is True.
            device (torch.device): Torch device cpu or cuda object.
            optimize_transform (bool): Whether to optimize the transforms that are: resizing the image to a fixed size.

        """
        super().__init__(
            transform,
            device,
            optimize_transform,
        )

    @Timer("TensorReader.run", "{name}: {milliseconds:.2f} ms", logger=logger.debug)
    def run(self, tensor: torch.Tensor, fix_img_size: bool = False) -> ImageData:
        """Reads a tensor and returns a tensor of the image with values between 0-255 and shape (batch, channels, height, width). The order of color channels is RGB. PyTorch and Torchvision are used to read the image.

        Args:
            tensor (torch.Tensor): Tensor of a single image with RGB values between 0-255 and shape (channels, height, width).
            fix_img_size (bool): Whether to resize the image to a fixed size. If False, the size_portrait and size_landscape are ignored. Default is False.

        Returns:
            ImageData: ImageData object with image tensor and pil Image.
        """
        data = ImageData(path_input=None)
        data.tensor = copy.deepcopy(tensor)
        data.tensor = tensor.unsqueeze(0)
        data.tensor = data.tensor.to(self.device)

        if fix_img_size:
            data.tensor = self.transform(data.tensor)

        data.img = data.tensor.squeeze(0).cpu()
        data.tensor = data.tensor.type(torch.float32)
        data.set_dims()

        return data
