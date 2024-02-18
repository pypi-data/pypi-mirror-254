"""
This script checks the Nexon's MapleStory game API for updates and performs necessary updates.
Nexon의 메이플스토리 게임 API를 확인하여 업데이트가 필요한 항목을 찾고, 필요한 업데이트를 수행합니다.

The script operates in the following order:
스크립트는 다음과 같은 순서로 작동합니다:

1. Retrieves the current version information of the API.
   API의 현재 버전 정보를 가져옵니다.
2. Compares it with the API information stored locally to check if an update is needed.
   로컬에 저장된 API 정보와 비교하여 업데이트가 필요한지 확인합니다.
3. If an update is needed, it downloads the new API information and updates the local API information.
   업데이트가 필요한 경우, 새로운 API 정보를 다운로드하고 로컬의 API 정보를 업데이트합니다.
4. Outputs the updated files.
   업데이트된 파일들을 출력합니다.
"""

from __future__ import annotations

import json
import urllib.parse
from datetime import datetime
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel, RootModel, field_validator
from rich import print

API_VERSION_URL = "https://openapi.nexon.com/game/maplestory/?id=22"


def decode_url(url):
    """Decodes the given URL."""
    try:
        return urllib.parse.unquote(url)
    except Exception as e:
        print(f"Error decoding URL: {e}")
        return None


def add_api_information_to_file(filepath: Path, api_info: APIInformation):
    """
    Adds 'x-fileName', 'x-updateDate', and 'x-fileUrl' to a YAML file just before the 'servers:' section.

    Args:
        filepath (Path): The path to the YAML file.
        api_info (APIInformation): An instance of APIInformation containing fileName, updateDate, and fileUrl.

    Raises:
        ValueError: If the 'servers:' section is not found in the YAML file.
    """
    with open(filepath, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    try:
        index = lines.index("servers:\n")
    except ValueError as e:
        raise ValueError(
            "The 'servers:' section was not found in the YAML file."
        ) from e

    insert_lines = [
        f"  x-fileName: {api_info.fileName}\n",
        f"  x-updateDate: '{api_info.updateDate}'\n",
        f"  x-fileUrl: '{api_info.fileUrl}'\n",
    ]
    output_lines = [*lines[:index], *insert_lines, *lines[index:]]

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(output_lines)


class APIInformation(BaseModel):
    id: int
    gameId: str
    categoryName: str
    filePath: str
    fileName: str
    fileUrl: str
    ordering: int
    createEmpNo: int
    createEmpName: str
    updateEmpNo: int
    updateEmpName: str
    createDate: datetime
    updateDate: datetime
    isVisible: bool

    @field_validator("createEmpName")
    def decode_name(cls, v):
        """Decodes the name."""
        return decode_url(v)

    def download(self, directory: Path) -> Path:
        """Downloads the API information to the given directory."""
        r = httpx.get(self.fileUrl)
        filename = f"{self.id}_{self.categoryName.replace(' ', '_')}.yaml"
        open(directory / filename, "wb").write(r.content)
        add_api_information_to_file(directory / filename, self)
        return directory / filename


class APIResultList(RootModel):
    """Represents a list of API results."""

    root: list[APIInformation]

    def __iter__(self):
        return iter(self.root)

    @property
    def latest_update_date(self):
        """Returns the latest update date among the API results."""
        return max(api.updateDate for api in self.root)

    def download(self, directory: Path) -> list[Path]:
        """Downloads all API results to the given directory."""
        filepaths = []
        for api in self:
            filepath = api.download(directory)
            filepaths.append(filepath)
        return filepaths


def retrieve_api_result() -> dict:
    """
    Fetches and returns the API result from the specified URL.

    Returns:
        dict: Parsed API result.
    """
    try:
        response = httpx.get(API_VERSION_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, "lxml")
        script = soup.select_one("#__NEXT_DATA__")
        script_data = json.loads(script.string)
        return script_data["props"]["pageProps"]["apiResult"]
    except Exception as e:
        raise Exception(f"Failed to fetch API result: {str(e)}")


if __name__ == "__main__":
    PROJECT_DIRECTORY = Path(__file__).parent.parent
    DATA_DIRECTORY = PROJECT_DIRECTORY / "data"
    yaml_files = list(DATA_DIRECTORY.glob("*.yaml"))
    openapi_file = DATA_DIRECTORY / "openapi.json"

    local_api_info = json.load(open(openapi_file, "r"))
    print("Local API Information")
    print(local_api_info)

    api_result = retrieve_api_result()
    print("Web API Information")
    print(api_result)
    web_api_info = APIResultList.model_validate(api_result)

    print(f"Local API Version == Web API Version: {local_api_info == api_result}")
    if local_api_info != api_result:
        print("Update Required")
        # Update openapi.json
        open(openapi_file, "w").write(
            json.dumps(api_result, indent=4, ensure_ascii=False)
        )

        # Download updated yaml files
        print("Downloading updated yaml files...")
        new_yaml_files = web_api_info.download(DATA_DIRECTORY)

        # Print updated files
        print("Updated files:")
        updated_files = [*yaml_files, *new_yaml_files, openapi_file]
        updated_files = [
            str(file.relative_to(PROJECT_DIRECTORY)) for file in sorted(updated_files)
        ]
        print(updated_files)

        open("updated_files.txt", "w").write("\n".join(updated_files))
