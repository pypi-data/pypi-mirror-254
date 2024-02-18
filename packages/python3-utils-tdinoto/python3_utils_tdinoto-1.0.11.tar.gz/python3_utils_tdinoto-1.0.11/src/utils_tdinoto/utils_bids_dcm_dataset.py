import os
import pydicom
from collections import Counter
import numpy as np
from utils_tdinoto.utils_strings import keep_only_digits
import SimpleITK as sitk
import pandas as pd
from tqdm import tqdm
from utils_tdinoto.numeric import round_half_up


def print_patient_sex_and_age(bids_dir: str,
                              bids_dcm_dir: str) -> None:
    """This function loops over a pseudo-BIDS dataset dir and prints the patient sex
    Args:
        bids_dir: directory containing the BIDS dataset
        bids_dcm_dir: directory containing the dcm series of the dataset. A pseudo-BIDS organization is expected. Specifically:
            sub-000
                |__ses-yyyymm01
                      |__dcm_series_1
                      |__dcm_series_2
                |__ses-yyyymm02
                      |__dcm_series_1
                      |__dcm_series_2
    """
    all_sex = []
    all_ages = []
    for sub in sorted(os.listdir(bids_dir)):
        if "sub" in sub and os.path.isdir(os.path.join(bids_dir, sub)):
            if len(os.listdir(os.path.join(bids_dir, sub))) >= 1:  # if there is at least one ses
                first_ses = os.listdir(os.path.join(bids_dir, sub))[0]
                if os.path.exists(os.path.join(bids_dcm_dir, sub, first_ses)):
                    if len(os.listdir(os.path.join(bids_dcm_dir, sub, first_ses))) >= 1:  # if there is at least one series
                        first_dcm_series = os.listdir(os.path.join(bids_dcm_dir, sub, first_ses))[0]
                        if len(os.listdir(os.path.join(bids_dcm_dir, sub, first_ses, first_dcm_series))) >= 1:  # if there is at least one dcm image
                            first_dcm_img = os.listdir(os.path.join(bids_dcm_dir, sub, first_ses, first_dcm_series))[0]
                            first_dcm_img_tags = pydicom.dcmread(os.path.join(bids_dcm_dir, sub, first_ses, first_dcm_series, first_dcm_img))
                            sex = first_dcm_img_tags.PatientSex
                            age = first_dcm_img_tags.PatientAge
                            all_sex.append(sex)
                            all_ages.append(age)
                else:
                    print(f"{sub}_{first_ses} missing")
    print(f"\n{len(all_sex)} subjects found")
    occurrence_count_sex = Counter(all_sex)
    print(f"\nSex: {occurrence_count_sex}")
    all_ages_only_numbers = [int(keep_only_digits(x)) for x in all_ages]
    mean_age, std_age = np.mean(all_ages_only_numbers), np.std(all_ages_only_numbers)
    print(f"\nAge: mean={mean_age}, std={std_age}")


def print_median_values(df: pd.DataFrame,
                        scanner_name: str) -> None:
    median_tr = df['TR'].median()
    median_te = df['TE'].median()
    median_spacing_x = df['spacing_x'].median()
    median_spacing_y = df['spacing_y'].median()
    median_spacing_z = df['spacing_z'].median()

    print(f"\nmedian values {scanner_name}: TR = {round_half_up(median_tr)}, TE = {round_half_up(median_te)}, spacing = {median_spacing_x} x {median_spacing_y} x {median_spacing_z}")


