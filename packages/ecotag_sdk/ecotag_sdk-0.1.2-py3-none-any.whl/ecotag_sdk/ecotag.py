import os
from dataclasses import dataclass
from pathlib import Path

import aiohttp
from aiohttp import FormData
from requests_oauth2client import OAuth2Client


@dataclass
class ApiInformation:
    api_url: str
    access_token: str

@dataclass
class Dataset:
    dataset_name: str
    dataset_type: str
    team_name: str
    directory: str
    classification: str = "Public"
    
@dataclass
class Label:
    name: str
    color: str
    id: str


@dataclass
class Project:
    project_name: str
    dataset_name: str
    team_name: str
    numberCrossAnnotation: int = 1
    annotationType: str = "ImageClassifier"
    labels: list[Label] = None


async def create_dataset(dataset: Dataset, api_information: ApiInformation):
    dataset_name = dataset.dataset_name
    dataset_type = dataset.dataset_type
    team_name = dataset.team_name
    directory = dataset.directory
    classification = dataset.classification

    jwt_token = api_information.access_token
    api_url = api_information.api_url

    headers = {"Authorization": f"Bearer {jwt_token}"}

    # Initialize a session.
    async with aiohttp.ClientSession() as session:
        # Fetch the teams and extract the team ID.
        team_id = await get_team_id(api_url, headers, session, team_name)

        # Create the dataset.
        payload = {
            "name": dataset_name,
            "type": dataset_type,
            "groupId": team_id,
            "classification": classification,
        }

        async with session.post(
            f"{api_url}/Datasets", headers=headers, json=payload
        ) as response:
            print(f"Create dataset status: {response.status}")
            await response.text()

        dataset_id = await get_dataset_id(api_url, dataset_name, headers, session)
        if(dataset_id is None):
            raise Exception(f"Dataset {dataset_name} not found")

        # Upload image files in the directory.
        print("start uploading files")
        for filename in os.listdir(directory):
            print(f"Uploading file: {filename}")
            if filename.endswith(".jpg") or filename.endswith(".png"):
                data = FormData()
                data.add_field(
                    "files",
                    open(Path(directory) / filename, "rb"),
                    filename=filename,
                    content_type="application/octet-stream",
                )

                async with session.post(
                    f"{api_url}/Datasets/{dataset_id}/files", headers=headers, data=data
                ) as response:
                    print(f"upload file status: {response.status} [{filename}]")
                    print(await response.text())

        # Lock the dataset.
        async with session.post(
            f"{api_url}/Datasets/{dataset_id}/lock", headers=headers
        ) as response:
            print(f"Lock dataset status: {response.status}")
            print(await response.text())


async def get_team_id(api_url, headers, session, team_name):
    team_id = None
    async with session.get(f"{api_url}/Groups", headers=headers) as response:
        print(f"Get teams status: {response.status}")
        teams = await response.json()
        for team in teams:
            if team["name"] == team_name:
                team_id = team["id"]
                break
        if team_id is None:
            raise Exception(f"Team {team_name} not found")
        print(f"Team ID: {team_id}")
    return team_id


async def get_dataset_id(api_url, dataset_name, headers, session):
    # Get Dataset ID.
    async with session.get(f"{api_url}/Datasets", headers=headers) as response:
        datasets = await response.json()
        for dataset in datasets:
            if dataset["name"] == dataset_name:
                dataset_id = dataset["id"]
                print(f"Dataset ID: {dataset_id}")
                return dataset_id
    return None

async def get_dataset(api_information: ApiInformation, dataset_name: str):
    jwt_token = api_information.access_token
    api_url = api_information.api_url
    headers = {"Authorization": f"Bearer {jwt_token}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{api_url}/Datasets", headers=headers) as response:
            datasets = await response.json()
            for dataset in datasets:
                if dataset["name"] == dataset_name:
                    return dataset
            return None

async def create_project(project: Project, api_information: ApiInformation):
    project_name = project.project_name
    dataset_name = project.dataset_name
    team_name = project.team_name

    jwt_token = api_information.access_token
    api_url = api_information.api_url

    headers = {"Authorization": f"Bearer {jwt_token}"}

    async with aiohttp.ClientSession() as session:
        dataset_id = await get_dataset_id(api_url, dataset_name, headers, session)
        if(dataset_id is None):
            raise Exception(f"Dataset {dataset_name} not found")
        team_id = await get_team_id(api_url, headers, session, team_name)

        # Create Image Classification Project.
        payload = {
            "name": project_name,
            "datasetId": dataset_id,
            "groupId": team_id,
            "numberCrossAnnotation": 1,
            "annotationType": "ImageClassifier",
            "labels": [],
        }

        for label in project.labels:
            payload["labels"].append(label.__dict__)

        async with session.post(
            f"{api_url}/Projects", headers=headers, json=payload
        ) as response:
            print(f"Create project status: {response.status}")
            print(await response.text())


async def get_project_id(api_url, project_name, headers, session):
    async with session.get(f"{api_url}/projects", headers=headers) as response:
        if response.status > 400:
            print("Error: ", response.code, response.reason)
            return None
        projects = await response.json()
        for project in projects:
            if project["name"] == project_name:
                project_id = project["id"]
                break
        if project_id is None:
            raise Exception(f"Project {project_name} not found")
        print(f"project ID: {project_id}")
    return project_id


async def get_project(api_information: ApiInformation, project_name: str):
    jwt_token = api_information.access_token
    api_url = api_information.api_url
    headers = {"Authorization": f"Bearer {jwt_token}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{api_url}/projects", headers=headers) as response:
            if response.status > 400:
                print("Error: ", response.code, response.reason)
                return None
            projects = await response.json()
            for project in projects:
                if project["name"] == project_name:
                    return project
        return None

async def download_annotations(
    api_information: ApiInformation,
    project_name: str,
    output_directory: str,
    filename: str,
):
    jwt_token = api_information.access_token
    api_url = api_information.api_url
    headers = {"Authorization": f"Bearer {jwt_token}"}

    async with aiohttp.ClientSession() as session:
        project_id = await get_project_id(api_url, project_name, headers, session)

        async with session.get(
            f"{api_url}/projects/{project_id}/export", headers=headers
        ) as response:
            if response.status == 200:
                content = await response.read()
                output_path = Path(output_directory) / filename
                with open(output_path, "wb") as file:
                    file.write(content)
                print(f"Fichier téléchargé et enregistré : {str(output_path)}")
            else:
                print("Erreur lors du téléchargement du fichier :", response.status)

def get_access_token(token_endpoint: str, client_id: str, client_secret: str):
    oauth2client = OAuth2Client(
        token_endpoint=token_endpoint,
        auth=(client_id, client_secret),
    )
    token = oauth2client.client_credentials(scope="api")
    jwt_token = token.access_token
    return jwt_token
