import pandas as pd
import plotly.graph_objects as go
from fetch import *


def create_data_by_feature_plot(dropdown_value="energy_usage"):
    # print(dropdown_value)
    data = fetch_data_by_feature(dropdown_value)
    # print(data)
    if not data:
        return "No data found."

    # 회사별 데이터 추출
    companies = sorted(list(set([entry["company"] for entry in data])))
    years = sorted(list(set([entry["year"] for entry in data])))

    # Plotly 그래프
    fig = go.Figure()

    # 각 회사별로 데이터 시각화
    for company in companies:
        company_data = [entry for entry in data if entry["company"] == company]
        years = [entry["year"] for entry in company_data]
        feature_values = [entry[dropdown_value] for entry in company_data]

        fig.add_trace(
            go.Scatter(
                x=years,
                y=feature_values,
                mode="lines+markers",
                name=f"{company} {dropdown_value}",
            )
        )

    fig.update_layout(
        title=f"{dropdown_value} 기업별 비교",
        xaxis_title="Year",
        yaxis_title=dropdown_value.capitalize(),
        legend_title="Company",
        font=dict(
            size=14,
            weight="bold",
        ),
        # paper_bgcolor="#43A047",
        xaxis=dict(
            tickmode="linear",
            tick0=min(years),
            dtick=1,
            tickvals=years,
        ),
        # plot_bgcolor="#BFFCC6",
    )

    return fig


def create_company_data_plot(company_name="삼성전자"):
    # print(f"Fetching data for {company_name}")
    company_data = fetch_company_data(company_name)
    # print(company_data)
    if not company_data:
        return "No data found for this company."

    years = [entry["year"] for entry in company_data]
    energy_usage = [entry["energy_usage"] for entry in company_data]
    ghg_emission = [entry["ghg_emission"] for entry in company_data]
    water_intake = [entry["water_intake"] for entry in company_data]
    waste_generation = [entry["waste_generation"] for entry in company_data]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=years, y=energy_usage, mode="lines+markers", name="Energy Usage")
    )
    fig.add_trace(
        go.Scatter(x=years, y=ghg_emission, mode="lines+markers", name="GHG Emission")
    )
    fig.add_trace(
        go.Scatter(x=years, y=water_intake, mode="lines+markers", name="Water Intake")
    )
    fig.add_trace(
        go.Scatter(
            x=years, y=waste_generation, mode="lines+markers", name="Waste Generation"
        )
    )

    fig.update_layout(
        title=f"{company_name} ESG 데이터",
        xaxis_title="Year",
        yaxis_title="Values",
        legend_title="Metrics",
        font=dict(
            size=14,
            weight="bold",
        ),
        # paper_bgcolor="#43A047",
        xaxis=dict(
            tickmode="linear",
            tick0=min(years),
            dtick=1,
            tickvals=years,
        ),
    )

    return fig


def create_company_average_plot(company_name="삼성전자"):
    data = fetch_company_average(company_name)

    if not data:
        return "No data found."

    # Plotly 바 차트 생성
    labels = list(data.keys())
    values = list(data.values())

    fig = go.Figure([go.Bar(x=labels, y=values)])

    fig.update_layout(
        title=f"Average Environmental Metrics for {company_name}",
        xaxis_title="Metrics",
        yaxis_title="Values",
        showlegend=False,
        font=dict(
            size=14,
            weight="bold",
        ),
        # paper_bgcolor="#43A047",
    )

    return fig


def create_yearly_average_plot():
    data = fetch_yearly_average()

    if not data:
        return "No data found."

    # 연도별 데이터 추출
    years = sorted(list(data.keys()))
    energy_usage = [data[year]["energy_usage"] for year in years]
    ghg_emission = [data[year]["ghg_emission"] for year in years]
    water_intake = [data[year]["water_intake"] for year in years]
    waste_generation = [data[year]["waste_generation"] for year in years]

    # Plotly 그래프 생성
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=years, y=energy_usage, mode="lines+markers", name="Energy Usage")
    )
    fig.add_trace(
        go.Scatter(x=years, y=ghg_emission, mode="lines+markers", name="GHG Emission")
    )
    fig.add_trace(
        go.Scatter(x=years, y=water_intake, mode="lines+markers", name="Water Intake")
    )
    fig.add_trace(
        go.Scatter(
            x=years, y=waste_generation, mode="lines+markers", name="Waste Generation"
        )
    )

    fig.update_layout(
        title="연도별 ESG 데이터 평균",
        xaxis_title="Year",
        yaxis_title="Values",
        legend_title="Metrics",
        xaxis=dict(tickmode="linear", tick0=min(map(int, years)), dtick=1),
        font=dict(
            size=14,
            weight="bold",
        ),
        # paper_bgcolor="#43A047",
    )

    return fig


def create_data_by_year_plot(year=2023):
    data = fetch_data_by_year(year)

    if not data:
        return "No data found."

    # 회사명과 각 지표 추출
    companies = [entry["company"] for entry in data]
    energy_usage = [entry["energy_usage"] for entry in data]
    ghg_emission = [entry["ghg_emission"] for entry in data]
    water_intake = [entry["water_intake"] for entry in data]
    waste_generation = [entry["waste_generation"] for entry in data]

    # Plotly 그래프 생성
    fig = go.Figure()

    fig.add_trace(go.Bar(x=companies, y=energy_usage, name="Energy Usage"))
    fig.add_trace(go.Bar(x=companies, y=ghg_emission, name="GHG Emission"))
    fig.add_trace(go.Bar(x=companies, y=water_intake, name="Water Intake"))
    fig.add_trace(go.Bar(x=companies, y=waste_generation, name="Waste Generation"))

    fig.update_layout(
        title=f"Environmental Data Comparison for {year}",
        xaxis_title="Company",
        yaxis_title="Values",
        barmode="group",
        legend_title="Metrics",
        font=dict(
            size=14,
            weight="bold",
        ),
        # paper_bgcolor="#43A047",
    )

    return fig


def create_max_dataframe(feature_name="energy_usage"):
    data = fetch_max_feature(feature_name)

    if not data:
        return "No data found."

    # 데이터프레임 생성
    df = pd.DataFrame([data])

    return df


def create_min_dataframe(feature_name="energy_usage"):
    data = fetch_min_feature(feature_name)

    if not data:
        return "No data found."

    # 데이터프레임 생성
    df = pd.DataFrame([data])

    return df