def find_mr_acquisition_params(bids_ds: str,
                               dcm_dir: str) -> None:
    cnt_subs = 0
    vendor_scanner_field_strength = []
    for sub in sorted(os.listdir(bids_ds)):
        if "sub" in sub and os.path.isdir(os.path.join(bids_ds, sub)):
            sub_dir_dmc_dir = os.path.join(dcm_dir, sub)
            if os.path.isdir(sub_dir_dmc_dir):
                cnt_subs += 1
                # if cnt_subs % 100 == 0:
                #     print(f"{cnt_subs}) {sub}:")
                for ses in sorted(os.listdir(sub_dir_dmc_dir)):
                    assert os.path.isdir(os.path.join(sub_dir_dmc_dir, ses))
                    # print(f"    {ses}")
                    for series in sorted(os.listdir(os.path.join(sub_dir_dmc_dir, ses))):
                        assert os.path.isdir(os.path.join(sub_dir_dmc_dir, ses, series))
                        cnt_images = 0
                        img_position_patient = []
                        for dcm_img in sorted(os.listdir(os.path.join(sub_dir_dmc_dir, ses, series))):
                            cnt_images += 1
                            one_dcm_img = pydicom.dcmread(os.path.join(sub_dir_dmc_dir, ses, series, dcm_img))
                            manufacturer = one_dcm_img.Manufacturer
                            model = one_dcm_img.ManufacturerModelName
                            field_strength = one_dcm_img.MagneticFieldStrength
                            tr = one_dcm_img.RepetitionTime
                            te = one_dcm_img.EchoTime

                            sitk_img = sitk.ReadImage(os.path.join(sub_dir_dmc_dir, ses, series, dcm_img))
                            voxel_spacing = sitk_img.GetSpacing()
                            spacing_x = round(voxel_spacing[0], 2)
                            spacing_y = round(voxel_spacing[1], 2)
                            spacing_z = round(voxel_spacing[2], 2)

                            vendor_scanner_field_strength.append([manufacturer, model, field_strength, tr, te, spacing_x, spacing_y, spacing_z])
                            break  # we only loop through one image
                        break  # we only loop through one series
            else:
                print(f"{sub} missing")

    df_vendor_scanner_field_strength = pd.DataFrame(vendor_scanner_field_strength, columns=['vendor', 'scanner', 'field_strength', 'TR', 'TE', 'spacing_x', 'spacing_y', 'spacing_z'])

    # re-adjust weird values
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.field_strength < 1.5, 'field_strength'] = 1.5
    df_vendor_scanner_field_strength.loc[(df_vendor_scanner_field_strength.field_strength < 3.0) & (df_vendor_scanner_field_strength.field_strength > 2.8), 'field_strength'] = 3.0
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.scanner == 'Trio', 'scanner'] = 'TrioTim'
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.scanner == 'Skyra_fit', 'scanner'] = 'Skyra'
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.scanner == 'Prisma_fit', 'scanner'] = 'Prisma'
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.scanner == 'SymphonyVision', 'scanner'] = 'Symphony'
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.scanner == 'GENESIS_SIGNA', 'scanner'] = 'Signa'
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.scanner == 'Signa HDxt', 'scanner'] = 'Signa'
    df_vendor_scanner_field_strength.loc[df_vendor_scanner_field_strength.field_strength == 15000, 'field_strength'] = 1.5

    # sort dataframe
    df_vendor_scanner_field_strength_sorted = df_vendor_scanner_field_strength.sort_values(["vendor", "scanner"], ignore_index=True)  # ignore_index=True re-starts the indexes from 0

    print()
    print(df_vendor_scanner_field_strength_sorted.value_counts(["vendor", "scanner"]))

    df_intera = df_vendor_scanner_field_strength_sorted.loc[df_vendor_scanner_field_strength_sorted["scanner"] == "Intera"]
    df_skyra = df_vendor_scanner_field_strength_sorted.loc[df_vendor_scanner_field_strength_sorted["scanner"] == "Skyra"]
    df_symphony = df_vendor_scanner_field_strength_sorted.loc[df_vendor_scanner_field_strength_sorted["scanner"] == "Symphony"]
    df_triotim = df_vendor_scanner_field_strength_sorted.loc[df_vendor_scanner_field_strength_sorted["scanner"] == "TrioTim"]
    df_verio = df_vendor_scanner_field_strength_sorted.loc[df_vendor_scanner_field_strength_sorted["scanner"] == "Verio"]
    df_aera = df_vendor_scanner_field_strength_sorted.loc[df_vendor_scanner_field_strength_sorted["scanner"] == "Aera"]
    df_prisma = df_vendor_scanner_field_strength_sorted.loc[df_vendor_scanner_field_strength_sorted["scanner"] == "Prisma"]

    if not df_intera.empty:
        print_median_values(df_intera, scanner_name="Intera")
    if not df_skyra.empty:
        print_median_values(df_skyra, scanner_name="Skyra")
    if not df_symphony.empty:
        print_median_values(df_symphony, scanner_name="Symphony")
    if not df_triotim.empty:
        print_median_values(df_triotim, scanner_name="TrioTim")
    if not df_verio.empty:
        print_median_values(df_verio, scanner_name="Verio")
    if not df_aera.empty:
        print_median_values(df_aera, scanner_name="Aera")
    if not df_prisma.empty:
        print_median_values(df_prisma, scanner_name="Prisma")


def print_distribution_sessions_bids_dataset(path_bids_ds: str) -> None:
    all_sub_ses = []
    for sub in tqdm(sorted(os.listdir(path_bids_ds))):
        if "sub" in sub and os.path.isdir(os.path.join(path_bids_ds, sub)):
            cnt_ses = 0
            for ses in sorted(os.listdir(os.path.join(path_bids_ds, sub))):
                if "ses" in ses and os.path.isdir(os.path.join(path_bids_ds, sub, ses)):
                    cnt_ses += 1
            all_sub_ses.append([sub, cnt_ses])

    df_all_sub_ses = pd.DataFrame(all_sub_ses, columns=['sub', 'ses'])

    # extract the different counts for the number of sessions
    ses_counts = df_all_sub_ses['ses'].value_counts()

    # print the distribution
    print()
    for nb_ses, count in ses_counts.items():
        print(f"Subjects with {nb_ses} ses: {count}")


def convert_age_str2int(age_str: str) -> int:
    """This function converts the age from string to int. It is used when for instance
    the PatientAge dicom attribute is in the format "075Y"
    Example:
        age_str = "075Y"
        age_int = convert_age_str2int(age_str)
        print(age_int)  # prints "75
    Args:
        age_str: age in string format
    Returns:
        age_int: age in int format if age_str is a string; otherwise, age_int is equal to age_str and a warning is printed
    """
    # check that age is a string
    if isinstance(age_str, str):
        age_int = int(keep_only_digits(age_str))
    else:
        age_int = age_str
        print("\nWARNING: age is not a string; leave value unchanged")

    return age_int


def main():
    # input args
    path_bids_ds = "/path/to/BIDS_Dataset/"
    # path_bids_ds = r"Z:\Database\ADNI_Controls_FDA_AI_Letter_BIDS"
    # print_distribution_sessions_bids_dataset(path_bids_ds)


if __name__ == '__main__':
    main()
