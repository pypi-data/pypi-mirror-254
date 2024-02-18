import os
import SimpleITK as sitk
import nibabel as nib
from typing import Tuple
import numpy as np
import pydicom
from datetime import datetime


def resample_volume(volume_path: str,
                    new_spacing: list,
                    out_path: str,
                    interpolator: int = sitk.sitkLinear) -> Tuple[sitk.Image, nib.Nifti1Image, np.ndarray]:
    """This function resamples the input volume to a specified voxel spacing
    Args:
        volume_path (str): input volume path
        new_spacing (list): desired voxel spacing that we want
        out_path (str): path where we temporarily save the resampled output volume
        interpolator (int): interpolator that we want to use (e.g. 1= NearNeigh., 2=linear, ...)
    Returns:
        resampled_volume_sitk_obj: resampled volume as sitk object
        resampled_volume_nii_obj: resampled volume as nib object
        resampled_volume_nii: resampled volume as numpy array
    """
    volume = sitk.ReadImage(volume_path)  # read volume
    original_size = volume.GetSize()  # extract size
    original_spacing = volume.GetSpacing()  # extract spacing
    new_size = [int(round(osz * ospc / nspc)) for osz, ospc, nspc in zip(original_size, original_spacing, new_spacing)]
    resampled_volume_sitk_obj = sitk.Resample(volume, new_size, sitk.Transform(), interpolator,
                                              volume.GetOrigin(), new_spacing, volume.GetDirection(), 0,
                                              volume.GetPixelID())
    sitk.WriteImage(resampled_volume_sitk_obj, out_path)  # write sitk volume object to disk
    resampled_volume_nii_obj = nib.load(out_path)  # type: nib.Nifti1Image # load volume as nibabel object
    resampled_volume_nii = np.asanyarray(resampled_volume_nii_obj.dataobj)  # type: np.ndarray # convert from nibabel object to np.array
    os.remove(out_path)  # remove volume from disk to save space

    return resampled_volume_sitk_obj, resampled_volume_nii_obj, resampled_volume_nii


def remove_zeros_ijk_from_volume(input_volume: np.ndarray) -> np.ndarray:
    """This function removes all the rows, columns and slices of the input volume that only contain zero values.
    Args:
        input_volume: volume from which we want to remove zeros
    Returns:
        cropped_volume: cropped volume (i.e. input volume with zeros removed)
    """

    def remove_zeros_one_coordinate(input_volume_: np.ndarray, range_spatial_dim: int, spatial_dim: int):
        idxs_nonzero_slices = []  # will the contain the indexes of all the slices that have nonzero values
        for idx in range(range_spatial_dim):  # loop over coordinate
            if spatial_dim == 0:
                one_slice = input_volume_[idx, :, :]
            elif spatial_dim == 1:
                one_slice = input_volume_[:, idx, :]
            elif spatial_dim == 2:
                one_slice = input_volume_[:, :, idx]
            else:
                raise ValueError(f"spatial_dim can only be 0, 1, or 2. Got {spatial_dim} instead")

            if np.count_nonzero(one_slice) > 0:  # if the slice has some nonzero values
                idxs_nonzero_slices.append(idx)  # save slice index

        # retain only indexes with nonzero values from the two input volumes
        if spatial_dim == 0:
            cropped_volume_ = input_volume_[idxs_nonzero_slices, :, :]
        elif spatial_dim == 1:
            cropped_volume_ = input_volume_[:, idxs_nonzero_slices, :]
        elif spatial_dim == 2:
            cropped_volume_ = input_volume_[:, :, idxs_nonzero_slices]
        else:
            raise ValueError(f"spatial_dim can only be 0, 1, or 2. Got {spatial_dim} instead")

        return cropped_volume_

    assert len(input_volume.shape) == 3, "The input volume must be 3D"

    # i coordinate
    cropped_volume = remove_zeros_one_coordinate(input_volume, input_volume.shape[0], spatial_dim=0)
    # j coordinate
    cropped_volume = remove_zeros_one_coordinate(cropped_volume, input_volume.shape[1], spatial_dim=1)
    # k coordinate
    cropped_volume = remove_zeros_one_coordinate(cropped_volume, input_volume.shape[2], spatial_dim=2)

    return cropped_volume


