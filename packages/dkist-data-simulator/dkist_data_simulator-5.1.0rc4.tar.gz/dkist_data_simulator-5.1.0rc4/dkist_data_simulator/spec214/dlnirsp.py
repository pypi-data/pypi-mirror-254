from random import choice
from typing import Any

import astropy.units as u
import numpy as np
from astropy.wcs import WCS
from dkist_fits_specifications.utils.spec_processors.polarimetric_requiredness import (
    POLARIMETRIC_HEADER_REQUIREMENTS,
)

from .core import Spec214Dataset, Spec214Schema


class BaseDLNIRSPDataset(Spec214Dataset):
    """
    A base class for DL-NIRSP datasets.
    """

    def __init__(
        self,
        n_exposures,
        n_stokes,
        time_delta,
        *,
        linewave,
        array_shape=(100, 100, 100)
    ):
        if not n_exposures:
            raise NotImplementedError(
                "Support for less than 4D DLNIRSP datasets is not implemented."
            )

        array_shape = list(array_shape)

        dataset_shape_rev = list(array_shape) + [n_exposures]
        if n_stokes > 1:
            dataset_shape_rev += [n_stokes]

        # These keys need to be passed to super().__init__ so the file schema is updated with the correct
        # polarimetric requiredness
        polarimetric_keys = self.get_polarimetric_keys(n_stokes)

        super().__init__(
            dataset_shape_rev[::-1],
            array_shape,
            time_delta=time_delta,
            instrument="dlnirsp",
            **polarimetric_keys
        )

        self.add_constant_key("DTYPE1", "SPATIAL")
        self.add_constant_key("DPNAME1", "spatial x")
        self.add_constant_key("DWNAME1", "helioprojective longitude")
        self.add_constant_key("DUNIT1", "arcsec")

        self.add_constant_key("DTYPE2", "SPATIAL")
        self.add_constant_key("DPNAME2", "spatial y")
        self.add_constant_key("DWNAME2", "helioprojective latitude")
        self.add_constant_key("DUNIT2", "arcsec")

        self.add_constant_key("DTYPE3", "SPECTRAL")
        self.add_constant_key("DPNAME3", "wavelength")
        self.add_constant_key("DWNAME3", "wavelength")
        self.add_constant_key("DUNIT3", "nm")

        self.add_constant_key("DTYPE4", "TEMPORAL")
        self.add_constant_key("DPNAME4", "exposure number")
        self.add_constant_key("DWNAME4", "time")
        self.add_constant_key("DUNIT4", "s")

        if n_stokes > 1:
            self.add_constant_key("DTYPE5", "STOKES")
            self.add_constant_key("DPNAME5", "stokes")
            self.add_constant_key("DWNAME5", "stokes")
            self.add_constant_key("DUNIT5", "")
            self.stokes_file_axis = 0

        self.add_constant_key("LINEWAV", linewave.to_value(u.nm))

        for key, value in polarimetric_keys.items():
            self.add_constant_key(key, value)

        # TODO: What is this value??
        self.plate_scale = (
            10 * u.arcsec / u.pix,
            10 * u.arcsec / u.pix,
            1 * u.nm / u.pix,
        )
        self.n_stokes = n_stokes

    def get_polarimetric_keys(self, n_stokes) -> dict[str, Any]:
        """
        Given the number of stokes parameters, update the header to correspond to polarimetric or non-polarimetric data.
        """
        # Just a dummy schema so we can generate values.
        file_schema = Spec214Schema(
            instrument="dlnirsp", naxis=3, dnaxis=4, deaxes=2, daaxes=2, nspeclns=1
        )
        polarimetric_keys = dict()
        for key, polarimetric_choices in POLARIMETRIC_HEADER_REQUIREMENTS[
            "dl-nirsp"
        ].items():
            if n_stokes > 1:
                value = choice(polarimetric_choices)

            else:
                key_schema = file_schema[key]
                value = key_schema.generate_value()
                while value in polarimetric_choices:
                    # Keep trying until we get something non-polarimetric
                    value = key_schema.generate_value()

            polarimetric_keys[key] = value

        return polarimetric_keys


class SimpleDLNIRSPDataset(BaseDLNIRSPDataset):
    """
    A simple five dimensional DLNIRSP dataset with a HPC grid aligned to the pixel axes.
    """

    name = "dlnirsp-simple"

    @property
    def non_temporal_file_axes(self):
        if self.n_stokes > 1:
            # This is the index in file shape so third file dimension
            return (0,)
        return super().non_temporal_file_axes

    @property
    def data(self):
        return np.random.random(self.array_shape)

    @property
    def fits_wcs(self):
        if self.array_ndim != 3:
            raise ValueError(
                "DLNIRSP dataset generator expects a three dimensional FITS WCS."
            )

        w = WCS(naxis=self.array_ndim)
        w.wcs.crpix = (
            self.array_shape[2] / 2,
            self.array_shape[1] / 2,
            self.array_shape[0] / 2,
        )
        w.wcs.crval = 0, 0, 0
        w.wcs.cdelt = [self.plate_scale[i].value for i in range(self.array_ndim)]
        w.wcs.cunit = "arcsec", "arcsec", "nm"
        w.wcs.ctype = "HPLN-TAN", "HPLT-TAN", "AWAV"
        w.wcs.pc = np.identity(self.array_ndim)
        return w
