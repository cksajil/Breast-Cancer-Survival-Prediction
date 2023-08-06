import requests
import pandas as pd
from utils.general import load_config


def main():
    config = load_config("config.yaml")

    # Base URL of the CBioPortal API
    base_url = config["base_url"]

    # Endpoint to get the list of studies
    studies_endpoint = "studies"

    # Make a GET request to retrieve the list of studies
    response = requests.get(base_url + studies_endpoint)

    if response.status_code == 200:
        studies = response.json()

        metabric_study_id = None
        for study in studies:
            if study["studyId"] == "brca_metabric":
                metabric_study_id = study["studyId"]
                break

        if metabric_study_id:
            # Endpoint for getting clinical data of the METABRIC study
            clinical_endpoint = f"studies/{metabric_study_id}/clinical-data"

            # Make a GET request to retrieve clinical data
            clinical_response = requests.get(base_url + clinical_endpoint)

            if clinical_response.status_code == 200:
                metabric_clinical_data = clinical_response.json()
                print(metabric_clinical_data)
                # data.to_csv("metabric_clinical.csv")
            else:
                print("Error retrieving METABRIC clinical data.")
        else:
            print("METABRIC study not found.")
    else:
        print("Error retrieving list of studies.")


if __name__ == "__main__":
    main()