def get_axes_orientations_with_nibabel(input_nifti_volume: nib.Nifti1Image) -> tuple:
    """This function returns the axes orientations as a tuple
    Args:
        input_nifti_volume: the input volume for which we want the axes orientations
    Returns:
        orientations: the axes orientations
    """
    aff_mat = input_nifti_volume.affine  # type: np.ndarray # extract affine matrix
    orientations = nib.aff2axcodes(aff_mat)

    return orientations


def get_nibabel_header(input_nifti_volume: nib.Nifti1Image,
                       print_header: bool = False) -> nib.nifti1.Nifti1Header:
    """This function returns the header of the nifti image/volume
    Args:
        input_nifti_volume: the input volume for which we want the header
        print_header: whether to print the header or not; defaults to False
    Returns:
        header (nib.nifti1.Nifti1Header): the axes orientations
    """
    header = input_nifti_volume.header
    if print_header:
        print(header)

    return header


def read_dcm_series(dcm_dir: str) -> sitk.Image:
    """This function reads a dicom series with SimpleITK
    Args:
        dcm_dir: directory where dicom files are stored
    Returns:
        volume_sitk: volume loaded as sitk.Image
    """
    reader = sitk.ImageSeriesReader()  # create reader
    dicom_names = reader.GetGDCMSeriesFileNames(dcm_dir)  # read dicom series
    reader.SetFileNames(dicom_names)

    volume_sitk = reader.Execute()  # extract sitk.Image

    return volume_sitk


def get_sitk_volume_info(path_to_nii_or_dcm: str,
                         print_info: bool = False) -> dict:
    """This function prints basic info of the input volume
    Args:
        path_to_nii_or_dcm: path to volume that we want to explore
        print_info: whether to print the volume info or no; defaults to False
    Returns:
        volume_info: it contains all the main volume information
    """
    if os.path.isdir(path_to_nii_or_dcm):  # if path_to_nii_or_dcm is a directory
        volume_sitk = read_dcm_series(path_to_nii_or_dcm)
    else:  # if instead path_to_nii_or_dcm is a file
        volume_sitk = sitk.ReadImage(path_to_nii_or_dcm)  # read as sitk Image

    volume_info = {"dimensions": volume_sitk.GetDimension(),
                   "size": volume_sitk.GetSize(),
                   "origin": volume_sitk.GetOrigin(),
                   "spacing": volume_sitk.GetSpacing(),
                   "direction": volume_sitk.GetDirection(),
                   "nb_components_per_pixel": volume_sitk.GetNumberOfComponentsPerPixel(),
                   "pixel_type": volume_sitk.GetPixelID(),
                   "pixel_id_type_as_string": volume_sitk.GetPixelIDTypeAsString(),
                   "pixel_id_value": volume_sitk.GetPixelIDValue()
                   }

    if print_info:
        print(f"Dimensions: {volume_sitk.GetDimension()}")
        print(f"Size: {volume_sitk.GetSize()}")
        print(f"Origin: {volume_sitk.GetOrigin()}")
        print(f"Spacing: {volume_sitk.GetSpacing()}")
        print(f"Direction cosine matrix: {volume_sitk.GetDirection()}")
        print(f"Nb. components per pixel {volume_sitk.GetNumberOfComponentsPerPixel()}")
        print(f"Pixel type: {volume_sitk.GetPixelID()}")
        print(f"Pixel ID type as string: {volume_sitk.GetPixelIDTypeAsString()}")
        print(f"Pixel ID value: {volume_sitk.GetPixelIDValue()}")

    return volume_info


