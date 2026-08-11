import time
import allure
from pages.gocayin.dashboard_page import DashboardPage
from pages.gocayin.login_page import LoginPage
from pages.gocayin.main_page import GoCayinPage


@allure.feature("GO CAYIN 登入模組")
@allure.story("使用者手動驗證碼登入與 Dashboard 驗證")
def test_login(driver):

    with allure.step("步驟 1：進入主頁並點擊登入按鈕"):
        gocayin = GoCayinPage(driver)
        login = LoginPage(driver)
        gocayin.click_login()

        login.wait_login_page()

    with allure.step("步驟 2：輸入帳號與密碼"):
        login.login("hankruan@cayintech.com", "Cayin1234")

    with allure.step("步驟 3：人工完成 reCAPTCHA 機器人驗證"):
        input("\n⚠️ 請完成機器人驗證後按 Enter 繼續...")
        # login.click_login_btn()

    with allure.step("步驟 4：等待進入 Dashboard 首頁並驗證畫面"):
        time.sleep(5)
        dashboard = DashboardPage(driver)
        assert dashboard.is_loaded(), "錯誤：Dashboard 載入失敗！"

    with allure.step("步驟 5：抓取並紀錄帳號資訊與選擇內容類型"):
        account_name = dashboard.get_account_name()
        status = dashboard.get_login_account_status()

        # 💡 小技巧：可以把文字資訊直接附在 Allure 報告的這一步中！
        allure.attach(
            f"帳號: {account_name}\n狀態: {status}",
            name="帳號詳細資訊紀錄",
            attachment_type=allure.attachment_type.TEXT,
        )

        dashboard.select_content_type("GO CAYIN meetingPost+")