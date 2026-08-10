from pages.gocayin.dashboard_page import DashboardPage


def test_dashboard_status_and_selection(logged_in_driver):
    # 傳入 logged_in_driver 時，畫面已經確定在 Dashboard
    dashboard = DashboardPage(logged_in_driver)

    # 1. 斷言畫面已載入
    assert dashboard.is_loaded(), "Dashboard 畫面載入失敗！"

    # 2. 印出帳號與狀態
    print(f"目前登入帳號：{dashboard.get_account_name()}")
    print(f"帳號狀態：{dashboard.get_login_account_status()}")

    # 3. 選擇內容類型
    dashboard.select_content_type("GO CAYIN meetingPost+")