def re_orient_to_nib_closest_canonical(path_to_nii_volume: str,
                                       sub: str,
                                       ses: str,
                                       volume_name: str,
                                       orig_anat_dir: str) -> None:
    """This function re-orients the input volume to the nibabel closest canonical orientation (i.e. RAS+)
    Args:
        path_to_nii_volume: path to volume that we want to re-oriented
        sub: subject of interest
        ses: session of interest
        volume_name: name of volume to re-orient
        orig_anat_dir: path to directory containing original TOF volume
    """
    # load mask volume
    nii_obj = nib.load(path_to_nii_volume)  # load as nibabel object
    nii_obj = nib.as_closest_canonical(nii_obj)  # re-orient to nibabel canonical axis orientation

    # load original volume; we use it to enforce the same affine matrix for the re-oriented mask
    original_volume_path = os.path.join(orig_anat_dir, f"{sub}_{ses}_{volume_name}.nii.gz")
    original_volume_obj = nib.load(original_volume_path)  # load as nibabel object

    # save re-oriented mask to disk, OVERWRITING the previous one
    nib.Nifti1Image(nii_obj.dataobj, original_volume_obj.affine, nii_obj.header).to_filename(path_to_nii_volume)


def change_dcm_tags_one_derived_image(ds: pydicom.dataset.FileDataset,
                                      series_date: str,
                                      invented_manufacturer: str,
                                      invented_model_name: str,
                                      series_time: str,
                                      new_series_name: str,
                                      new_protocol_name: str,
                                      original_study_instance_uid: pydicom.uid.UID) -> pydicom.dataset.FileDataset:
    """This function changes some dicom tags for the derived volume (following https://gdcm.sourceforge.net/wiki/index.php/Writing_DICOM but not only).
    Args:
        ds: pydicom object that contains the dicom tags
        series_date: today's date (used as series' date)
        invented_manufacturer: invented manufacturer name
        invented_model_name: invented model name
        series_time: generated time of series
        new_series_name: name of new generated series
        new_protocol_name: name of new generated protocol
        original_study_instance_uid: study instance UID of the study; all series should have the same
    Returns:
        ds: same pydicom object, but with some modified tags
    """
    # below, we report all the dcm tags that will be changed

    # 1) Media Storage SOP Instance UID (0002, 0003), it's a tag in the file meta information
    generated_media_storage_sop_instance_uid = pydicom.uid.generate_uid()  # generate UID
    ds.file_meta.MediaStorageSOPInstanceUID = generated_media_storage_sop_instance_uid

    # 2) Image Type (0008, 0008) was already modified within MeVisLab

    # 3) Instance creation date (0008, 0012)
    if "InstanceCreationDate" in ds:
        ds.InstanceCreationDate = series_date

    # 4) Instance creation time (0008, 0013)
    if "InstanceCreationTime" in ds:
        time_now = datetime.today().strftime('%H%M%S.%f')  # save time now
        ds.InstanceCreationTime = time_now

    # 5) SOP Instance UID (0008, 0018)
    if "SOPInstanceUID" in ds:
        generated_sop_instance_uid = pydicom.uid.generate_uid()  # generate UID
        ds.SOPInstanceUID = generated_sop_instance_uid

    # 6) Acquisition Time (0008, 0032); generate a unique time for each dcm image
    if "AcquisitionTime" in ds:
        time_now = datetime.today().strftime('%H%M%S.%f')  # save time now
        ds.AcquisitionTime = time_now

    # 7) Series Time (0008, 0031); this needs to be the same for all dcm images in the series, so we define it outside of the function
    if "SeriesTime" in ds:
        ds.SeriesTime = series_time

    # 8) Content Time (0008, 0032); this needs to be different for each dcm image
    if "ContentTime" in ds:
        time_now = datetime.today().strftime('%H%M%S.%f')  # save time now
        ds.ContentTime = time_now

    # 9) Manufacturer (0008, 0070)
    if "Manufacturer" in ds:
        ds.Manufacturer = invented_manufacturer

    # 10) Series Description (0008, 103E) was already modified within MeVisLab

    # 11) Manufacturer's model name (0008, 1090)
    if "ManufacturerModelName" in ds:
        ds.ManufacturerModelName = invented_model_name

    # 12) Referenced Image Sequence (0008, 1140)
    ref_img_seq = ds.ReferencedImageSequence
    for idx, _ in enumerate(ref_img_seq):
        if "ReferencedSOPInstanceUID" in ref_img_seq[idx]:
            new_uid = pydicom.uid.generate_uid()  # generate UID
            ref_img_seq[idx].ReferencedSOPInstanceUID = new_uid

    # 13) Derivation description (0008, 2111)
    ds.add_new(0x00082111, 'ST', 'Segmentation_Neuroinformatics_Paper')

    # 14) Source image sequence (0008, 2112): don't know what to put and how to generate a valid SQ tag
    # ds.add_new(0x00082112, 'SQ', '')

    # 15) Sequence Name (0018, 0024)
    if "SequenceName" in ds:
        ds.SequenceName = new_series_name

    # 16) Protocol Name (0018, 1030)
    if "ProtocolName" in ds:
        ds.ProtocolName = new_protocol_name

    # 17) Study Instance UID (0020, 000D): this should be identical to the one of the original series cause the study is the same
    if ds.StudyInstanceUID != original_study_instance_uid:  # if it's different
        ds.StudyInstanceUID = original_study_instance_uid  # change it

    # 18) Series Instance UID (0020, 000E) was already modified in MeVisLab

    # 19) Series Number (0020, 0011) was already modified in MeVisLab

    # 20) Image Comments (0020, 4000) was already modified in MeVisLab

    # 21) Pixel Data (7FE0, 0010) was already modified in MeVisLab

    return ds


