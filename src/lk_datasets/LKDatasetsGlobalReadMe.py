from scraper import GlobalReadMe


class LKDatasetsGlobalReadMe(GlobalReadMe):
    def __init__(self):
        super().__init__(
            {
                "lk_hansard": ["lk_hansard"],
                "lk_appeal_court_judgements": ["lk_appeal_court_judgements"],
                "lk_supreme_court_judgements": ["lk_supreme_court_judgements"],
                "lk_police_press_releases": ["lk_police_press_releases"],
                "lk_legal_docs": [
                    "lk_acts",
                    "lk_bills",
                    "lk_extraordinary_gazettes_2020s",
                    "lk_extraordinary_gazettes_2010s",
                ],
                "lk_cabinet_decisions": ["lk_cabinet_decisions"],
                "lk_treasury": ["lk_treasury_press_releases"],
                "lk_pmd": ["lk_pmd_press_releases"],
                "lk_news": ["lk_news"],
                "lk_tourism": [
                    "lk_tourism_weekly_reports",
                    "lk_tourism_monthly_reports",
                ],
                "lk_dmc": [
                    "lk_dmc_situation_reports",
                    "lk_dmc_weather_forecasts",
                    "lk_dmc_river_water_level_and_flood_warnings",
                    "lk_dmc_landslide_warnings",
                ],
                "cbsl": ["cbsl_annual_reports"],
            }
        )
