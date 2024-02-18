import numpy as np
import rasterio
from rasterio import MemoryFile
from rasterio.enums import Resampling


def rescale_dataset(dataset, pixel_size):
    resampling_factor_x = dataset.res[0] / pixel_size
    resampling_factor_y = dataset.res[1] / pixel_size

    new_transform = dataset.transform * rasterio.Affine.scale(
        resampling_factor_x, resampling_factor_y
    )

    new_width = max(int(dataset.width * resampling_factor_x), 1)
    new_height = max(int(dataset.height * resampling_factor_y), 1)

    new_meta = dataset.meta.copy()
    new_meta.update(
        {
            "transform": new_transform,
            "width": new_width,
            "height": new_height,
        }
    )

    rescaled_data = np.empty(
        (dataset.count, new_meta["height"], new_meta["width"]), dtype=dataset.dtypes[0]
    )

    dataset.read(out=rescaled_data, resampling=Resampling.bilinear)

    rescaled_dataset = MemoryFile().open(
        driver="GTiff",
        count=dataset.count,
        dtype=dataset.dtypes[0],
        width=new_meta["width"],
        height=new_meta["height"],
        transform=new_meta["transform"],
        crs=dataset.crs,
    )

    rescaled_dataset.write(rescaled_data)

    return rescaled_dataset
