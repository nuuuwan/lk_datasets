import os

from utils import File, Log

log = Log("ArXivDoc")


class ArXivDoc(File):
    LATEX_PATH = os.path.join("latex", "arxiv.tex")

    def __init__(self):
        super().__init__(self.LATEX_PATH)
        # lk_datasets_global_readme = LKDatasetsGlobalReadMe()
        # self.global_summary = lk_datasets_global_readme.global_summary
        self.global_summary = {
            "n_datasets": 13,
            "n_docs": 215552,
            "all_dataset_size": 59605072155,
        }
        log.debug(f"global_summary={self.global_summary}")
        # self.summary_list = lk_datasets_global_readme.summary_list
        self.summary_list = [
            {
                "doc_class_label": "lk_hansard",
                "doc_class_emoji": "🏛️",
                "doc_class_description": "A Hansard is the official verbatim record of parliamentary debates, preserving lawmakers’ words and decisions for history, law, and public accountability.",
                "time_updated": "2025-10-04 18:36:13",
                "n_docs": 1665,
                "n_docs_with_pdfs": 1636,
                "n_docs_with_text": 1636,
                "date_str_min": "2006-02-01",
                "date_str_max": "2025-09-24",
                "dataset_size": 17904497223,
                "url_source_list": ["https://www.parliament.lk"],
                "url_data": "https://github.com/nuuuwan/lk_hansard/tree/data/data/lk_hansard",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_hansard/refs/heads/data/data/lk_hansard/docs_by_year_and_lang.png",
                "langs": ["si-ta-en"],
                "latest_doc_d": {
                    "doc_type": "lk_hansard",
                    "doc_id": "2025-09-24-2025-09-24",
                    "num": "2025-09-24",
                    "date_str": "2025-09-24",
                    "description": "Hansard of September 24, 2025",
                    "url_metadata": "https://www.parliament.lk/en/business-of-parliament/hansards",
                    "lang": "si-ta-en",
                    "url_pdf": "https://www.parliament.lk/uploads/documents/hansard/1759314058095637.pdf",
                },
            },
            {
                "doc_class_label": "lk_appeal_court_judgements",
                "doc_class_emoji": "⚖️",
                "doc_class_description": "A Court of Appeal judgment is a higher court ruling that reviews decisions of lower courts, shaping legal precedent and protecting citizens’ rights.",
                "time_updated": "2025-10-04 18:44:41",
                "n_docs": 10146,
                "n_docs_with_pdfs": 10146,
                "n_docs_with_text": 10146,
                "date_str_min": "2012-04-23",
                "date_str_max": "2025-10-03",
                "dataset_size": 10341714312,
                "url_source_list": ["https://courtofappeal.lk"],
                "url_data": "https://github.com/nuuuwan/lk_appeal_court_judgements/tree/data/data/lk_appeal_court_judgements",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_appeal_court_judgements/refs/heads/data/data/lk_appeal_court_judgements/docs_by_year_and_lang.png",
                "langs": ["en"],
                "latest_doc_d": {
                    "doc_type": "lk_appeal_court_judgements",
                    "doc_id": "2025-10-03-CA-WRT-0056-2025",
                    "num": "CA/WRT/0056/2025",
                    "date_str": "2025-10-03",
                    "description": "Samarakoon Mudiyanselage Chaminda Prasad Samarakoon Vs. Ceylon Petroleum Corporation & 3 Others before Hon. K. M. S. DISSANAYAKE, J",
                    "url_metadata": "https://courtofappeal.lk/?page_id=13124",
                    "lang": "en",
                    "url_pdf": "https://courtofappeal.lk/?melsta_doc_download=1&doc_id=ba4daea5-6599-4213-be22-d48215c13b58&filename=WRT-0056-25%20Decided%20on%2003.09.2025.pdf.pdf",
                    "parties": "Samarakoon Mudiyanselage Chaminda Prasad Samarakoon Vs. Ceylon Petroleum Corporation & 3 Others",
                    "judgement_by": "Hon. K. M. S. DISSANAYAKE, J",
                    "keywords": "Effective date of an Interim Order issued by Court under section 2 (1) of the Court of Appeal (Appellate Procedure) Rules 1990-Is an interim order prospective or retrospective.",
                    "legistation": "Article 140 of the Constitution of the Democratic Socialist Republic of Sri Lanka.",
                },
            },
            {
                "doc_class_label": "lk_supreme_court_judgements",
                "doc_class_emoji": "⚖️",
                "doc_class_description": "A Supreme Court judgment is a binding legal decision that interprets the Constitution and laws, shaping justice, governance, and citizens’ rights.",
                "time_updated": "2025-10-04 18:44:12",
                "n_docs": 1575,
                "n_docs_with_pdfs": 1399,
                "n_docs_with_text": 1399,
                "date_str_min": "2016-07-22",
                "date_str_max": "2025-10-03",
                "dataset_size": 1280271923,
                "url_source_list": ["https://supremecourt.lk"],
                "url_data": "https://github.com/nuuuwan/lk_supreme_court_judgements/tree/data/data/lk_supreme_court_judgements",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_supreme_court_judgements/refs/heads/data/data/lk_supreme_court_judgements/docs_by_year_and_lang.png",
                "langs": ["en"],
                "latest_doc_d": {
                    "doc_type": "lk_supreme_court_judgements",
                    "doc_id": "2025-10-03-SC-CHC-APPEAL-17-2014",
                    "num": "SC/CHC APPEAL/17/2014",
                    "date_str": "2025-10-03",
                    "description": "Hon. Janak De Silva J - Anthony Saliya Godwin Ranasin...",
                    "url_metadata": "https://supremecourt.lk/judgements/",
                    "lang": "en",
                    "url_pdf": "https://supremecourt.lk/wp-content/uploads/judgements/sc_chc_appeal_17_2014.pdf",
                    "parties": "Anthony Saliya Godwin Ranasinghe, “Rose Villa”, No. 79/7, Hettiyawatte, Elpitiwala, Ragama. 2nd Defendant – Appellant Vs. Warnasirige Sinharage Paul Jayantha De Silva, No. 155/24, Dolalanda Gardens, Thalawathugoda. 1st Defendant – Respondent Commercial Bank of Ceylon PLC., No. 21, Sir Razik Fareed Mawatha, Colombo 01. And having a Branch Office and/or a Place of Business called and known as the “Thalawathugoda Branch” at No. 07, Suramya Building, Kottawa Road, Thalawathugoda. Plaintiff – Respondent\n\nView More",
                    "judgement_by": "Hon. Janak De Silva J",
                },
            },
            {
                "doc_class_label": "lk_police_press_releases",
                "doc_class_emoji": "👮\u200d♂️",
                "doc_class_description": "A police press release is an official update from law enforcement on crimes, arrests, safety alerts, or public notices, ensuring transparency and public awareness.",
                "time_updated": "2025-10-04 18:28:49",
                "n_docs": 736,
                "n_docs_with_pdfs": 736,
                "n_docs_with_text": 736,
                "date_str_min": "2025-05-01",
                "date_str_max": "2025-10-03",
                "dataset_size": 250452640,
                "url_source_list": ["https://www.police.lk"],
                "url_data": "https://github.com/nuuuwan/lk_police_press_releases/tree/data/data/lk_police_press_releases",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_police_press_releases/refs/heads/data/data/lk_police_press_releases/docs_by_month_and_lang.png",
                "langs": ["si"],
                "latest_doc_d": {
                    "doc_type": "lk_police_press_releases",
                    "doc_id": "2025-10-03-2025-10-03-11-30",
                    "num": "2025-10-03 11:30",
                    "date_str": "2025-10-03",
                    "description": "2025-10-03 11:30",
                    "url_metadata": "https://www.police.lk/?p=15487",
                    "lang": "si",
                    "url_pdf": "https://www.police.lk/wp-content/uploads/2025/10/Media-on-2025.10.03-at-1130.pdf",
                    "time_str": "2025-10-03 11:30",
                },
            },
            {
                "doc_class_label": "lk_acts",
                "doc_class_emoji": "⚖️",
                "doc_class_description": "A legal act is a law passed by Parliament that governs rights, duties, economy, and society, shaping daily life and national policy.",
                "time_updated": "2025-10-04 18:42:02",
                "n_docs": 3928,
                "n_docs_with_pdfs": 3922,
                "n_docs_with_text": 3922,
                "date_str_min": "1981-01-22",
                "date_str_max": "2025-09-22",
                "dataset_size": 6792718866,
                "url_source_list": ["https://documents.gov.lk"],
                "url_data": "https://github.com/nuuuwan/lk_legal_docs/tree/data_lk_acts/data/lk_acts",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_legal_docs/refs/heads/data_lk_acts/data/lk_acts/docs_by_decade_and_lang.png",
                "langs": ["en", "ta", "si"],
                "latest_doc_d": {
                    "doc_type": "lk_acts",
                    "doc_id": "2025-09-22-2025-09-22-19-2025-ta",
                    "num": "2025-09-22-19-2025-ta",
                    "date_str": "2025-09-22",
                    "description": "National Audit (Amendment)",
                    "url_metadata": "https://documents.gov.lk/view/acts/acts_2025.html",
                    "lang": "ta",
                    "url_pdf": "https://documents.gov.lk/view/acts/2025/9/19-2025_T.pdf",
                    "doc_number": "19/2025",
                },
            },
            {
                "doc_class_label": "lk_bills",
                "doc_class_emoji": "⚖️",
                "doc_class_description": "A Bill is a draft law proposed in Parliament. It becomes binding once passed and enacted, shaping governance, rights, and daily life in the country.",
                "time_updated": "2025-10-04 18:37:26",
                "n_docs": 4077,
                "n_docs_with_pdfs": 4076,
                "n_docs_with_text": 4076,
                "date_str_min": "2010-05-10",
                "date_str_max": "2025-10-26",
                "dataset_size": 1797815696,
                "url_source_list": ["https://documents.gov.lk"],
                "url_data": "https://github.com/nuuuwan/lk_legal_docs/tree/data_lk_bills/data/lk_bills",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_legal_docs/refs/heads/data_lk_bills/data/lk_bills/docs_by_year_and_lang.png",
                "langs": ["si", "ta", "en"],
                "latest_doc_d": {
                    "doc_type": "lk_bills",
                    "doc_id": "2025-10-26-2025-10-26-639-2025-ta",
                    "num": "2025-10-26-639-2025-ta",
                    "date_str": "2025-10-26",
                    "description": "Appropriation - Bill",
                    "url_metadata": "https://documents.gov.lk/view/bills/bl_2025.html",
                    "lang": "ta",
                    "url_pdf": "https://documents.gov.lk/view/bills/2025/10/639-2025_T.pdf",
                    "doc_number": "639/2025",
                },
            },
            {
                "doc_class_label": "lk_extraordinary_gazettes",
                "doc_class_emoji": "⚖️",
                "doc_class_description": "An Extraordinary Gazette is an official government publication used to announce urgent laws, regulations, or public notices with immediate effect.",
                "time_updated": "2025-10-04 18:39:51",
                "n_docs": 101532,
                "n_docs_with_pdfs": 22925,
                "n_docs_with_text": 22601,
                "date_str_min": "2010-01-01",
                "date_str_max": "2025-10-03",
                "dataset_size": 19355144888,
                "url_source_list": ["https://documents.gov.lk"],
                "url_data": "https://github.com/nuuuwan/lk_legal_docs/tree/data_lk_extraordinary_gazettes/data/lk_extraordinary_gazettes",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_legal_docs/refs/heads/data_lk_extraordinary_gazettes/data/lk_extraordinary_gazettes/docs_by_year_and_lang.png",
                "langs": ["ta", "si", "en"],
                "latest_doc_d": {
                    "doc_type": "lk_extraordinary_gazettes",
                    "doc_id": "2025-10-03-2025-10-03-2456-73-si",
                    "num": "2025-10-03-2456-73-si",
                    "date_str": "2025-10-03",
                    "description": "Ministry of Labour - The Wages Boards Ordinance. Nominated Members of the Wages Board.",
                    "url_metadata": "https://documents.gov.lk/view/extra-gazettes/egz_2025.html",
                    "lang": "si",
                    "url_pdf": "https://documents.gov.lk/view/extra-gazettes/2025/10/2456-73_S.pdf",
                    "doc_number": "2456/73",
                },
            },
            {
                "doc_class_label": "lk_cabinet_decisions",
                "doc_class_emoji": "🏛️",
                "doc_class_description": "A Sri Lanka Cabinet Decision is an official policy or action agreed by the Cabinet of Ministers, shaping governance, law, and national development in the country.",
                "time_updated": "2025-10-04 18:08:09",
                "n_docs": 10369,
                "n_docs_with_pdfs": 0,
                "n_docs_with_text": 10369,
                "date_str_min": "2010-09-27",
                "date_str_max": "2025-09-22",
                "dataset_size": 125308971,
                "url_source_list": ["https://www.cabinetoffice.gov.lk"],
                "url_data": "https://github.com/nuuuwan/lk_cabinet_decisions/tree/data/data/lk_cabinet_decisions",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_cabinet_decisions/refs/heads/data/data/lk_cabinet_decisions/docs_by_year_and_lang.png",
                "langs": ["en", "si"],
                "latest_doc_d": {
                    "doc_type": "lk_cabinet_decisions",
                    "doc_id": "2025-09-22-015-si",
                    "num": "15",
                    "date_str": "2025-09-22",
                    "description": "නව ක්ෂුද්\u200dර මූල්\u200dය හා ණය නියාමන අධිකාරිය පනත් කෙටුම්පත",
                    "url_metadata": "https://www.cabinetoffice.gov.lk/cab/index.php?option=com_content&view=article&id=16&Itemid=49&lang=si&dID=13451",
                    "lang": "si",
                    "decision_details_title": "2025-09-22 දිනැති අමාත්\u200dය මණ්ඩල තීරණය පිලිබඳ මාධ්\u200dය ප්\u200dරකාශය (මීලග රැස්වීමේදී සම්මත කිරීමට යටත්ව)",
                    "decision_details_body": "- ශ්\u200dරී ලංකාව තුළ ක්ෂුද්\u200dර මූල්\u200dය කර්මාන්තය සඳහා පුළුල් නියාමන රාමුවක් ස්ථාපිත කිරීම උදෙසා 2016 අංක 6 දරන ක්ෂුද්\u200dරමූල්\u200dය පනතේ ප්\u200dරතිපාදන ප්\u200dරමාණවත් නොවීම හේතුවෙන් නව ක්ෂුද්\u200dර මූල්\u200dය හා ණය නියාමන අධිකාරිය පනත හඳුන්වා දීම පිණිස මීට පෙර අමාත්\u200dය මණ්ඩල අනුමැතිය ලබා දී තිබේ. ඒ අනුව, සකස් කරන ලද පනත් කෙටුම්පත රජයේ ගැසට් පත්\u200dරයේ පළ කිරීමෙන් අනතුරුව එම පනත් කෙටුම්පතට එරෙහිව විවිධ පාර්ශ්වයන් විසින් ශ්\u200dරේෂ්ඨාධිකරණයේ පෙත්සම් 07ක් ගොනු කර ඇත. එම පෙත්සම් සම්බන්ධයෙන් ශ්\u200dරේෂ්ඨාධිකරණය විසින් ලබා දී ඇති තීරණය හා පාර්ලිමේන්තුවේ 'ආර්ථික අර්බුදය බලපෑම සමනය කිරීම පිළිබඳ ආංශික අධීක්ෂණ කාරක සභාව' විසින් ලබා දෙන ලද මඟ පෙන්වීම ද සැලකිල්ලට ගනිමින් නව පනත් කෙටුම්පතක් සකස් කිරීමට මුදල්, ක්\u200dරමසම්පාදන සහ ආර්ථික සංවර්ධන අමාත්\u200dයාංශය සහ ශ්\u200dරී ලංකා මහ බැංකුව විසින් අවධානය යොමු කර තිබේ. ඒ අනුව, නව ක්ෂුද්\u200dර මූල්\u200dය හා ණය නියාමන අධිකාරිය පනත හඳුන්වා දීම සඳහා 2025-08-11 දින පැවැති අමාත්\u200dය මණ්ඩල රැස්වීමේ දී අනුමැතිය ලබා දී ඇත. නීති කෙටුම්පත් සම්පාදක විසින් සකස් කරන ලද නව පනත් කෙටුම්පත සඳහා නීතිපතිගේ නිෂ්කාශනය ලැබී තිබේ. එකී ක්ෂුද්\u200dර මූල්\u200dය හා ණය නියාමන අධිකාරිය පනත් කෙටුම්පත රජයේ ගැසට් පත්\u200dරයේ පළ කිරීමටත්, ඉන් අනතුරුව අනුමැතිය සඳහා පාර්ලිමේන්තුවට ඉදිරිපත් කිරීමටත්\xa0 මුදල්, ක්\u200dරමසම්පාදන සහ ආර්ථික සංවර්ධන අමාත්\u200dය වශයෙන් ගරු ජනාධිපතිතුමා ඉදිරිපත් කළ යෝජනාව අමාත්\u200dය මණ්ඩලය විසින් අනුමත කරන ලදී.",
                },
            },
            {
                "doc_class_label": "lk_treasury_press_releases",
                "doc_class_emoji": "💰",
                "doc_class_description": "A Sri Lanka Treasury press release shares key govt financial updates—on budgets, debt, or policy—vital for transparency, guiding investors, citizens, and markets on the nation’s economic direction.",
                "time_updated": "2025-10-04 18:18:09",
                "n_docs": 133,
                "n_docs_with_pdfs": 133,
                "n_docs_with_text": 133,
                "date_str_min": "2015-09-08",
                "date_str_max": "2025-07-30",
                "dataset_size": 142939539,
                "url_source_list": ["https://www.treasury.gov.lk"],
                "url_data": "https://github.com/nuuuwan/lk_treasury/tree/data_lk_treasury_press_releases/data/lk_treasury_press_releases",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_treasury/refs/heads/data_lk_treasury_press_releases/data/lk_treasury_press_releases/docs_by_year_and_lang.png",
                "langs": ["en", "si"],
                "latest_doc_d": {
                    "doc_type": "lk_treasury_press_releases",
                    "doc_id": "2025-07-30-d1aea6",
                    "num": "d1aea6",
                    "date_str": "2025-07-30",
                    "description": "Investor Call in Relation to Macro-Linked and Governance-Linked Bonds",
                    "url_metadata": "https://www.treasury.gov.lk//web/press-releases/section/2025",
                    "lang": "en",
                    "url_pdf": "https://www.treasury.gov.lk//api/file/bf543476-9d80-4115-8f1f-4b1eb0a8526c",
                },
            },
            {
                "doc_class_label": "lk_pmd_press_releases",
                "doc_class_emoji": "📢",
                "doc_class_description": "A Sri Lanka Presidential Media Division press release shares official updates on national decisions, policies, or events. It’s vital as the authoritative source ensuring transparency and public awareness.",
                "time_updated": "2025-09-26 08:23:47",
                "n_docs": 2182,
                "n_docs_with_pdfs": 0,
                "n_docs_with_text": 2182,
                "date_str_min": "2024-09-23",
                "date_str_max": "2025-09-24",
                "dataset_size": 55904500,
                "url_source": "https://pmd.gov.lk",
                "url_data": "https://github.com/nuuuwan/lk_pmd/tree/data_lk_pmd_press_releases/data/lk_pmd_press_releases",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_pmd/refs/heads/data_lk_pmd_press_releases/data/lk_pmd_press_releases/docs_by_month_and_lang.png",
                "langs": ["si", "ta", "en"],
                "latest_doc_d": {
                    "doc_type": "lk_pmd_press_releases",
                    "doc_id": "2025-09-24-ta-f6263c",
                    "num": "ta-f6263c",
                    "date_str": "2025-09-24",
                    "description": "ஜனாதிபதிக்கும் பாகிஸ்தான் பிரதமருக்கும் இடையே இருதரப்பு பேச்சுவார்த்தைகள்",
                    "url_metadata": "https://pmd.gov.lk/ta/%e0%ae%9a%e0%af%86%e0%ae%af%e0%af%8d%e0%ae%a4%e0%ae%bf/%e0%ae%9c%e0%ae%a9%e0%ae%be%e0%ae%a4%e0%ae%bf%e0%ae%aa%e0%ae%a4%e0%ae%bf%e0%ae%95%e0%af%8d%e0%ae%95%e0%af%81%e0%ae%ae%e0%af%8d-%e0%ae%aa%e0%ae%be%e0%ae%95%e0%ae%bf%e0%ae%b8%e0%af%8d%e0%ae%a4%e0%ae%be/",
                    "lang": "ta",
                },
            },
            {
                "doc_class_label": "lk_news",
                "doc_class_emoji": "📄",
                "doc_class_description": "A collection of lk_news documents.",
                "time_updated": "2025-10-04 18:41:30",
                "n_docs": 79049,
                "n_docs_with_pdfs": 0,
                "n_docs_with_text": 79049,
                "date_str_min": "2021-09-12",
                "date_str_max": "2025-10-04",
                "dataset_size": 1157884624,
                "url_source_list": [
                    "http://sinhala.adaderana.lk",
                    "https://www.virakesari.lk",
                    "https://www.tamilmirror.lk",
                    "https://www.adaderana.lk",
                    "https://www.ada.lk",
                    "https://www.ft.lk",
                    "http://island.lk",
                    "https://economynext.com",
                    "https://www.dailymirror.lk",
                    "https://www.colombotelegraph.com",
                    "https://www.bbc.com",
                    "https://dbsjeyaraj.com",
                    "https://www.lankadeepa.lk",
                    "https://www.newsfirst.lk",
                    "https://english.newsfirst.lk",
                ],
                "url_data": "https://github.com/nuuuwan/lk_news/tree/data/data/lk_news",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_news/refs/heads/data/data/lk_news/docs_by_month_and_lang.png",
                "langs": ["en", "ta", "si"],
                "latest_doc_d": {
                    "doc_type": "lk_news",
                    "doc_id": "2025-10-04-lankadeepalk-62c61e02",
                    "num": "lankadeepalk-62c61e02",
                    "date_str": "2025-10-04",
                    "description": "‘‘ආණ්ඩුව හොඳ ගමනක් යනවා‘‘",
                    "url_metadata": "https://www.lankadeepa.lk/latest_news/ආණඩව-හඳ-ගමනක-යනව/1-680736",
                    "lang": "si",
                    "newspaper_id": "lankadeepalk",
                    "time_ut": 1759581231.0,
                },
            },
            {
                "doc_class_label": "lk_tourism_weekly_reports",
                "doc_class_emoji": "🌴",
                "doc_class_description": "Report on Weekly Tourist Arrivals to Sri Lanka.",
                "time_updated": "2025-10-04 18:36:40",
                "n_docs": 33,
                "n_docs_with_pdfs": 33,
                "n_docs_with_text": 33,
                "date_str_min": "2023-01-01",
                "date_str_max": "2025-09-01",
                "dataset_size": 91539272,
                "url_source_list": ["https://www.sltda.gov.lk"],
                "url_data": "https://github.com/nuuuwan/lk_tourism/tree/data_lk_tourism_weekly_reports/data/lk_tourism_weekly_reports",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_tourism/refs/heads/data_lk_tourism_weekly_reports/data/lk_tourism_weekly_reports/docs_by_month_and_lang.png",
                "langs": ["en"],
                "latest_doc_d": {
                    "doc_type": "lk_tourism_weekly_reports",
                    "doc_id": "2025-09-01-2025-09-01",
                    "num": "2025-09-01",
                    "date_str": "2025-09-01",
                    "description": "TOURIST ARRIVALS - 2025 - September",
                    "url_metadata": "https://www.sltda.gov.lk/en/weekly-tourist-arrivals-reports-2025",
                    "lang": "en",
                    "url_pdf": "https://www.sltda.gov.lk/storage/common_media/Weekly_Report_1st_to_30th_September_2025.pdf",
                },
            },
            {
                "doc_class_label": "lk_tourism_monthly_reports",
                "doc_class_emoji": "🌴",
                "doc_class_description": "Report on Monthly Tourist Arrivals to Sri Lanka.",
                "time_updated": "2025-10-04 18:36:59",
                "n_docs": 127,
                "n_docs_with_pdfs": 126,
                "n_docs_with_text": 126,
                "date_str_min": "2015-01-01",
                "date_str_max": "2025-08-01",
                "dataset_size": 308879703,
                "url_source_list": [
                    "https://sltda.gov.lk",
                    "https://www.sltda.gov.lk",
                ],
                "url_data": "https://github.com/nuuuwan/lk_tourism/tree/data_lk_tourism_monthly_reports/data/lk_tourism_monthly_reports",
                "url_chart": "https://raw.githubusercontent.com/nuuuwan/lk_tourism/refs/heads/data_lk_tourism_monthly_reports/data/lk_tourism_monthly_reports/docs_by_year_and_lang.png",
                "langs": ["en"],
                "latest_doc_d": {
                    "doc_type": "lk_tourism_monthly_reports",
                    "doc_id": "2025-08-01-2025-08-01",
                    "num": "2025-08-01",
                    "date_str": "2025-08-01",
                    "description": "Arrivals Report August 2025",
                    "url_metadata": "https://www.sltda.gov.lk/en/monthly-tourist-arrivals-reports-2025",
                    "lang": "en",
                    "url_pdf": "https://www.sltda.gov.lk/storage/common_media/Monthly_Tourits_Arrivals_Report-August-2025-Final.pdf",
                },
            },
        ]
        log.debug(f"summary_list={self.summary_list}")
        self.n_datasets = self.global_summary["n_datasets"]
        self.n_docs = self.global_summary["n_docs"]
        self.all_dataset_size_humanized = File.humanize_size(
            self.global_summary["all_dataset_size"]
        )

    def build(self):
        self.write(self.content)
        log.info(f"Wrote {self.path}")
        os.system(f"pdflatex -output-directory=latex {self.LATEX_PATH}")
        for ext in ["aux", "log", "out"]:
            os.remove(os.path.join("latex", f"arxiv.{ext}"))
        log.info("Generated PDF.")

    @property
    def content_abstract(self):
        return (
            r"""
\begin{abstract}
"""
            + f"""
We present a collection of open, machine-readable document datasets covering
parliamentary proceedings, legal judgments, government publications, news, and
tourism statistics from Sri Lanka. The collection currently comprises
$\\sim${self.n_docs:,} documents ({self.all_dataset_size_humanized})
across {self.n_datasets} datasets in Sinhala, Tamil, and
English, updated daily and mirrored on GitHub and Hugging Face. These datasets
aim to support research in computational linguistics, legal analytics,
socio-political studies, and multilingual natural language processing. We
describe the sources, collection pipeline, formats, and potential use cases,
while discussing licensing and ethical considerations.
"""
            + """
\\end{abstract}
            """
        )

    def get_content_subsection_dataset(self, summary):
        title = (
            summary["doc_class_label"]
            .replace("lk_", "")
            .replace("_", " ")
            .title()
        )
        return f"""
\\subsection{{{title}}}
"""

    @property
    def content_section_datasets(self):
        return r"""
\section{Datasets}
""" + "\n\n".join(
            [
                self.get_content_subsection_dataset(summary)
                for summary in self.summary_list
            ]
        )

    @property
    def content(self):
        return (
            r"""

\documentclass[11pt]{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{margin=1in}

\title{%
Sri Lanka Document Datasets: \\
A Large-Scale, Multilingual Resource for Law, News, and Policy
}

\author{Nuwan I. Senaratna \small{Independent Researcher} \\
\texttt{nuwans@alumni.stanford.edu}
}

\date{\today}

\begin{document}

\maketitle

"""
            + self.content_abstract
            + r"""

\section{Introduction}

\section{Related Work}

"""
            + self.content_section_datasets
            + r"""

\section{Data Collection Pipeline}

\section{Licensing and Access}

\section{Conclusion and Future Work}

\bibliographystyle{plain}
\bibliography{references}

\end{document}

    """
        )
