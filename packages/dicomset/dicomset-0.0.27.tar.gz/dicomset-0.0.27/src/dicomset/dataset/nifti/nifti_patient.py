import nibabel as nib
import numpy as np
import os
import pandas as pd
from typing import List, Literal, Optional, OrderedDict, Tuple

from dicomset.types import ImageSpacing3D, PatientID, PatientRegions, Point3D
from dicomset.utils import arg_to_list

class NIFTIPatient:
    def __init__(
        self,
        dataset: 'NIFTIDataset',
        id: PatientID,
        ct_from: Optional['NIFTIDataset'] = None,
        excluded_labels: Optional[pd.DataFrame] = None):
        self.__dataset = dataset
        self.__ct_from = ct_from
        self.__id = str(id)
        self.__excluded_labels = excluded_labels[excluded_labels['patient-id'] == self.__id] if excluded_labels is not None else None
        self.__global_id = f'{dataset} - {self.__id}'

        # Check that patient ID exists.
        if ct_from is not None:
            self.__ct_path = os.path.join(self.__ct_from.path, 'data', 'ct', f'{self.__id}.nii.gz')
        else:
            self.__ct_path = os.path.join(dataset.path, 'data', 'ct', f'{self.__id}.nii.gz')
        if not os.path.exists(self.__ct_path):
            raise ValueError(f"Patient '{self}' not found. Filepath: '{self.__ct_path}'.")

    @property
    def ct_data(self) -> np.ndarray:
        img = nib.load(self.__ct_path)
        data = img.get_data()
        return data

    @property
    def ct_offset(self) -> Point3D:
        img = nib.load(self.__ct_path)
        affine = img.affine
        offset = (affine[0][3], affine[1][3], affine[2][3])
        return offset

    @property
    def ct_size(self) -> np.ndarray:
        return self.ct_data.shape

    @property
    def ct_spacing(self) -> ImageSpacing3D:
        img = nib.load(self.__ct_path)
        affine = img.affine
        spacing = (abs(affine[0][0]), abs(affine[1][1]), abs(affine[2][2]))
        return spacing
    
    @property
    def description(self) -> str:
        return self.__global_id

    @property
    def dose_data(self) -> np.ndarray:
        filepath = os.path.join(self.__dataset.path, 'data', 'dose', f'{self.__id}.nii.gz')
        if not os.path.exists(filepath):
            raise ValueError(f"Dose data not found for patient '{self}'.")
        img = nib.load(filepath)
        data = img.get_fdata()
        return data

    @property
    def id(self) -> str:
        return self.__id

    @property
    def origin(self) -> Tuple[str, str]:
        df = self.__dataset.anon_index
        row = df[df['anon-id'] == self.__id].iloc[0]
        dataset = row['dicom-dataset']
        pat_id = row['patient-id']
        return (dataset, pat_id)

    @property
    def patient_id(self) -> Optional[str]:
        # Get anon manifest.
        manifest = self.__dataset.anon_manifest
        if manifest is None:
            raise ValueError(f"No anon manifest found for dataset '{self.__dataset}'.")

        # Get patient ID.
        manifest = manifest[manifest['anon-id'] == self.__id]
        if len(manifest) == 0:
            raise ValueError(f"No entry for anon patient '{self.__id}' found in anon manifest for dataset '{self.__dataset}'.")
        pat_id = manifest.iloc[0]['patient-id']

        return pat_id

    @property
    def ct_path(self) -> str:
        return self.__ct_path

    def has_region(
        self,
        region: PatientRegions,
        labels: Literal['included', 'excluded', 'all'] = 'included') -> bool:
        # Return 'True' if patient has at least one of the requested regions.
        regions = arg_to_list(region, str)
        pat_regions = self.list_regions(labels=labels)
        if len(np.intersect1d(regions, pat_regions)) != 0:
            return True
        else:
            return False

    def list_regions(
        self,
        labels: Literal['included', 'excluded', 'all'] = 'included',
        only: Optional[PatientRegions] = None) -> List[str]:
        # Find regions by file names.
        dirpath = os.path.join(self.__dataset.path, 'data', 'regions')
        folders = os.listdir(dirpath)
        regions = []
        for f in folders:
            dirpath = os.path.join(self.__dataset.path, 'data', 'regions', f)
            if f'{self.__id}.nii.gz' in os.listdir(dirpath):
                # Apply exclusion criteria.
                if self.__excluded_labels is not None:
                    df = self.__excluded_labels[(self.__excluded_labels['patient-id'] == self.__id) & (self.__excluded_labels['region'] == f)]
                    if labels == 'included' and len(df) >= 1:
                        continue
                    elif labels == 'excluded' and len(df) == 0:
                        continue
                regions.append(f)

        # Filter on 'only'.
        if only is not None:
            only = arg_to_list(only, str)
            regions = [r for r in regions if r in only]

        # Sort regions.
        regions = list(sorted(regions))

        return regions

    def region_data(
        self,
        labels: Literal['included', 'excluded', 'all'] = 'included',
        region: PatientRegions = 'all') -> OrderedDict:
        regions = arg_to_list(region, str, literals={ 'all': self.list_regions(labels=labels)})

        data = {}
        for region in regions:
            if not self.has_region(region, labels=labels):
                raise ValueError(f"Requested region '{region}' not found for patient '{self.__id}', dataset '{self.__dataset}'.")
            path = os.path.join(self.__dataset.path, 'data', 'regions', region, f'{self.__id}.nii.gz')
            img = nib.load(path)
            rdata = img.get_fdata()
            data[region] = rdata.astype(bool)
        return data

    def __str__(self) -> str:
        return self.__global_id
