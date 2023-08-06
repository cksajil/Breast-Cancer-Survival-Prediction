import requests
from utils.general import load_config, json_to_df, create_folder
from os import path


def main():
    config = load_config("config.yaml")

    # Base URL of the CBioPortal API
    base_url = config["base_url"]
    data_path = config["data_directory"]
    clinical_data_file = config["clinical_data"]

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
                clinical_df = json_to_df(metabric_clinical_data)
                create_folder(data_path)
                clinical_df.to_csv(path.join(data_path, clinical_data_file))
            else:
                print("Error retrieving METABRIC clinical data.")
        else:
            print("METABRIC study not found.")
    else:
        print("Error retrieving list of studies.")


if __name__ == "__main__":
    main()