def dcm2nii_sitk(in_dcm_dir: str,
                 out_nii_dir: str,
                 out_name: str) -> bool:
    """This function converts a DICOM sequence to a NIfTI file using SimpleITK.
    Args:
        in_dcm_dir: input directory containing the DICOM sequence
        out_nii_dir: output directory where the NIfTI file will be saved
        out_name: name of the NIfTI file
    Returns:
        conversion_ok: whether the conversion was successful or not
    """
    # initialize conversion_ok to False; if the conversion is successful, it will be set to True
    conversion_ok = False

    # Load DICOM sequence
    reader = sitk.ImageSeriesReader()  # type: sitk.ImageSeriesReader # create reader
    dicom_names = reader.GetGDCMSeriesFileNames(in_dcm_dir)  # type: list # get dicom names
    reader.SetFileNames(dicom_names)  # set dicom names to reader
    image = reader.Execute()  # type: sitk.Image # execute reader to get sitk image

    # Convert to NIfTI format
    img_array = sitk.GetArrayFromImage(image)  # type: np.ndarray  # convert to numpy array
    image_nifti = sitk.GetImageFromArray(img_array)  # type: sitk.Image  # convert to sitk image
    image_nifti.SetSpacing(image.GetSpacing())  # set spacing as in original dicom
    if len(image.GetDirection()) == len(image_nifti.GetDirection()):
        image_nifti.SetDirection(image.GetDirection())  # set direction as in original dicom
        image_nifti.SetOrigin(image.GetOrigin())  # set origin as in original dicom

        # Save NIfTI file
        sitk.WriteImage(image_nifti, os.path.join(out_nii_dir, f"{out_name}.nii.gz"))  # save nifti file

        conversion_ok = True

    return conversion_ok


def bias_field_correction_sitk(input_img_path: str,
                               output_path: str) -> None:
    """This function applies bias field correction to the input image using SimpleITK.
    Args:
        input_img_path: path to input image
        output_path: path where the output image will be saved
    """
    input_img = sitk.ReadImage(input_img_path)  # read image
    mask_img = sitk.OtsuThreshold(input_img, 0, 1, 200)  # create binary mask with Otsu method
    input_img = sitk.Cast(input_img, sitk.sitkFloat32)  # cast to float32
    corrector = sitk.N4BiasFieldCorrectionImageFilter()  # create corrector object
    output = corrector.Execute(input_img, mask_img)  # apply corrector to obtain output image
    sitk.WriteImage(output, output_path)  # save output image to output_path


def extract_filename_from_nifti_path(in_nifti_path: str) -> str:
    """This function extracts the filename of a nifti file from its path, regardless
    of the extension which can be either .nii or .nii.gz
    Args:
        in_nifti_path: path to nifti file
    Returns:
        filename: filename of nifti file
    """
    filename = os.path.splitext(os.path.splitext(os.path.basename(in_nifti_path))[0])[0]

    return filename

