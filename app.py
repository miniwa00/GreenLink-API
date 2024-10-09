import gradio as gr
from utils import *
from css import custom_css


def embed_fastapi_docs():
    return """
    <iframe src="http://127.0.0.1:8000/docs" width="100%" height="800px"></iframe>
    """


TITLE = (
    """<h1 align="center" id="space-title" style="color: green;">GreenLink API</h1>"""
)

NAME = """<p align="center" style="color: green;">GreenLink API</p>"""

EXPAINATION = """
<p align="center" style="color: black; text-align: center;">ESG 데이터를 조회할 수 있는 API 입니다.</p> 
<p align="left" style="color: black; text-align: left;"> 
    <br> 세상을 바꿀 수 있는 혁신을 추구합니다. 
    <br> 지속 가능한 미래사회 건설을 위해 이바지합니다. 
    <br> 고객의 편의를 최우선으로 생각합니다.
</p>
"""


# Gradio 인터페이스 설정
with gr.Blocks(
    css=custom_css,
    title="GreenLink API",
) as demo:
    gr.HTML(TITLE)
    gr.Markdown()
    gr.Markdown()
    with gr.Tabs(elem_classes="tab-buttons"):
        with gr.TabItem(label="Dashboard 🚀"):

            with gr.Row():
                with gr.Column():
                    with gr.Row():
                        gr.Image(
                            "pic.jpg",
                            show_download_button=False,
                            show_label=False,
                            show_fullscreen_button=False,
                            elem_id="img-box",
                            elem_classes="block",
                            width=300,
                            height=300,
                        )
                        gr.Image(
                            "name.jpg",
                            show_download_button=False,
                            show_label=False,
                            show_fullscreen_button=False,
                            elem_id="img-box",
                            elem_classes="block",
                            width=300,
                            height=300,
                        )
                    gr.Markdown()
                    gr.Markdown()
                    gr.Markdown()
                    gr.Markdown()
                    gr.Markdown(EXPAINATION, elem_classes="markdown-text-explain")
                with gr.Column(scale=2):
                    gr.Markdown("ESG 데이터 종류별 비교", elem_classes="markdown-text")
                    with gr.Row():
                        feature_dropdown = gr.Dropdown(
                            label="Feature",
                            choices=[
                                "energy_usage",
                                "ghg_emission",
                                "water_intake",
                                "waste_generation",
                            ],
                            value="energy_usage",
                            elem_id="requried-dropdown",
                            elem_classes="block-info",
                        )
                        gr.Markdown()
                        gr.Markdown()
                    feature_plot = gr.Plot(show_label=False)

                    feature_dropdown.select(
                        fn=create_data_by_feature_plot,
                        inputs=feature_dropdown,
                        outputs=feature_plot,
                    )
                    demo.load(
                        fn=create_data_by_feature_plot,
                        outputs=feature_plot,
                    )
                # gr.Markdown()

            with gr.Row():
                with gr.Column():
                    gr.Markdown("기업별 ESG 데이터 비교", elem_classes="markdown-text")
                    comparison_by_company_textbox = gr.Textbox(
                        label="Company Name",
                        placeholder="Enter company name, e.g., 삼성전자",
                        elem_id="text-box",
                        elem_classes="block-info",
                    )
                    comparison_by_company_plot = gr.Plot(show_label=False)

                    comparison_by_company_textbox.submit(
                        fn=create_company_data_plot,
                        inputs=comparison_by_company_textbox,
                        outputs=comparison_by_company_plot,
                    )
                    demo.load(
                        fn=create_company_data_plot, outputs=comparison_by_company_plot
                    )

                with gr.Column():
                    gr.Markdown("연도별 ESG 데이터 비교", elem_classes="markdown-text")
                    year_dropdown = gr.Dropdown(
                        label="Year",
                        choices=[2021, 2022, 2023],
                        value=2023,
                        elem_id="requried-dropdown",
                        elem_classes="block-info",
                    )
                    year_plot = gr.Plot(show_label=False)

                    year_dropdown.select(
                        fn=create_data_by_year_plot,
                        inputs=year_dropdown,
                        outputs=year_plot,
                    )
                    demo.load(fn=create_data_by_year_plot, outputs=year_plot)

                with gr.Column():
                    gr.Markdown("기업별 ESG 데이터 평균", elem_classes="markdown-text")
                    company_average_textbox = gr.Textbox(
                        label="Company Name",
                        placeholder="Enter company name, e.g., 삼성전자",
                        elem_id="text-box",
                        elem_classes="block-info",
                    )
                    company_average_plot = gr.Plot(show_label=False)
                    company_average_textbox.submit(
                        fn=create_company_average_plot,
                        inputs=company_average_textbox,
                        outputs=company_average_plot,
                    )
                    demo.load(
                        fn=create_company_average_plot, outputs=company_average_plot
                    )

            with gr.Row():
                with gr.Column():
                    gr.Markdown("연도별 ESG 데이터 평균", elem_classes="markdown-text")
                    yearly_average_plot = gr.Plot(show_label=False)
                    demo.load(
                        fn=create_yearly_average_plot, outputs=yearly_average_plot
                    )

                with gr.Column():
                    with gr.Column():
                        gr.Markdown("ESG 데이터 최대값", elem_classes="markdown-text")
                        max_feature_dropdown = gr.Dropdown(
                            label="Feature",
                            choices=[
                                "energy_usage",
                                "ghg_emission",
                                "water_intake",
                                "waste_generation",
                            ],
                            value="energy_usage",
                            elem_id="requried-dropdown",
                            elem_classes="block-info",
                        )
                        max_feature_df = gr.DataFrame()
                        max_feature_dropdown.select(
                            fn=create_max_dataframe,
                            inputs=max_feature_dropdown,
                            outputs=max_feature_df,
                        )
                        demo.load(fn=create_max_dataframe, outputs=max_feature_df)
                    with gr.Column():
                        gr.Markdown("ESG 데이터 최소값", elem_classes="markdown-text")
                        min_feature_dropdown = gr.Dropdown(
                            label="Feature",
                            choices=[
                                "energy_usage",
                                "ghg_emission",
                                "water_intake",
                                "waste_generation",
                            ],
                            value="energy_usage",
                            elem_id="requried-dropdown",
                            elem_classes="block-info",
                        )
                        min_feature_df = gr.DataFrame()
                        min_feature_dropdown.select(
                            fn=create_min_dataframe,
                            inputs=min_feature_dropdown,
                            outputs=min_feature_df,
                        )
                        demo.load(fn=create_min_dataframe, outputs=min_feature_df)

        with gr.TabItem(label="API Developer Documentation 📘"):
            gr.HTML(embed_fastapi_docs(), elem_id="api-docs")

# Gradio 인터페이스 실행
demo.launch(share=True)
