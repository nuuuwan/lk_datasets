from scraper import GlobalReadMe


def main():

    GlobalReadMe(
        {
            "lk_hansard": ["lk_hansard"],
            "lk_appeal_court_judgements": ["lk_appeal_court_judgements"],
            "lk_supreme_court_judgements": ["lk_supreme_court_judgements"],
            "lk_police_press_releases": ["lk_police_press_releases"],
            "lk_legal_docs": [
                "lk_acts",
                "lk_bills",
                "lk_extraordinary_gazettes",
            ],
            "lk_cabinet_decisions": ["lk_cabinet_decisions"],
            "lk_treasury": ["lk_treasury_press_releases"],
            "lk_pmd": ["lk_pmd_press_releases"],
            "lk_news": ["lk_news"],
            "lk_tourism": [
                "lk_tourism_weekly_reports",
                "lk_tourism_monthly_reports",
            ],
        }
    ).build()


if __name__ == "__main__":
    main()
