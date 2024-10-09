from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Union
import csv

app = FastAPI()

# CSV 파일 경로
CSV_FILE_PATH = "data.csv"


# CSV 데이터를 읽는 함수
data = []
with open(CSV_FILE_PATH, mode="r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # print(row)
        data.append(
            {
                "year": int(row["연도"]),
                "company": row["기업명"],
                "energy_usage": float(row["에너지사용량"]),
                "ghg_emission": float(row["온실가스배출량"]),
                "water_intake": float(row["용수취수량"]),
                "waste_generation": float(row["폐기물발생량"]),
            }
        )
        # break

# print(data)


# """
# Pydantic model to validate the input data
class ESGData(BaseModel):
    year: int
    company: str
    energy_usage: Union[float, None] = None
    ghg_emission: Union[float, None] = None
    water_intake: Union[float, None] = None
    waste_generation: Union[float, None] = None


# 1. Get all data
@app.get("/data", response_model=List[ESGData])
def get_all_data():
    return data


# 2. Get data by company
@app.get("/data/company/{company_name}", response_model=List[ESGData])
def get_data_by_company(company_name: str):
    company_data = [entry for entry in data if entry["company"] == company_name]
    if not company_data:
        raise HTTPException(status_code=404, detail="Company not found")
    return company_data


# 2. 각 회사의 연도별 평균을 조회할 수 있는 API
@app.get("/data/company/{company_name}/average", response_model=Dict)
def get_company_yearly_average(company_name: str):
    company_data = [entry for entry in data if entry["company"] == company_name]
    if not company_data:
        raise HTTPException(
            status_code=404, detail=f"No data found for company {company_name}"
        )

    averages = {}
    total_years = len(company_data)
    for feature in ["energy_usage", "ghg_emission", "water_intake", "waste_generation"]:
        averages[feature] = sum(entry[feature] for entry in company_data) / total_years
    return averages


# 3. Get data by year
@app.get("/data/year/{year}", response_model=List[ESGData])
def get_data_by_year(year: int):
    year_data = [entry for entry in data if entry["year"] == year]
    if not year_data:
        raise HTTPException(status_code=404, detail="Data not found for the given year")
    return year_data


# 5. 피쳐명으로 데이터를 조회할 수 있는 API
@app.get(
    "/data/feature/{feature_name}",
    response_model=List[Dict[str, Union[int, str, float]]],
)
def get_data_by_feature(feature_name: str):
    valid_features = [
        "energy_usage",
        "ghg_emission",
        "water_intake",
        "waste_generation",
    ]
    if feature_name not in valid_features:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid feature name. Choose from {valid_features}",
        )
    feature_data = [
        {
            "year": entry["year"],
            "company": entry["company"],
            feature_name: entry[feature_name],
        }
        for entry in data
    ]
    return feature_data


# 4. Get data by year and company
@app.get("/data/by_year/{year}/{company_name}", response_model=ESGData)
def get_data_by_year_and_company(year: int, company_name: str):
    for entry in data:
        if entry["year"] == year and entry["company"] == company_name:
            return entry
    raise HTTPException(
        status_code=404, detail="Data not found for the given year and company"
    )


# 3. 모든 회사의 연도별 평균을 볼 수 있는 API
@app.get("/data/yearly_average", response_model=Dict)
def get_all_company_yearly_average():
    yearly_averages = {}
    years = set(entry["year"] for entry in data)

    for year in years:
        year_data = [entry for entry in data if entry["year"] == year]
        averages = {}
        for feature in [
            "energy_usage",
            "ghg_emission",
            "water_intake",
            "waste_generation",
        ]:
            averages[feature] = sum(entry[feature] for entry in year_data) / len(
                year_data
            )
        yearly_averages[year] = averages

    return yearly_averages


# 4. 모든 회사의 연도별 평균을 피쳐별로 조회할 수 있는 API
@app.get("/data/yearly_average/{feature_name}", response_model=Dict)
def get_yearly_average_by_feature(feature_name: str):
    valid_features = [
        "energy_usage",
        "ghg_emission",
        "water_intake",
        "waste_generation",
    ]
    if feature_name not in valid_features:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid feature name. Choose from {valid_features}",
        )

    yearly_averages = {}
    years = set(entry["year"] for entry in data)

    for year in years:
        year_data = [entry for entry in data if entry["year"] == year]
        yearly_averages[year] = sum(entry[feature_name] for entry in year_data) / len(
            year_data
        )

    return yearly_averages


# 5. 피쳐별 최댓값이 포함된 데이터 반환 API
@app.get("/data/max/{feature_name}", response_model=Dict)
def get_max_value_by_feature(feature_name: str):
    valid_features = [
        "energy_usage",
        "ghg_emission",
        "water_intake",
        "waste_generation",
    ]
    if feature_name not in valid_features:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid feature name. Choose from {valid_features}",
        )

    max_value = max(data, key=lambda x: x[feature_name])
    return max_value


# 6. 피쳐별 최소값이 포함된 데이터 반환 API
@app.get("/data/min/{feature_name}", response_model=Dict)
def get_min_value_by_feature(feature_name: str):
    valid_features = [
        "energy_usage",
        "ghg_emission",
        "water_intake",
        "waste_generation",
    ]
    if feature_name not in valid_features:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid feature name. Choose from {valid_features}",
        )

    min_value = min(data, key=lambda x: x[feature_name])
    return min_value


# """
